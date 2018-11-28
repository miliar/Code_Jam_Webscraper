#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define pb push_back
#define sz size()
#define ln length()
#define fore(i,a,b) for(int i=a;i<b;i++)
#define fores(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define md 1000000

int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
		printf("Case #%d: ",z+1);
		int n;
		cin>>n;
		double x,v;
		cin>>v>>x;
		if(n==1)
        {
            double r,c;
            cin>>r>>c;
            if(x!=c)
            {
                cout<<"IMPOSSIBLE"<<endl;
                continue;
            }
            cout<<setprecision(20)<<v/r<<endl;
            continue;
        }
        else if(n==2)
        {
            double r1,c1,r2,c2;
            cin>>r1>>c1>>r2>>c2;
            if(c1==x && c2==x)
            {
                cout<<setprecision(20)<<v/(r1+r2)<<endl;
                continue;
            }
            else if(c1==x)
            {
                cout<<setprecision(20)<<v/r1<<endl;
                continue;
            }
            else if(c2==x)
            {
                cout<<setprecision(20)<<v/r2<<endl;
                continue;
            }
            else if(c1<x && c2<x)
            {
                cout<<"IMPOSSIBLE"<<endl;
                continue;
            }
            else if(c1>x && c2>x)
            {
                cout<<"IMPOSSIBLE"<<endl;
                continue;
            }
            double v2 = ((c1-x)*v)/(c1-c2);
            double v1 = v-v2;
            cout<<setprecision(20)<<max(v1/r1,v2/r2)<<endl;
        }
	}
	return 0;
}
