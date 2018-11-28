#if 1
#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;

typedef unsigned long long ull;
int main()
{

FILE* fin = fopen("run5.in","r");
FILE* fout = fopen("submit.txt","w+");

	int N=0;//number of test cases
	fscanf(fin,"%d",&N);
	int k = 0;
	 int n = 0;
	int* index = new int[10000];
	
	char str[102];
	

	for(int nc = 1 ; nc <= N;nc++)
	{
		int k = 0;
		int n =0;
		memset(str,0,102);
		for(int r= 0; r < 10000; r++)
		{
			index[r]=0;
		}
		fscanf(fin,"%s",str);
		fscanf(fin,"%d",&n);

		for(int i=0;i<strlen(str);i++)
		{
			if(i <= strlen(str)-n)
			{
				if((str[i]!='a')&&(str[i]!='e')&&(str[i]!='i')&&(str[i]!='o')&&(str[i]!='u')&&(str[i+n-1]!='a')&&str[i+n-1]!='e'&&str[i+n-1]!='i'&&str[i+n-1]!='o'&&str[i+n-1]!='u')
				{
					bool bcons = true;
					for(int j = 0 ; j < n;j++)
					{
						if(str[j+i]!='a'&&str[j+i]!='e'&&str[j+i]!='i'&&str[j+i]!='o'&&str[j+i]!='u')
						{

						}
						else
						{
							bcons=false;
							break;
						}
					}
					if(bcons)
					{
						index[k]=i;
						k++;
					}
				}
			}
			else
			{
				break;
			}
		}

	
	cout<<"k  = "<<k<<endl;
	int sub=0;
	int len = strlen(str);
	for(int l = 0; l <k;l++)
	{
		int w;
		if(l>0)
			w=index[l-1]+1;
		else
			w=0;
		for( ; w <=index[l];w++)
		{
			sub=sub+len-(index[l]+n)+1;
		}

	}
	cout<<"number of substrings = "<<sub;
	fprintf(fout,"Case #%d: %d\n",nc,sub);
	}
	fclose(fin);
	fclose(fout);

	return 0;
}

#endif