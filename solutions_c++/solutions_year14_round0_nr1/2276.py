//Author: Siddharth Saluja
//Quote: "DIE FOR YOUR AIM"
#include <bits/stdc++.h>

using namespace std;


#define mod 1000000007
//#define DEBUG
#define inf 2147483647
#define ninf -2147483648
#define FOR(i,a,b) for(i=a;i<b;i++)
#define s(a) scanf("%d",&a)
#define lls(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define p(a) printf("%d",a)
#define llp(a) printf("%lld",a)
#define sp(a) printf("%s",a)
#define cp(a) printf("%c",a)
#define nline printf("\n")
#define space printf(" ")
#define fs(a) fscanf(fp,"%d",&a)
#define flls(a) fscanf(fp,"%lld",&a)
#define fss(a) fscanf(fp,"%s",a)
#define fp(a) fprintf(fo,"%d",a)
#define fllp(a) fprintf(fo,"%lld",a)
#define fsp(a) fprintf(fo,"%s",a)
#define fcp(a) fprintf(fo,"%c",a)
#define fnline fprintf(fo,"\n")
#define fspace fprintf(fo," ")
#define ll long long


int main()
{
#ifdef DEBUG
    cout<<"Debugging\n";
#endif
//ios::sync_with_stdio(false);
FILE *fp,*fo;
fp=fopen("input.txt","r");
fo=fopen("output.txt","w");

int t,k=0,i,j;
fs(t);
while(t--)
{
    k++;
    fprintf(fo,"Case #%d: ",k);
    int r1,r2,a[10][10]={0},b[10][10]={0},m[30]={0},flag=0,ans;
    fs(r1);
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            fs(a[i][j]);
        }
    }
    fs(r2);
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            fs(b[i][j]);
        }
    }
    //cout<<r1<<" "<<r2<<endl;
    for(i=1;i<=4;i++)
    {
        m[a[r1][i]]=1;
    }
    for(i=1;i<=4;i++)
    {
        if(m[b[r2][i]]==1)
            flag++;
    }
    if(flag==1)
    {
        for(i=1;i<=4;i++)
        {
            if(m[b[r2][i]]==1)
                ans=b[r2][i];
        }
        fprintf(fo,"%d\n",ans);
    }
    else if(flag==0)
    {
        fprintf(fo,"Volunteer cheated!\n");
    }
    else if(flag>1)
    {
        fprintf(fo,"Bad magician!\n");
    }
}


return 0;
}
