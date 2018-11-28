#include <fstream>
using namespace std;
short t,n,m,a[101][101],q,e,j,k,mi,poz1,poz2,i;
ifstream f("lan.in");
ofstream g("lan.out");
void fil(short mi,short poz1, short poz2)
{
    q=0;
    e=0;
    j=poz2+1;;
    while((j<m)&&(e!=1))
    {
        if ((a[poz1][j]!=mi)&&(a[poz1][j]!=0)) e=1;
        j++;
    }
    if (e==0)
    {
        j=poz2-1;
        while((j>=0)&&(e!=1))
        {
            if ((a[poz1][j]!=mi)&&(a[poz1][j]!=0)) e=1;
            j--;
        }
        if (e==0){
            q=1;
         for(j=0;j<m;j++)
        {
            a[poz1][j]=0;
        }
        }
    }
    e=0;
    j=poz1+1;;
    while((j<n)&&(e!=1))
    {
        if ((a[j][poz2]!=mi)&&(a[j][poz2]!=0)) e=1;
        j++;
    }
    if (e==0)
    {
        j=poz1-1;
        while((j>=0)&&(e!=1))
        {
            if ((a[j][poz1]!=mi)&&(a[j][poz2]!=0)) e=1;
            j--;
        }
        if (e==0){
            q=1;
            for(j=0;j<n;j++)
        {
            a[j][poz2]=0;
        }
        }
    }
}
void back()
{
    f>>n>>m;
    mi=100;
    for(j=0;j<n;j++)
    for(k=0;k<m;k++)
    {
        f>>a[j][k];
        if(a[j][k]<mi)
        {
            mi=a[j][k];
            poz1=j;
            poz2=k;
        }
    }
    fil(mi,poz1,poz2);
    while(q==1)
    {
        mi=100;
        e=0;
    for(j=0;j<n&&e==0;j++)
    for(k=0;k<m&&e==0;k++)
    {
        if((a[j][k]!=0)&&(a[j][k]<mi))
        {
            mi=a[j][k];
            poz1=j;
            poz2=k;
            if (mi==1) e=1;
        }
    }
    if (mi!=100) fil(mi,poz1,poz2);
    else q=0;
    }
    }

int main()
{
    f>>t;
    for(i=1;i<=t;i++)
    {
        back();
        if (mi==100) g<<"Case #"<<i<<": YES"<<'\n';
        else g<<"Case #"<<i<<": NO"<<'\n';
    }
    f.close();
    g.close();
    return 0;
}
