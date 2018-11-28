#include<iostream>
#include<fstream>
using namespace std;
ifstream fin;
ofstream fout;
void deal(int);
struct square
{
    int h,x,y;
};
int g[101][101];
square q[10001];
bool h[101][101];
void sort(int l,int r);
int main()
{
    fin.open("gcj2013-Q-B.in");
    fout.open("gcj2013-Q-B.out");
    int t;
    fin>>t;
    for (int i=0;i<t;i++)
        deal(i);
}

void deal(int p)
{
    int m,n;
    fin>>n>>m;
    int l=0;
    bool flag=true;
    memset(h,0,sizeof(h));
    for (int i=0;i<n;i++)
        for (int j=0;j<m;j++)
        {
            fin>>g[i][j];
            q[l].h=g[i][j];
            q[l].x=i;
            q[l].y=j;
            l++;
        }
    sort(0,l-1);
    for (int i=0;i<l;i++)
    {
        if (h[q[i].x][q[i].y]) continue;
        h[q[i].x][q[i].y]=true;
        bool flag2=true;
        for (int j=0;j<m;j++)
            if (g[q[i].x][j]>g[q[i].x][q[i].y])
            {
                flag2=false;
                break;
            }
        if (flag2)
        {
            for (int j=0;j<m;j++)
                h[q[i].x][j]=true;
        }
        bool flag3=true;
        for (int j=0;j<n;j++)
            if (g[j][q[i].y]>g[q[i].x][q[i].y])
            {
                flag3=false;
                break;
            }
        if (flag3)
        {
            for (int j=0;j<n;j++)
                h[j][q[i].y]=true;
        }
        flag=flag2 || flag3;
        if (!flag) break;
    }
    fout<<"Case #"<<p+1<<": ";
    if (flag) fout<<"YES"<<endl;
    else fout<<"NO"<<endl;
/*    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
            fout<<g[i][j]<<' ';
        fout<<endl;
    }*/
}

void sort(int l,int r)
{
    int x=q[(l+r)/2].h;
    int i=l,j=r;
    do
    {
        while(q[i].h<x)
            i++;
        while(x<q[j].h)
            j--;
        if (i<=j)
        {
            square tmp=q[i];
            q[i]=q[j];
            q[j]=tmp;
            i++;
            j--;
        }
    }
    while (i<=j);
    if (j>l) sort(l,j);
    if (i<r) sort(i,r);
}

