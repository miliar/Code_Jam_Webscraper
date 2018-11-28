#include "stdio.h"
#include "stdlib.h"
#include "string.h"
int cmp ( const void *a , const void *b);
int findmember(int **lawn ,int m,int n,int *result);
int DelChar(int *nInt, int nSize);
int judge(int **flag,int **lawn,int n,int m,int *result);
int equjug(int **lawn,int i,int j,int n,int m,int val);
int main()
{
	FILE *input;
	FILE *output;	
	int **lawn;
	int **flag;
	int n,m,k,i,j,T,M;
	int res;
	int *result;
	char *str4;
	str4=(char*)malloc(5*sizeof(char));
	
	input=fopen("E:B-small-attempt1.in","rw");
	output=fopen("E:B-small-attempt1.out","awr");
	if(input!=NULL)
	{
		fscanf(input,"%d",&T);
		fgets(str4,5,input);
		M=T;
		while(T--)
		{
			fscanf(input,"%d",&n);
			fscanf(input,"%d",&m);
			result=(int *)malloc(m*n*sizeof(int));
			lawn=(int **)malloc(n*sizeof(int *));
			flag=(int **)malloc(n*sizeof(int *));
			for (k=0;k<n;k++)
			{
				lawn[k]=(int *)malloc(m*sizeof(int *));
				flag[k]=(int *)malloc(m*sizeof(int *));
			}
			for (i=0;i<n;i++)
			{
				for (j=0;j<m;j++)
				{  flag[i][j]=0;
				fscanf(input,"%d",&lawn[i][j]);
				}
			}
	 
			res=judge(flag,lawn,n,m,result);
			if (res==1)
				fprintf(output,"Case #%d: YES\n",M-T);
			else
				fprintf(output,"Case #%d: NO\n",M-T);
			free(result);
		}
	}
	free(str4);
	return 0;
}


int judge(int **flag,int **lawn,int n,int m,int *result)
{
		int k,i,j,n_new,s,t;	
	
		n_new=findmember(lawn,m,n,result);
		for (k=0;k<n_new-1;k++)
		{
			for (i=0;i<n;i++)
		{
		for (j=0;j<m;j++)
		{
			if(lawn[i][j]!=result[k])
				continue;
			//if ((lawn[i][j]==lawn[0][j]&&lawn[i][j]==lawn[n-1][j])||(lawn[i][j]==lawn[i][0]&&lawn[i][j]==lawn[i][m-1]))
				if(equjug(lawn,i,j,n,m,lawn[i][j])==1)
					flag[i][j]=1;
			else
			{	return 0;}
		}
		for (s=0;s<n;s++)
		{
			for (t=0;t<m;t++)
		{
				if (flag[s][t]==1)
				{
					lawn[i][j]=result[k+1];
					flag[s][t]=0;
				}
		}
		}

		}
		}
			return 1;
	
	/*for (k=0;k<n;k++)
	{	
		free(lawn[k]);
		free(flag[k]);
	}
	free(lawn);
	free(flag);*/
	

}


int findmember(int **lawn ,int m,int n,int *temp)
{
	int i,j,newsize;
	for (i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			temp[i*m+j]=lawn[i][j];
		}
	}	
	qsort(temp,m*n,sizeof(temp[0]),cmp);
	newsize=DelChar(temp,m*n);
	return newsize;
}
int cmp ( const void *a , const void *b)
{
	return *(int *)a - *(int *)b;
}

int DelChar(int *nInt, int nSize)
{
    int i = 1;
    int j = 0;
    int nKey = 0;
    int k = 0;
    for (;i<nSize; i++)
    {
        nKey = nInt[i - 1];
        j = i;
        while (j<nSize)
        {
            if (nKey == nInt[j])
            {
                k = j;
            
                while (k<nSize-1)
                {
                    nInt[k] = nInt[k+1];
                    ++k;
                }
                --nSize;                
            }
            else
                ++j;
        }
    }
    return nSize;
}

int equjug(int **lawn,int i,int j,int n,int m,int val)
{
	int p,cnt,cnt1;
cnt=cnt1=0;
	for (p=0;p<m;p++)
	{
		if (val==lawn[i][p])
			cnt+=1;
	}
	for (p=0;p<n;p++)
	{
		if (val==lawn[p][j])
			cnt1+=1;
	}
	if (cnt==m||cnt1==n)
		return 1;
	else
		return 0;
}