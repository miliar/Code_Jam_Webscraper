#include <algorithm>
#include <bitset>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

#define inf 1<<30
#define eps 1e-8
#define pi acos(-1)
#define mod 1000000007

#define vi vector<int>
#define pb(x) push_back(x)
#define f(i,x,y) for(int i=x;i<y;i++)
#define rf(i,y,x) for(int i=y;i>=x;i--)
#define cerr1(x) cerr<<x<<endl
#define cerr2(x,y) cerr<<x<<" "<<y<<endl
#define bit(x) __builtin_popcount(x)
#define clr(a, val) memset(a, val, sizeof(a))
#define sorta(a) sort(a, 0, sizeof(a))
#define sortv(x) sort((x).begin(),(x).end())
string tos(int a) { ostringstream os(""); os << a; return os.str(); }


int T;
long double C, F, X;
vector<long double> v;
int main() {
	ios::sync_with_stdio(1); 
	
	#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif  
    
    cin>>T;
    f(i, 1 , T+1){
    	v.clear();
    	if(i!=1)cout<<endl;
		cout<<"Case #"<<i<<": ";
		cin>>C>>F>>X;
		
		v.push_back(0);
		f(ii, 1, 1000000){
			v.push_back(v[ii-1]+ C/(long double)(2+(ii-1)*F));
		}
		double mini= inf;
		double newmin= inf - 1;
		int p=0; 
		while(newmin< mini){
			mini= newmin;
			newmin=v[p]+X/double(2+p*F);
			p++;
		}
		printf("%.7llf",mini);
	}
    return 0;
}