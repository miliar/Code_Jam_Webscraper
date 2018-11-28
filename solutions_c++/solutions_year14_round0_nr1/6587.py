#include "cstdio"
#include <set>
#include <numeric>
#include <iostream>
using namespace std;

int main()
{
	int casenum;
	int answer1,answer2;
	int first_arr[5][5];
	int second_arr[5][5];
	int i,j;
	int k;
	int element_num;
	int result;

	FILE *fp=fopen("A-small-attempt7.in","r");
	FILE *fpout=fopen("out.txt","w");

	fscanf(fp,"%d",&casenum);
	for(k=0;k<casenum;k++)
	{
		fscanf(fp,"%d",&answer1);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fscanf(fp,"%d",&first_arr[i][j]);
		fscanf(fp,"%d",&answer2);
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fscanf(fp,"%d",&second_arr[i][j]);
		set<int> int_set;
		pair<set<int>::const_iterator,bool> p;
		for(i=0;i<4;i++)
		{
			p=int_set.insert(first_arr[answer1-1][i]);
			
		}
		for(i=0;i<4;i++)
		{
			p=int_set.insert(second_arr[answer2-1][i]);
			if(!p.second)
				result=*(p.first);
		}
		element_num=int_set.size();
		if (element_num==7)
			fprintf(fpout,"Case #%d: %d\n",k+1,result);
		else if(element_num<7)
			fprintf(fpout,"Case #%d: Bad magician!\n",k+1);
		else 
			fprintf(fpout,"Case #%d: Volunteer cheated!\n",k+1);
		int_set.clear();
	}
	return 0;
}