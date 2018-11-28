#include<stdio.h>
using namespace std;
#include<algorithm>
#include<vector>
int a1;
int a2;
vector<int>v;
int ash[8];
int main()
{
	FILE* fin = fopen("A-small-attempt0.in","r");
	FILE* fout = fopen("output.txt","w+");
	int n=0;
	fscanf(fin,"%d",&n);
	int nNum=0;
	for(int i = 1; i <= n; i++)
	{

		fscanf(fin,"%d",&a1);
		for(int j = 1; j <= 16;j++)
		{
			fscanf(fin,"%d",&nNum);
			v.push_back(nNum);
		}
		for(int k = 0; k <=3; k++)
		{
			ash[k]=v[(a1-1)*4+k];
		}
		//clear
		v.clear();
		//second chance
		fscanf(fin,"%d",&a2);
		for(int j = 1; j <= 16;j++)
		{
			fscanf(fin,"%d",&nNum);
			v.push_back(nNum);
		}
		for(int k = 4; k <=7; k++)
		{
			ash[k]=v[(a2-1)*4 +k-4];
		}
		//clear
		v.clear();
		//count matches in 1 & 2
		int match = 0;
		int nCard=0;
		for(int c= 0; c<=3; c++)
		{

			for(int d= 4; d<=7; d++)
			{
				if(ash[c] == ash[d])
				{
					nCard = ash[c];
					match++;
					break;
				}
			}
		}
		for(int e= 0; e<=7; e++)
			printf("num  -- %d \n",ash[e]);

		printf("matches -- %d \n",match);
		switch(match)
		{
			case 1:
				{
					fprintf(fout,"Case #%d: %d\n",i,nCard);
				}
				break;
			case 0:
				{
					fprintf(fout,"Case #%d: Volunteer cheated!\n",i);
				}
				break;
			default:
				{
					fprintf(fout,"Case #%d: Bad magician!\n",i);
				}
				break;
		}
	}
	fclose(fin);
	fclose(fout);
}
