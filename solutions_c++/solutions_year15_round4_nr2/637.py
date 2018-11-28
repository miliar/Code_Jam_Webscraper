#include<fstream>
using namespace std;
#include<utility>
FILE*fin=fopen("input.txt","r");
FILE*fout=fopen("output.txt","w");
int n;
double out;
pair<double,double> p[110];
double mn2(double a,double b)
{
	if(a>b)return b;
	else return a;
}
double mx2(double a,double b)
{
	if(a>b)return a;
	else return b;
}
int main()
{
	int i,j,x;
	double y,z;
	fscanf(fin,"%d",&n);
	for(i=1;i<=n;++i)
	{
		fscanf(fin,"%d%lf%lf",&x,&y,&z);
		for(j=1;j<=x;++j)fscanf(fin,"%lf%lf",&p[j].first,&p[j].second);
		switch(x)
		{
		case 1:
			if(p[1].second!=z)fprintf(fout,"Case #%d: IMPOSSIBLE\n",i);
			else fprintf(fout,"Case #%d: %.9lf\n",i,y/p[1].first);
			break;
		case 2:
			if(p[1].second>p[2].second)swap(p[1],p[2]);
			if(z<p[1].second||z>p[2].second)fprintf(fout,"Case #%d: IMPOSSIBLE\n",i);
			else if(p[1].second==p[2].second)fprintf(fout,"Case #%d: %.9lf\n",i,y/(p[1].first+p[2].first));
			else if(z==p[1].second)fprintf(fout,"Case #%d: %.9lf\n",i,y/p[1].first);
			else if(z==p[2].second)fprintf(fout,"Case #%d: %.9lf\n",i,y/p[2].first);
			else fprintf(fout,"Case #%d: %.9lf\n",i,mx2(y*(z-p[2].second)/(p[1].second-p[2].second)/p[1].first,y*(z-p[1].second)/(p[2].second-p[1].second)/p[2].first));
			break;
		default:
			fprintf(fout,"Case #%d: SKIP\n",i);
			break;
		}
	}
	return 0;
}