#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<cstdlib>
#include<string.h>
#include<limits.h>
#define lli long long int
#define minm(a,b) (a<b)?a:b
using namespace std;

int m[105],n;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int check(int csize, int k, int csteps)
{
    //printf("reached %d with csize=%d cteps=%d\n",k,csize,csteps);
    if(k==n){
        //printf("reach last return %d\n",csteps);
        return csteps;
    }

    if(csize>m[k]){
        //printf("reach %d csize > m[k]\n",k);
        return check(csize+m[k],k+1,csteps);
    }

    int nsize = 2*csize-1;

    if(nsize>csize)
    {
        int nsteps = check(nsize,k,csteps+1);
        //printf("reach %d return %d\n",k,minm((n-k),nsteps));
        return minm(csteps+(n-k),nsteps);
    }
    else
        return csteps+(n-k);

}

int main(void)
{
	freopen("A-Large.in", "r", stdin);
	freopen("A-Large-out.txt", "w", stdout);

	int T,msize,i,cno=0;
	cin>>T;
	while(T--)
	{
	    //memset(m,500,sizeof(m));
        cno++;

	    cin>>msize;
	    cin>>n;

	    for(i=0;i<n;i++)
            cin>>m[i];

        qsort(m,n,sizeof(int),compare);

        cout<<"Case #"<<cno<<": "<<check(msize,0,0)<<endl;
	}
	return 0;
}

