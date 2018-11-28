#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
#define FOR(i,l,n) for(int i=l;i<n;i++)
#define INT(c) int c;scanf("%d",&c);
#define LL(c) long long c;scanf("%ll",&c);
#define ULL(c) unsigned long long c;scanf("%llu",&c);
#define MOD 1000000007
#define Ull unsigned long long
#define Ll lnong long
#define chk(x) x%=MOD;
bool comp(double i,double j)
{
    return (i>j);
}
int main()
{
    INT(t)
    FOR(i,0,t)
    {
        INT(n)
        double a[n],b[n];
        FOR(j,0,n)
            scanf("%lf",&a[j]);
        FOR(j,0,n)
            scanf("%lf",&b[j]);
        vector<double> A(a,a+n);
        sort(A.begin(),A.end());
        vector<double> B(b,b+n);
        sort(B.begin(),B.end());
        vector<double> AA(a,a+n);
        sort(AA.begin(),AA.end(),comp);
        vector<double> BB(b,b+n);
        sort(BB.begin(),BB.end(),comp);
        int used[n];
        int b_points=0,a_points=0;
        FOR(j,0,n)
            used[j]=0;
        FOR(j,0,n)
        {
            int found=0;
            FOR(k,0,n)
                if(used[k]==0 && A[j]<B[k])
                {
                    //cout<<"-"<<A[j]<<" "<<B[j]<<endl;
                    b_points++;
                    used[k]=1;
                    found=1;
                    break;
                }
            if(!found)
            FOR(k,0,n)
                if(used[k]==0)
                {
                    //cout<<"+"<<A[j]<<" "<<B[j]<<endl;
                    a_points++;
                    used[k]=1;
                    break;
                }
        }
        int normal_points=a_points;
        a_points=0,b_points=0;
        int last_small=0;
        FOR(j,0,n)
            used[j]=0;
        FOR(j,0,n)
        {
            int found=0;
            FOR(k,0,n)
                if(used[k]==0 && A[j]<BB[k] &&A[j]<B[last_small])
                {
                    //cout<<"-"<<A[j]<<" "<<BB[k]<<endl;
                    b_points++;
                    used[k]=1;
                    found=1;
                    if(used[n-1-last_small])
                        last_small++;
                    break;
                }
            if(!found)
            FOR(k,0,n)
                if(used[k]==0 && A[j]>BB[k])
                {
                    //cout<<"+"<<A[j]<<" "<<BB[k]<<endl;
                    a_points++;
                    used[k]=1;
                    break;
                }
        }
        //cout<<a_points<<" "<<b_points<<endl;
        int cheat=a_points;
        cout<<"Case #"<<i+1<<": "<<cheat<<" "<<normal_points<<endl;
    }
    return 0;
}



