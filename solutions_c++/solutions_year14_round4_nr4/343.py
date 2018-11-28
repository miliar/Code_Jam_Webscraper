#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector> 

using namespace std;

class AngAttr{
public:
	int attr[14][30];
	AngAttr()
	{
		memset(attr, 0, sizeof(attr));
	}
};

class LimbAttr{
	public:
	int attr[4][2];
	LimbAttr()
	{
		memset(attr, 0, sizeof(attr));
	}
};

class PsAttr{
	public:
	int attr[10][2];
	PsAttr()
	{
		memset(attr, 0, sizeof(attr));
	}
};

class PosAttr{
public:
	int attr[1][30];
	PosAttr()
	{
		memset(attr, 0, sizeof(attr));
	}
};

class OriAttr{
public:
	int attr[1][42];
	OriAttr()
	{
		memset(attr, 0, sizeof(attr));
	}
};

vector <AngAttr> ang[20];
vector <LimbAttr> limb[20];
vector <PsAttr> ps[20];
vector <PosAttr> pos[20];
vector <OriAttr> ori[20];

vector <AngAttr> ang_test[20];
vector <LimbAttr> limb_test[20];
vector <PsAttr> ps_test[20];
vector <PosAttr> pos_test[20];
vector <OriAttr> ori_test[20];

int ang_map[6][6];
int limb_map[2][2];
int ps_map[2][2];
int pos_map[6][6];
int ori_map[7][7];

