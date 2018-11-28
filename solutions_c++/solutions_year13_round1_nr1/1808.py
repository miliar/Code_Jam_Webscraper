//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
//Other Includes
#include<iostream>
#include<algorithm>
#include<iomanip>
#include<utility>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
//some common functionn
#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define FOR(i,a,b)              for(int i=a;i<b;i++)
#define FORs(i,a,b)             for(int i=a;i>=b;i--)
#define fill(a,v)               memset(a,v,sizeof a)
#define abS(x)                  ((x)<0?-(x):(x))
#define mP                      make_pair
#define pB                      push_back
#define error(x)                cout << #x << " : " << (x) << endl
#define ALL(a)                  (a).begin(),(a).end()
#define SZ(a)                   ((int) a.size())
#define SORT(a)                  sort(ALL(a))

using namespace std;

typedef long long LL;



void chekarre(int * arr,int n)
{
    cout<<"[";
    for(int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<"]"<<endl;
}

bool comp(int i,int j) { return (i>j); }


int main()
{
    freopen("input1.txt","r",stdin);
    freopen("output.txt","w",stdout);

    long long n,x=0;
    long long r,t,res=0;
    long double r1,r2,r3;
    long double r4;

    cin >>n;
    while(x!=n){
        cin >> r>>t;
        r1=(2*r)-1;
        r2=8*t;
        r3=pow(r1,2)+r2;
        r4=sqrt(r3);
        res=(r4-r1)/4;
        //cout<<r1<<"\n"<<r2<<"\n"<<r3<<"\n"<<r4<<endl;
        cout<<"Case #"<<x+1<<": "<<res<<endl;
        x++;
    }
    return 0;
}
