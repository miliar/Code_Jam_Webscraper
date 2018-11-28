#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
using namespace std;
double A[1005],B[1005];

int main()
{
    int T=0;
    int M=0;
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        int i,j;
        for(i=0;i<n;i++)
            scanf("%lf",&A[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&B[i]);
        sort(A,A+n);
        sort(B,B+n);
        int Ans1=0,Ans2=n;
        for(i=n-1,j=n-1;i>=0;i--)
        {
            for(;j>=0&&B[j]>A[i];j--);
            if(j!=-1){Ans1++;j--;}
            if(j<0)break;
        }
        for(i=n-1,j=n-1;i>=0;i--)
        {
            for(;j>=0&&A[j]>B[i];j--);
            if(j!=-1){Ans2--;j--;}
            if(j<0)break;

        }
        printf("Case #%d: %d %d\n",++M,Ans1,Ans2);
    }
}