void generate(int a1, int a2, int s1, int s2, int e1, int e2, char* ofn1, char* ofn2)
{
	char ifn[1000];

	vector < vector <int> > ang_feat;
	vector < vector <int> > limb_feat;
	vector < vector <int> > ps_feat;
	vector < vector <int> > pos_feat;
	vector < vector <int> > ori_feat;

	int ang_num = 14;
	int limb_num = 4;
	int ps_num = 10;
	int pos_num = 1;
	int ori_num = 1;

	int n_ang_attr = 30;
	int n_limb_attr = 2;
	int n_ps_attr = 2;
	int n_pos_attr = 30;
	int n_ori_attr = 42;

	int idx = 0;
	for (int iOri=0;iOri<6;++iOri)
	{
		for (int jOri=0;jOri<6;++jOri)
		{
			if (iOri == jOri) 
			{
				ang_map[iOri][jOri] = -1;
				pos_map[iOri][jOri] = -1;
			}
			else
			{
				ang_map[iOri][jOri] = idx;
				pos_map[iOri][jOri] = idx;
				idx++;
			}
		}
	}

	idx = 0;
	for (int iOri=0;iOri<2;++iOri)
	{
		for (int jOri=0;jOri<2;++jOri)
		{
			if (iOri == jOri) 
			{
				limb_map[iOri][jOri] = -1;
				ps_map[iOri][jOri] = -1;
			}
			else
			{
				limb_map[iOri][jOri] = idx;
				ps_map[iOri][jOri] = idx;
				idx++;
			}
		}
	}

	idx = 0;
	for (int iOri=0;iOri<7;++iOri)
	{
		for (int jOri=0;jOri<7;++jOri)
		{
			if (iOri == jOri) 
			{
				ori_map[iOri][jOri] = -1;
			}
			else
			{
				ori_map[iOri][jOri] = idx;
				idx++;
			}

		}
	}

	vector <int> tmp_ang, tmp_limb, tmp_ps, tmp_pos, tmp_ori;
	int tmp_val;

	for (int a=a1; a<=a2; ++a)
	{
		ang[a-1].clear();
		limb[a-1].clear();
		ps[a-1].clear();
		pos[a-1].clear();
		ori[a-1].clear();

		for (int s=s1; s<=s2; ++s)
		{
			for (int e=e1; e<=e2; ++e)
			{
				ang_feat.clear();
				limb_feat.clear();
				ps_feat.clear();
				pos_feat.clear();
				ori_feat.clear();

				AngAttr ang_attr;
				LimbAttr limb_attr;
				PsAttr ps_attr;
				PosAttr pos_attr;
				OriAttr ori_attr;

				FILE *frep;
				int nframe;
				vector <int> tmp_feat;

				sprintf(ifn, "..\\..\\..\\Feature\\[ang_feat]_a%02d_s%02d_e%02d_skeleton3D.txt", a, s, e);
				frep = freopen(ifn, "r", stdin);
				if (!frep) continue;
				while (~scanf("%d", &tmp_val))
				{
					tmp_ang.clear();
					tmp_ang.push_back(tmp_val);
					for (int iAng=1;iAng<ang_num;++iAng) 
					{
						scanf("%d", &tmp_val);
						tmp_ang.push_back(tmp_val);
					}
					ang_feat.push_back(tmp_ang);
				}
				nframe = ang_feat.size();
				for (int iAng=0;iAng<ang_num;++iAng)
				{
					tmp_feat.clear();
					int last_num = 1;
					for (int iFrame=1;iFrame<nframe;++iFrame)
					{
						if (ang_feat[iFrame][iAng] == ang_feat[iFrame-1][iAng])
							last_num ++;
						else
						{
							if (last_num >= 3) tmp_feat.push_back(ang_feat[iFrame-1][iAng]);
							last_num = 1;
						}
					}
					if (last_num >= 3) tmp_feat.push_back(ang_feat[nframe-1][iAng]);
					int nframe_elime = tmp_feat.size();
					for (int iFrame=1;iFrame<nframe_elime;++iFrame)
					{
						int idx = ang_map[tmp_feat[iFrame-1]][tmp_feat[iFrame]];
						if (idx == -1) continue;
						ang_attr.attr[iAng][idx] ++;
					}
				}
				ang[a-1].push_back(ang_attr);

				sprintf(ifn, "..\\..\\..\\Feature\\[limbs_feat]_a%02d_s%02d_e%02d_skeleton3D.txt", a, s, e);
				frep = freopen(ifn, "r", stdin);
				if (!frep) continue;
				while (~scanf("%d", &tmp_val))
				{
					tmp_limb.clear();
					tmp_limb.push_back(tmp_val);
					for (int iLimb=1;iLimb<limb_num;++iLimb) 
					{
						scanf("%d", &tmp_val);
						tmp_limb.push_back(tmp_val);
					}
					limb_feat.push_back(tmp_limb);
				}
				nframe = limb_feat.size();
				for (int iLimb=0;iLimb<limb_num;++iLimb)
				{
					tmp_feat.clear();
					int last_num = 1;
					for (int iFrame=1;iFrame<nframe;++iFrame)
					{
						if (limb_feat[iFrame][iLimb] == limb_feat[iFrame-1][iLimb])
							last_num ++;
						else
						{
							if (last_num >= 3) tmp_feat.push_back(limb_feat[iFrame-1][iLimb]);
							last_num = 1;
						}
					}
					if (last_num >= 3) tmp_feat.push_back(limb_feat[nframe-1][iLimb]);
					int nframe_elime = tmp_feat.size();
					for (int iFrame=1;iFrame<nframe_elime;++iFrame)
					{
						int idx = limb_map[tmp_feat[iFrame-1]][tmp_feat[iFrame]];
						if (idx == -1) continue;
						limb_attr.attr[iLimb][idx]++;
					}
				}
				limb[a-1].push_back(limb_attr);

				sprintf(ifn, "..\\..\\..\\Feature\\[part_set_feat]_a%02d_s%02d_e%02d_skeleton3D.txt", a, s, e);
				frep = freopen(ifn, "r", stdin);
				if (!frep) continue;
				while (~scanf("%d", &tmp_val))
				{
					tmp_ps.clear();
					tmp_ps.push_back(tmp_val);
					for (int iPs=1;iPs<ps_num;++iPs) 
					{
						scanf("%d", &tmp_val);
						tmp_ps.push_back(tmp_val);
					}
					ps_feat.push_back(tmp_ps);
				}
				nframe = ps_feat.size();
				for (int iPs=0;iPs<ps_num;++iPs)
				{
					tmp_feat.clear();
					int last_num = 1;
					for (int iFrame=1;iFrame<nframe;++iFrame)
					{
						if (ps_feat[iFrame][iPs] == ps_feat[iFrame-1][iPs])
							last_num ++;
						else
						{
							if (last_num >= 3) tmp_feat.push_back(ps_feat[iFrame-1][iPs]);
							last_num = 1;
						}
					}
					if (last_num >= 3) tmp_feat.push_back(ps_feat[nframe-1][iPs]);
					int nframe_elime = tmp_feat.size();
					for (int iFrame=1;iFrame<nframe_elime;++iFrame)
					{
						int idx = ps_map[tmp_feat[iFrame-1]][tmp_feat[iFrame]];
						if (idx == -1) continue;
						ps_attr.attr[iPs][idx]++;
					}
				}
				ps[a-1].push_back(ps_attr);

				sprintf(ifn, "..\\..\\..\\Feature\\[pos_feat]_a%02d_s%02d_e%02d_skeleton3D.txt", a, s, e);
				frep = freopen(ifn, "r", stdin);
				if (!frep) continue;
				while (~scanf("%d", &tmp_val))
				{
					tmp_pos.clear();
					tmp_pos.push_back(tmp_val);
					for (int iPos=1;iPos<pos_num;++iPos) 
					{
						scanf("%d", &tmp_val);
						tmp_pos.push_back(tmp_val);
					}
					pos_feat.push_back(tmp_pos);
				}
				nframe = pos_feat.size();
				for (int iPos=0;iPos<pos_num;++iPos)
				{
					tmp_feat.clear();
					int last_num = 1;
					for (int iFrame=1;iFrame<nframe;++iFrame)
					{
						if (pos_feat[iFrame][iPos] == pos_feat[iFrame-1][iPos])
							last_num ++;
						else
						{
							if (last_num >= 2) tmp_feat.push_back(pos_feat[iFrame-1][iPos]);
							last_num = 1;
						}
					}
					if (last_num >= 2) tmp_feat.push_back(pos_feat[nframe-1][iPos]);
					int nframe_elime = tmp_feat.size();
					for (int iFrame=1;iFrame<nframe_elime;++iFrame)
					{
						int idx = pos_map[tmp_feat[iFrame-1]][tmp_feat[iFrame]];
						if (idx == -1) continue;
						pos_attr.attr[iPos][idx]++;
					}
				}
				pos[a-1].push_back(pos_attr);

				sprintf(ifn, "..\\..\\..\\Feature\\[ori_feat]_a%02d_s%02d_e%02d_skeleton3D.txt", a, s, e);
				frep = freopen(ifn, "r", stdin);
				if (!frep) continue;
				while (~scanf("%d", &tmp_val))
				{
					tmp_ori.clear();
					tmp_ori.push_back(tmp_val);
					for (int iOri=1;iOri<ori_num;++iOri) 
					{
						scanf("%d", &tmp_val);
						tmp_ori.push_back(tmp_val);
					}
					ori_feat.push_back(tmp_ori);
				}
				nframe = ori_feat.size();
				for (int iOri=0;iOri<ori_num;++iOri)
				{
					tmp_feat.clear();
					int last_num = 1;
					for (int iFrame=1;iFrame<nframe;++iFrame)
					{
						if (ori_feat[iFrame][iOri] == ori_feat[iFrame-1][iOri])
							last_num ++;
						else
						{
							if (last_num >= 2) tmp_feat.push_back(ori_feat[iFrame-1][iOri]);
							last_num = 1;
						}
					}
					if (last_num >= 2) tmp_feat.push_back(ori_feat[nframe-1][iOri]);
					int nframe_elime = tmp_feat.size();
					for (int iFrame=1;iFrame<nframe_elime;++iFrame)
					{
						int idx = ori_map[tmp_feat[iFrame-1]][tmp_feat[iFrame]];
						if (idx == -1) continue;
						ori_attr.attr[iOri][idx]++;
					}
				}
				ori[a-1].push_back(ori_attr);
			}
		}
	}

	//char ofn[1000];
	//sprintf(ofn, "svm_train.txt");
#ifdef OUTPUT
	freopen(ofn1, "w", stdout);
#endif
	for (int a=a1; a<=a2; ++a)
	{
		int nfile = ang[a-1].size();
		for (int iFile=0;iFile<nfile;++iFile)
		{
			printf("%d", a);
			int ind = 1;
			for (int iAng=0;iAng<ang_num;++iAng)
			{
				if (iAng == 1 || iAng == 2 || iAng == 8 || iAng == 9) continue;
				//if (iAng == 0 || iAng == 10 || iAng == 12) continue;
				for (int iAttr=0;iAttr<n_ang_attr;++iAttr)
				{
					printf(" %d:%d", ind++, ang[a-1][iFile].attr[iAng][iAttr]);
				}
			}

			for (int iLimb=0;iLimb<limb_num;++iLimb)
			{
				for (int iAttr=0;iAttr<n_limb_attr;++iAttr)
				{
					printf(" %d:%d", ind++, limb[a-1][iFile].attr[iLimb][iAttr]);
				}
			}

			for (int iPs=0;iPs<ps_num;++iPs)
			{
				for (int iAttr=0;iAttr<n_ps_attr;++iAttr)
				{
					printf(" %d:%d", ind++, ps[a-1][iFile].attr[iPs][iAttr]);
				}
			}

			for (int iPos=0;iPos<pos_num;++iPos)
			{
				for (int iAttr=0;iAttr<n_pos_attr;++iAttr)
				{
					printf(" %d:%d", ind++, pos[a-1][iFile].attr[iPos][iAttr]);
				}
			}

			for (int iOri=0;iOri<ori_num;++iOri)
			{
				for (int iAttr=0;iAttr<n_ori_attr;++iAttr)
				{
					printf(" %d:%d", ind++, ori[a-1][iFile].attr[iOri][iAttr]);
				}
			}

			printf("\n");
		}
	}

	//sprintf(ofn, "analysis_attr.txt");
#ifdef OUTPUT
	freopen(ofn2, "w", stdout);
#endif
	for (int a=a1; a<=a2; ++a)
	{
		int nfile = ang[a-1].size();
		for (int iFile=0;iFile<nfile;++iFile)
		{
			printf("%d", a);
			int ind = 1;
			for (int iAng=0;iAng<ang_num;++iAng)
			{
				if (iAng == 1 || iAng == 2 || iAng == 8 || iAng == 9) continue;
				//if (iAng == 0 || iAng == 10 || iAng == 12) continue;
				for (int iAttr=0;iAttr<n_ang_attr;++iAttr)
				{
					if (ang[a-1][iFile].attr[iAng][iAttr]) printf("\t%d", ind);
					ind++;
				}
			}

			for (int iLimb=0;iLimb<limb_num;++iLimb)
			{
				for (int iAttr=0;iAttr<n_limb_attr;++iAttr)
				{
					if (limb[a-1][iFile].attr[iLimb][iAttr]) printf("\t%d", ind);
					ind++;
				}
			}

			for (int iPs=0;iPs<ps_num;++iPs)
			{
				for (int iAttr=0;iAttr<n_ps_attr;++iAttr)
				{
					if (ps[a-1][iFile].attr[iPs][iAttr]) printf("\t%d", ind);
					ind++;
				}
			}

			for (int iPos=0;iPos<pos_num;++iPos)
			{
				for (int iAttr=0;iAttr<n_pos_attr;++iAttr)
				{
					if (pos[a-1][iFile].attr[iPos][iAttr]) printf("\t%d", ind);
					ind++;
				}
			}

			for (int iOri=0;iOri<ori_num;++iOri)
			{
				for (int iAttr=0;iAttr<n_ori_attr;++iAttr)
				{
					if (ori[a-1][iFile].attr[iOri][iAttr]) printf("\t%d", ind);
					ind++;
				}
			}

			printf("\n");
		}
	}
}

void solve()
{
	int a1 = 1, a2 = 20;
	int s1 = 1, s2 = 10;
	int e1 = 1, e2 = 2;
	generate(1,20,2,10,1,3,"svm_train.txt", "analysis_attr.txt");
	generate(1,20,1,1,1,3,"svm_test.txt", "analysis_attr_test.txt");
}

int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int ln_t;
    scanf("%d", &ln_t);
    for (int ln_cas=1;ln_cas<=ln_t;++ln_cas)
    {
        printf("Case #%d:\n", ln_cas);
        solve();
    }
    return 0;
}