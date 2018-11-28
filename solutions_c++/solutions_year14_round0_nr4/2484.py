#include<stdio.h>
#include<algorithm>
using namespace std;

double inp1[1001],inp2[1001];

bool cmpmore(double a,double b){return a>b;}
bool cmpless(double a,double b){return a<b;}

void play(int t)
{
    int n,i,j,ans1=0,ans2=0;
    scanf ("%d",&n);
    for (i=0;i<n;++i)scanf ("%lf",&inp1[i]);
    for (i=0;i<n;++i)scanf ("%lf",&inp2[i]);
    sort(inp1,inp1+n,cmpless);
    /*
    sort(inp2,inp2+n,cmpmore);
    for (i=0;i<n && inp1[i]<inp2[i];++i);
    ans1 = n-i;
    */
    sort(inp2,inp2+n,cmpless);
    for (i=0,j=0;j<n;++i,++j)
    {
        while(j<n && inp1[i]>inp2[j])++j;
        if(j == n)break;
        ++ans2;
    }
    ans2 = n-ans2;
    for (i=0,j=0;j<n;++i,++j)
    {
        while(j<n && inp2[i]>inp1[j])++j;
        if(j == n)break;
        ++ans1;
    }
    //ans1 = n-ans1;
    //for (i=0;i<n;++i)printf ("%lf ",inp1[i]);
    //printf ("\n");
    //for (i=0;i<n;++i)printf ("%lf ",inp2[i]);
    printf ("Case #%d: %d %d\n",t,ans1,ans2);
    //return 0;
}

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("txt.txt","w",stdout);
    int n,i;
    scanf ("%d",&n);
    for (i=0;i<n;++i)play(i+1);
    return 0;
}
