#include <bits/stdc++.h>

using namespace std;

int n, p[30][2];



void Merge(int a[][2],int i,int m,int j)
{
    long long int temp[j-i+1][2];
    int iptr=i,jptr=m+1,mptr=0;
    while(iptr<=m && jptr<=j)
    {
        if(a[iptr][0]<a[jptr][0])
        {
            temp[mptr][0]=a[iptr][0];
            temp[mptr][1]=a[iptr][1];
            iptr++;
            mptr++;
        }
        else
        {
            temp[mptr][0]=a[jptr][0];
            temp[mptr][1]=a[jptr][1];
            jptr++;
            mptr++;
        }
    }
    while(iptr<=m)
    {            
    	temp[mptr][0]=a[iptr][0];
            temp[mptr][1]=a[iptr][1];
            iptr++;
            mptr++;
    }
    while(jptr<=j)
    {
        temp[mptr][0]=a[jptr][0];
            temp[mptr][1]=a[jptr][1];
            jptr++;
            mptr++;
    }
    mptr=0;
    for(iptr=i;iptr<=j;iptr++)
    {
        a[iptr][0]=temp[mptr][0];
        a[iptr][1]=temp[mptr][1];
        
        mptr++;
    }
}
void mergeSort(int a[][2],int i,int j)
{
    if(i<j)
    {
        int m=(i+j)/2;
        mergeSort(a,i,m);
        mergeSort(a,m+1,j);
        Merge(a,i,m,j);
    }
}
void solve(int ind)
{
	if(ind<0)	return;
	if(ind>=1){
		while(p[ind][0]>p[ind-1][0])
		{
			for(int i=ind;i<n;i++)
			{
				{
					printf("%c ", p[i][1]+'A');
				}
			}
			p[ind][0]--;
		}
		solve(ind-1);
	}
	else{
		while(p[ind][0]>0)
		{
			for(int i=ind+2;i<n;i++)
			{
				printf("%c ", p[i][1]+'A');
			}
			printf("%c%c ", p[0][1]+'A', p[1][1]+'A');
			p[0][0]--;
		}
	}
	return;
}
int main()
{
	int t, sum, index=0;;
	scanf("%d",&t);
	while(t--)
	{
		index++;
		scanf("%d",&n);
		sum=0;
		for(int i=0;i<n;i++)
		{
			scanf("%d",&p[i][0]);
			p[i][1] = i;
		}
		printf("Case #%d: ", index);
		
		mergeSort(p, 0, n-1);		
		solve(n-1);
		printf("\n");
	}
	return 0;
}