#include <iostream>
#include<fstream>
#include<algorithm>
#include<iomanip>
#define X first
#define Y second

using namespace std;

typedef long double ld;
typedef pair<ld,ld> pii;
const ld eps=0;//1e-20;
pii P[200];
ld v,x;
int n;

bool check(ld k)
{
    ld sum=0,sum1=0;
    for(int i=0;i<n;i++)
        sum+=k*P[i].Y;
    if(sum<v-eps)
        return false;
    sum=0;
    int i=0;
    while(sum<v)
    {
        ld a=min(k*P[i].Y,v-sum);
        sum1+=P[i].X*a;
        sum+=a;
        i++;
    }
    if(sum1>x*v+eps)
        return false;
    sum=sum1=0;
    i=n-1;
    while(sum<v)
    {
        ld a=min(k*P[i].Y,v-sum);
        sum1+=P[i].X*a;
        sum+=a;
        i--;
    }
    if(sum1<x*v-eps)
        return false;
    return true;
}

int main()
{
    ifstream cin("B-large.in");
    ofstream cout("B-large.out");
    int qw;
    cin>>qw;
    for(int q=1;q<=qw;q++)
    {
        cin>>n>>v>>x;
        bool mark1,mark2;
        mark1=mark2=false;
        for(int i=0;i<n;i++)
        {
            cin>>P[i].Y>>P[i].X;
            if(P[i].X<=x+eps)
                mark1=true;
            if(P[i].X>=x-eps)
                mark2=true;
        }
        sort(P,P+n);
        cout<<"case #"<<q<<": ";
        if(!mark1 || !mark2)
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        ld l=0,r=1000000000;
        for(int qwe=0;qwe<200;qwe++)
        {
            ld mid=(l+r)/2.0;
            if(check(mid))
                r=mid;
            else
                l=mid;
        }
        cout<<fixed<<setprecision(7)<<l<<endl;
    }
}
