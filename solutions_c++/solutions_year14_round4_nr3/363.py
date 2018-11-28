#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>

#define eps 1e-6
#define Inf 1e8

using namespace std; 

class PART_CTR
{
public:
	int ctr_num;
	double ctr[200][200];
	double dim_num;
	int odist_num, theta_num;
	double ave_sigma;
};

class PART{
public:
	double feat[200];
	int cnt_feat;
};

PART parts[10];
PART parts_set[20];
PART gd, ga;

PART_CTR parts_ctr[6];
PART_CTR parts_set_ctr[15];
PART_CTR global_dist, global_ang;

FILE *fpsq, *fphq;

double calc_dist(double*a, double *b, int odist_num, int theta_num)
{
	int feat_num = odist_num+theta_num;
	double dist1 = 0;
	for (int iFeat=0;iFeat<odist_num;++iFeat)
	{
		dist1 += (a[iFeat]-b[iFeat])*(a[iFeat]-b[iFeat]);
	}
	dist1 = sqrt(dist1);

	double dist2 = 0;
	for (int iFeat=odist_num;iFeat<feat_num;++iFeat)
	{
		dist2 += 1-cos(a[iFeat]-b[iFeat]);
	}

	if (abs(dist1)<eps)
		return dist2;
	if (abs(dist2)<eps)
		return dist1;
	return sqrt(dist1*dist2);
}

void soft_quantization(PART p, PART_CTR C)
{
	//output ctr_num double prob
	double dist[200];
	double w[200];
	double sum_dist = 0;
	double ave_feat[200];
	for (int iFeat=0;iFeat<C.dim_num;++iFeat)
		ave_feat[iFeat] = 0;
	// guassian ; daizy
	for (int iCtrNum=0;iCtrNum<C.ctr_num;++iCtrNum)
	{
		dist[iCtrNum] = calc_dist(p.feat, C.ctr[iCtrNum], C.odist_num, C.theta_num);
		sum_dist += dist[iCtrNum];

		for (int iFeat=0;iFeat<C.dim_num;++iFeat)
		{
			ave_feat[iFeat] += C.ctr[iCtrNum][iFeat];
		}
	}
	double sum_w = 0;
	for (int iCtrNum=0;iCtrNum<C.ctr_num;++iCtrNum)
	{
		w[iCtrNum] = exp(-dist[iCtrNum]/(2*C.ave_sigma));
		sum_w += w[iCtrNum];
	}
	for (int iCtrNum=0;iCtrNum<C.ctr_num;++iCtrNum)
	{
		w[iCtrNum] /= sum_w;
		fprintf(fpsq, "%f ", w[iCtrNum]);
	}
	fprintf(fpsq, "\n");
}

void hard_quantization(PART p, PART_CTR C)
{
	double min_dist = Inf;
	int min_ctr = -1;
	for (int iCtrNum=0;iCtrNum<C.ctr_num;++iCtrNum)
	{
		double tmp = calc_dist(p.feat, C.ctr[iCtrNum], C.odist_num, C.theta_num);
		if (tmp<min_dist)
		{
			min_dist = tmp;
			min_ctr = iCtrNum;
		}
	}
	fprintf(fphq, "%d ", min_ctr);
}

