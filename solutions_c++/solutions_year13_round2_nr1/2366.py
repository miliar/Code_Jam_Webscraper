#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#define MIN(a,b) (a>b?b:a)
#define SIZE 12

using namespace std;
int n,mote;

int myfunc(int num,int sum,vector<int> &arr)
{
    if(num>=n)
    return(0);

    if(sum>arr[num])
    {
        return(myfunc(num+1,sum+arr[num],arr));
    }
    else
    {
        return(MIN(1+myfunc(num+1,sum,arr),1+myfunc(num,sum+(sum-1),arr)));
    }
}

int main()
{
    FILE *fin,*fout;
    fin=fopen("A-small-attempt2.in","r");
    fout=fopen("output000.txt","w");
    int t,i,x,ret;

    fscanf(fin,"%d",&t);
    for(x=1;x<=t;x++)
    {
        fscanf(fin,"%d%d",&mote,&n);
        vector<int> arr(n);
        for(i=0;i<n;i++)
        fscanf(fin,"%d",&arr[i]);

        if(mote==1)
        {
            ret=n;
            fprintf(fout,"Case #%d: %d\n",x,ret);
            continue;
        }

        sort(arr.begin(),arr.end());

        ret=myfunc(0,mote,arr);

        fprintf(fout,"Case #%d: %d\n",x,ret);
    }

    return(0);
}
