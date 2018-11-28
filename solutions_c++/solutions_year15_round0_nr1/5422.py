#include <iostream>
#include <cstdio>
#include <cstdlib>
//#include <string> 
//#include <vector>
//#include <algorithm>
using namespace std; 

int T; //test case number
int Smax;
char arr[1005];
int iTotalClap = 0;
int iNeedInvite = 0;


void run(int cur)
{
	int iNeedInvite_delta;
	if(arr[cur] != 0)
	{
		if(cur <= iTotalClap)
		{
			iTotalClap += arr[cur];
		}
		else
		{
			iNeedInvite_delta = (cur - iTotalClap);
			iNeedInvite = iNeedInvite + iNeedInvite_delta;
			iTotalClap = iTotalClap + (iNeedInvite_delta + arr[cur]);
		}
	}

	return;
}

int main()
{	
	int iCase = 0;
	int i;
	char input;
	FILE *fp_r, *fp_w; 
	if((fp_r = fopen("A-large.in", "r")) == NULL)
	{
		exit(-1);
	} 
	if((fp_w = fopen("A-large.out", "w")) == NULL)
	{
		exit(-1);
	} 
	fscanf(fp_r, "%d", &T); //test case number
	printf("T = %d\n", T);

	while(T--)
	{
		Smax = 0;
		iNeedInvite = 0;
		iTotalClap = 0;
		memset(arr, 0, sizeof(arr));

		fscanf(fp_r, "%d", &Smax);
		//printf("Smax = %d\n", Smax);
		//arr = (char*)malloc((Smax+2)*sizeof(int));
		
		fscanf(fp_r, "%s", arr);
		for(i=0;i<Smax+1;i++)
		{
			arr[i] -= 48;
			//printf("%d\n", arr[i]);
		}

		//start to solve problem
		if(arr[0] == 0)
		{
			iNeedInvite++;
			iTotalClap++;
		}
		else
		{
			iTotalClap += arr[0];
		}

		for(i=1;i<Smax+1;i++)
		{
			run(i);
		}

		/////output/////
		fprintf(fp_w, "Case #%d: %d\n", ++iCase, iNeedInvite);
	}

	fclose(fp_r);
	fclose(fp_w);
	return 0;
}

