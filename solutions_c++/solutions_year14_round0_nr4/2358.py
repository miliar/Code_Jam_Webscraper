#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	int n,i,m,j;
	FILE *fs = fopen("input.in","rt");
	FILE *fp = fopen("output.out","wt");
	fscanf(fs,"%d",&n);

	for(i=0;i<n;i++)
	{
		double Naomi[2000]={0,};
		double Ken[2000]={0,};
		fscanf(fs,"%d",&m);

		for(j=0;j<m;j++)
			fscanf(fs,"%lf",&Naomi[j]);
		for(j=0;j<m;j++)
			fscanf(fs,"%lf",&Ken[j]);

		std::sort(Naomi,Naomi+m);
		std::sort(Ken,Ken+m);

		int t=0,war_score=0,de_score=0;
		for(j=0;j<m;j++)
		{
			if(Naomi[j]>Ken[t])
			{
				war_score++;
				t++;
				if(t==m){
					war_score+=(m-1)-j;
					break;
				}
			}
		}
		t=0;
		for(j=0;j<m;j++)
		{
			while(Ken[t]<Naomi[j]&&t<m) t++;
			if(t>m-1)
			{
				de_score=m-j;
				break;
			}
			t++;
		}

		fprintf(fp,"Case #%d: %d %d\n",i+1,war_score,de_score);
	}
	fclose(fs);
	fclose(fp);
	return 0;
}