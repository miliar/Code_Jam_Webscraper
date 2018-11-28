#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;
int t,r1,r2,n,r,p;
vector<double> a,b;
bool u[2000],g;
double d;
int cmp(vector<double> x, vector<double> y)
{
    r=0;
    memset(u,0,sizeof(u));
    for(int i=0;i<n;i++)
    {
        g=false;
        for(int j=0;j<n;j++)
            if(!u[j]&&y[j]>x[i])
            {
                g=true;
                p=j;
                break;
            }
        if(g)
        {
            r++;
            u[p]=true;
        }
        else
            for(int j=0;j<n;j++)
                if(!u[j])
                {
                    u[j]=true;
                    break;
                }
    }
    return r;
}
int main()
{
    freopen("dlarge.in","r",stdin);
    freopen("dlarge.out","w",stdout);
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        a.clear();
        b.clear();
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>d;
            a.push_back(d);
        }
        for(int i=0;i<n;i++)
        {
            cin>>d;
            b.push_back(d);
        }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        r2=n-cmp(a,b);
        r1=cmp(b,a);
        printf("Case #%d: %d %d\n",test,r1,r2);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
