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

int T, F, a[4][4], b[4][4];

int main() {
	ios::sync_with_stdio(1); 
	
	#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif  
	cin>>T;
	f(i, 1, T+1){
		if(i!=1)cout<<endl;
		cout<<"Case #"<<i<<": ";
		set<int> S;
		cin>>F;
		f(j, 0, 4)f(k, 0, 4){
			cin>>a[j][k];
			if(F-1==j)S.insert(a[j][k]);
		}

		cin>>F;
		int rpta=-1;
		f(j, 0, 4)f(k, 0, 4){
			cin>>b[j][k];
			if(F-1==j){
				if(S.find(b[j][k])!=S.end())rpta=b[j][k];
				S.insert(b[j][k]);
			}
		}

		if(S.size()==7)cout<<rpta;
		else if(S.size()==8)cout<<"Volunteer cheated!";
		else cout<<"Bad magician!";

	}	

    return 0;
}