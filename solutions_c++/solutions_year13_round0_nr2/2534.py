#include<stdio.h>
#include<vector>

using namespace std;

void print(vector<vector<int> > garden,int n, int m)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        printf("%d ",garden[i][j]);
        printf("\n");
    }
}

int process(vector<vector<int> > garden,int n, int m)
{
    int min=101,mr,mc,i,j;
    //print(garden,n,m);
    if(m<=1 || n<=1) return 1;
    for(i=0;i<n;i++)
    for(j=0;j<m;j++)
    if(garden[i][j]<min) { min=garden[i][j]; mr=i; mc=j; }
    //printf("min row %d min col %d\n",mr,mc);
    for(i=0;i<m;i++)
    {
        if(garden[mr][i]!=min) break;
    }
    if(i==m)
    {
        garden.erase(garden.begin()+mr);
        //print(garden,n-1,m);
        return process(garden,n-1,m);
    }
    
    for(i=0;i<n;i++)
    {
        if(garden[i][mc]!=min) break;
    }
    if(i==n)
    {
        for(j=0;j<n;j++)
        garden[j].erase(garden[j].begin()+mc);
        //print(garden,n,m-1);
        return process(garden,n,m-1);
    }
    
    return 0;
}

int main()
{
    int t,k,h,n,m;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d %d",&n,&m);
        vector< vector<int> > garden(n,vector<int> (m));
        for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
        {
            scanf("%d",&h);
            garden[i][j]=h;
        }
        if(process(garden,n,m)) printf("Case #%d: YES\n",k);
        else printf("Case #%d: NO\n",k);
        garden.clear();
    }
    return 0;
}
