#include<iostream>
#include<cstdio>
#include<sstream>
#include<fstream>
#include<cctype>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<cstring>
#include<string>
#include<complex>
#include<bitset>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>
#include<deque>
#include<stack>
#include<iomanip>
#include<utility>

#define pb push_back
#define pp pop_back
#define xx first
#define yy second
#define mp make_pair

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int maxn=1000+10;
int t,n,a[maxn],b[maxn];
string s;
bool check(int x){
	for(int i=0;i<=n;i++)b[i]=a[i];
	b[0]+=x;
	int sum=b[0];
	for(int i=1;i<=n;i++){
		if(sum<i)return false;
		sum+=b[i];
	}
	return true;
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin>>t;
	for(int l=1;l<=t;l++){
		memset(a,0,sizeof(a));
		cin>>n>>s;
		int lo=-1,hi=1e6;
		for(int i=0;i<=n;i++)a[i]=s[i]-'0';
		while(hi-lo>1){
			int mid=(lo+hi)/2;
			if(check(mid))hi=mid;
			else lo=mid;
		}
		cout<<"Case #"<<l<<": "<<hi<<endl;
	}
	return 0;
}
