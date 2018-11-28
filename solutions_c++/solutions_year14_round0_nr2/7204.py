#include<iostream>
#include<cstdio>
#include<climits>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<cmath>
#include<queue>
#include<utility>
#include<fstream>
#include<iomanip>
using namespace std;

//#define inp(a) scanf("%d",&a)
#define out(a) printf("%d\n",a)
#define inpll(a) scanf("%lld",&a)
#define outll(a) printf("%lld\n",a)

#define swap(a,b) {a=a+b;a=a-b;b=a-b;}
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>

#define ll long long int
#define mod 1000000007

#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define rep(i,a,b) for(i=a;i<b;i++)


ifstream myfile("input.txt");
ofstream outs("outputcookies.txt");

int main()
{
    double c,f,x,time,rate,data[3];
    int t,count=0,i;
    myfile >> t;
    while(t--)
    {
        count++;
        myfile >> c >> f >> x;
        rate=2.0;
        time=0.0;
        while(((c/rate)+(x/(rate+f)))<(x/rate))
        {
            time+=(c/rate);
            rate+=f;
        }
        time+=(x/rate);
        outs<<"Case #"<<count<<": " << std::fixed << std::setprecision(7) << time << '\n';
    }
    return 0;
}
