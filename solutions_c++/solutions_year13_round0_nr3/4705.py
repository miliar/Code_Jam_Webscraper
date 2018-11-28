#include <iostream>
#include <cstdio>
using namespace std;

long long a[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
FILE *fin,*fout;
int main()
{
    fin =fopen("test_in.txt","r");
    fout = fopen("test_out.txt","w+");
    long long i,j,k,t,CASE,l,r,ans,num=39;
    fscanf(fin,"%lld",&CASE);
    for (t=1;t<=CASE;t++)
    {
        fscanf(fin,"%lld%lld",&l,&r);
        ans =0;
        for (i=0;i<num;i++)
        {
            if (a[i]>=l && a[i]<=r)
                ans++;

        }
        fprintf(fout,"Case #%lld: %lld\n",t,ans);
    }

    return 0;
}

