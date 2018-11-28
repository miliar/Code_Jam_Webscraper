/*
Prikshit
C++
*/
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<math.h>
#include<stack>
#define f0(i,n) for(int i=0;i<=n;i++)
#define fn(i,n) for(int i=n;i>0;i--)
#define f1(i,a,n) for(int i=a;i<=n;i++)
#define f2(i,a,n) for(int i=a;i>=n;i--)

using namespace std;

int war(double a[],double b[],int n)
{
    int c=0,i,j,k;
    vector<double> b1;
    for(i=0;i<n;i++)
    {
        b1.push_back(b[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<b1.size();j++)
        {
            if(a[i]>b1[j])
            {
                b1.erase(b1.begin()+j);
                c++;
                break;
            }
        }
    }
    return c;
}
int war_original(double a[],double b[],int n)
{
    int c=0,i,j,k;
    vector<double> b1;
    for(i=0;i<n;i++)
    {
        b1.push_back(b[i]);
    }
    for(i=n-1;i>=0;i--)
    {
        k=0;
        for(j=0;j<b1.size();j++)
        {
            if(a[i]<b1[j])
            {
                k=1;
                b1.erase(b1.begin()+j);
                break;
            }
        }
        if(k==0)
        {
            c++;
        }
    }
    return c;
}
int main()
{
    ofstream fout ("frac1.out");
    ifstream fin ("frac1.in");
    int t,T,n,i,j,k,fg,r,c,m,pi,mc,bc,k1,k2,k3;
    double a[1000],b[1000];
    fin>>T;
    for(t=1;t<=T;t++)
    {
        fin>>n;
        for(i=0;i<n;i++)
            fin>>a[i];
        for(i=0;i<n;i++)
            fin>>b[i];
        sort(a,a+n);sort(b,b+n);
    fout<<"Case #"<<t<<": "<<war(a,b,n)<<" "<<war_original(a,b,n)<<endl;
    }
    return 0;
}