void solve()
{
	char ictrfn[1000];
	int part_ctr_num[6] = {2,6,6,2,4,4};
	int part_feat_dim[6] = {2,4,4,2,4,4};
	for (int iCtr=0;iCtr<6;++iCtr)
	{
		sprintf(ictrfn, "..\\..\\Cluster\\Kmeans\\part_ctr_%d.txt", iCtr+1);
		FILE *frep = freopen(ictrfn, "r", stdin);
		parts_ctr[iCtr].ctr_num = part_ctr_num[iCtr];
		parts_ctr[iCtr].dim_num = part_feat_dim[iCtr];
		parts_ctr[iCtr].odist_num = 0;
		parts_ctr[iCtr].theta_num = part_feat_dim[iCtr];
		//daizy?
		parts_ctr[iCtr].ave_sigma = 1;
		for (int iCtrNum=0;iCtrNum<parts_ctr[iCtr].ctr_num;++iCtrNum)
			for (int iFeat=0;iFeat<parts_ctr[iCtr].dim_num;++iFeat)
				scanf("%lf", &parts_ctr[iCtr].ctr[iCtrNum][iFeat]);
		fclose(frep);
	}

	int part_set_num = 0;
	int ps_dim_num[15] = {6,6,9,4,6,6,6,9,9,6,6,9,9,6,9};
	int ps_ctr_num = 3;
	for (int iPart=1;iPart<=6;++iPart)
	{
		for (int jPart=1;jPart<iPart;++jPart)
		{
			sprintf(ictrfn, "..\\..\\Cluster\\Kmeans\\part_set_ctr_%d_%d.txt", iPart, jPart);
			FILE* frep = freopen(ictrfn, "r", stdin);
			for (int iCtrNum=0;iCtrNum<ps_ctr_num;++iCtrNum)
				for (int iFeat=0;iFeat<ps_dim_num[part_set_num];++iFeat)
					scanf("%lf", &parts_set_ctr[part_set_num].ctr[iCtrNum][iFeat]);
			parts_set_ctr[part_set_num].ctr_num = 3;
			parts_set_ctr[part_set_num].odist_num = ps_dim_num[part_set_num];
			parts_set_ctr[part_set_num].dim_num = ps_dim_num[part_set_num];
			parts_set_ctr[part_set_num].theta_num = 0;
			//daizy
			parts_set_ctr[part_set_num].ave_sigma = 1;
			part_set_num++;
			fclose(frep);
		}
	}

	int gd_ctr_nun = 25;
	FILE* frep = freopen("..\\..\\Cluster\\Kmeans\\global_ctr_dist.txt", "r", stdin);
	for (int iCtrNum=0;iCtrNum<gd_ctr_nun;++iCtrNum)
		for (int iFeat=0;iFeat<105;++iFeat)
			scanf("%lf", &global_dist.ctr[iCtrNum][iFeat]);
	global_dist.ctr_num = gd_ctr_nun;
	global_dist.dim_num = 105;
	global_dist.odist_num = global_dist.dim_num;
	global_dist.theta_num = 0;
	global_dist.ave_sigma = 1;
	fclose(frep);

	int ga_ctr_num = 25;
	frep = freopen("..\\..\\Cluster\\Kmeans\\global_ctr_ang.txt", "r", stdin);
	for (int iCtrNum=0;iCtrNum<ga_ctr_num;++iCtrNum)
		for (int iFeat=0;iFeat<28;++iFeat)
			scanf("%lf", &global_ang.ctr[iCtrNum][iFeat]);
	global_ang.ctr_num = ga_ctr_num;
	global_ang.dim_num = 28;
	global_ang.odist_num = 0;
	global_ang.theta_num = global_ang.dim_num;
	global_ang.ave_sigma = 1;
	fclose(frep);

	int a1 = 1, a2 = 20;
	int s1 = 1, s2 = 10;
	int e1 = 1, e2 = 3;

	char ifn[1000];
	char ofn[2][1000];

	for (int a=a1;a<=a2;++a)
	{
		for (int s=s1;s<=s2;++s)
		{
			for (int e=e1;e<=e2;++e)
			{
				sprintf(ifn, "..\\..\\Feature\\[part_feat]_a%02d_s%02d_e%02d_skeleton3D.txt", a,s,e);
				FILE *frep = freopen(ifn, "r", stdin);
				if (!frep) continue;
				printf("%d %d %d\n", a,s,e);
				double tmp_feat;
				int cnt_feat;

				sprintf(ofn[0], "SQ\\[SoftQuantizationPart]a%02d_s%02d_e%02d_skeleton3D.txt",a,s,e);
				fpsq = fopen(ofn[0], "w");

				sprintf(ofn[1], "HQ\\[HardQuantizationPart]a%02d_s%02d_e%02d_skeleton3D.txt",a,s,e);
				fphq = fopen(ofn[1], "w");

				while (~scanf("%lf", &tmp_feat))
				{
					cnt_feat = 0;
					parts[1].feat[cnt_feat++] = tmp_feat;
					for (int iAng=1;iAng<2;++iAng)
					{
						scanf("%lf", &tmp_feat);
						parts[1].feat[cnt_feat++] = tmp_feat;
					}
					parts[1].cnt_feat = cnt_feat;

					for (int iPart=2;iPart<=3;++iPart)
					{
						cnt_feat = 0;
						for (int iAng=0;iAng<4;++iAng)
						{
							scanf("%lf", &tmp_feat);
							parts[iPart].feat[cnt_feat++] = tmp_feat;
						}
						parts[iPart].cnt_feat = cnt_feat;
					}

					cnt_feat = 0;
					for (int iAng=0;iAng<2;++iAng)
					{
						scanf("%lf", &tmp_feat);
						parts[4].feat[cnt_feat++] = tmp_feat;
					}
					parts[4].cnt_feat = cnt_feat;

					for (int iPart=5;iPart<=6;++iPart)
					{
						cnt_feat = 0;
						for (int iAng=0;iAng<4;++iAng)
						{
							scanf("%lf", &tmp_feat);
							parts[iPart].feat[cnt_feat++] = tmp_feat;
						}
						parts[iPart].cnt_feat = cnt_feat;
					}

					for (int iPart=1;iPart<=6;++iPart)
					{
						soft_quantization(parts[iPart], parts_ctr[iPart-1]);
						hard_quantization(parts[iPart], parts_ctr[iPart-1]);
					}
					fprintf(fphq, "\n");
				}
				fclose(frep);
				fclose(fpsq);
				fclose(fphq);

				sprintf(ifn, "..\\..\\Feature\\[part_set_feat]_a%02d_s%02d_e%02d_skeleton3D.txt", a,s,e);
				frep = freopen(ifn, "r", stdin);
				if (!frep) continue;

				double ps_tmp_feat[110];

				sprintf(ofn[0], "SQ\\[SoftQuantizationPS]a%02d_s%02d_e%02d_skeleton3D.txt",a,s,e);
				fpsq = fopen(ofn[0], "w");

				sprintf(ofn[1], "HQ\\[HardQuantizationPS]a%02d_s%02d_e%02d_skeleton3D.txt",a,s,e);
				fphq = fopen(ofn[1], "w");

				while(~scanf("%lf", &ps_tmp_feat[0]))
				{
					for (int iFeat=1;iFeat<106;++iFeat)
					{
						scanf("%lf", &ps_tmp_feat[iFeat]);
					}
					int upB = 0;
					int lowB = 0;
					int iFeat = 0;
					for (int iSeg=0;iSeg<15;++iSeg)
					{
						upB += ps_dim_num[iSeg];
						for (;iFeat<upB;++iFeat)
						{
							parts_set[iSeg].feat[iFeat-lowB] = ps_tmp_feat[iFeat];
						}
						lowB = upB;
						parts_set[iSeg].cnt_feat = ps_dim_num[iSeg];
					}

					for (int iSeg=0;iSeg<15;++iSeg)
					{
						soft_quantization(parts_set[iSeg], parts_set_ctr[iSeg]);
						hard_quantization(parts_set[iSeg], parts_set_ctr[iSeg]);
					}
					fprintf(fphq, "\n");
				}
				fclose(frep);
				fclose(fphq);
				fclose(fpsq);

				sprintf(ifn, "..\\..\\Feature\\[dist_feat]_a%02d_s%02d_e%02d_skeleton3D.txt", a,s,e);
				frep = freopen(ifn, "r", stdin);
				if (!frep) continue;
				sprintf(ofn[0], "SQ\\[SoftQuantizationGD]a%02d_s%02d_e%02d_skeleton3D.txt",a,s,e);
				fpsq = fopen(ofn[0], "w");
				sprintf(ofn[1], "HQ\\[HardQuantizationGD]a%02d_s%02d_e%02d_skeleton3D.txt",a,s,e);
				fphq = fopen(ofn[1], "w");
				while(~scanf("%lf", &gd.feat[0]))
				{
					for (int iFeat=1;iFeat<global_dist.dim_num;++iFeat)
					{
						scanf("%lf", &gd.feat[iFeat]);
					}
					gd.cnt_feat = global_dist.dim_num;

					soft_quantization(gd, global_dist);
					hard_quantization(gd, global_dist);
					fprintf(fphq, "\n");
				}
				fclose(frep);
				fclose(fphq);
				fclose(fpsq);

				sprintf(ifn, "..\\..\\Feature\\[ang_feat]_a%02d_s%02d_e%02d_skeleton3D.txt", a,s,e);
				frep = freopen(ifn, "r", stdin);
				if (!frep) continue;
				sprintf(ofn[0], "SQ\\[SoftQuantizationGA]a%02d_s%02d_e%02d_skeleton3D.txt",a,s,e);
				fpsq = fopen(ofn[0], "w");
				sprintf(ofn[1], "HQ\\[HardQuantizationGA]a%02d_s%02d_e%02d_skeleton3D.txt",a,s,e);
				fphq = fopen(ofn[1], "w");
				while(~scanf("%lf", &ga.feat[0]))
				{
					for (int iFeat=1;iFeat<global_ang.dim_num;++iFeat)
					{
						scanf("%lf", &ga.feat[iFeat]);
					}
					gd.cnt_feat = global_ang.dim_num;

					soft_quantization(ga, global_ang);
					hard_quantization(ga, global_ang);
					fprintf(fphq, "\n");
				}
				fclose(frep);
				fclose(fphq);
				fclose(fpsq);
			}
		}
	}
}

int main()
{

	freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int ln_t;
    scanf("%d", &ln_t);
    for (int ln_cas=1;ln_cas<=ln_t;++ln_cas)
    {
        printf("Case #%d:\n", ln_cas);
        solve();
    }
    return 0;
}
