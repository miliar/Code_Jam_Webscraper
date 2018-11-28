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

const int maxn=10000+10;
bool mark[4][4]={
	{0,0,0,0},
	{0,1,0,1},
	{0,1,1,0},
	{0,0,1,1}
};
int ans[maxn][maxn][2],t,l,a[maxn];
int mat[4][4]={
	{0,1,2,3},
	{1,0,3,2},
	{2,3,0,1},
	{3,2,1,0}
};
ll x;
string s;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin>>t;
	for(int test=1;test<=t;test++){
		cin>>l>>x;
		cin>>s;
		if(l==1){
			cout<<"Case #"<<test<<": "<<"NO"<<endl;
			continue;
		}
		string now=s;
		for(int i=1;i<=x;i++)s+=now;
		l*=x;
		for(int i=0;i<l;i++){
			if(s[i]=='i')a[i]=1;
			if(s[i]=='j')a[i]=2;
			if(s[i]=='k')a[i]=3;
		}
		int cur=0,cnt=0;
		for(int i=0;i<l;i++)ans[i][i][0]=a[i];
		for(int i=2;i<=l;i++){
			for(int j=0;j<l-i+1;j++){
				ans[j][i+j-1][0]=mat[ans[j][i+j-2][0]][a[i+j-1]];
				ans[j][i+j-1][1]=mark[ans[j][i+j-2][0]][a[i+j-1]]+ans[j][i+j-2][1];
			}
		}
		bool flag=false;
		for(int i=0;i<l;i++){
			for(int j=i+2;j<l;j++){
				if(ans[0][i][0]==1 && ans[i+1][j-1][0]==2 && ans[j][l-1][0]==3 && 
				ans[0][i][1]%2==0 && ans[i+1][j-1][1]%2==0 && ans[j][l-1][1]%2==0){
					cout<<"Case #"<<test<<": "<<"YES"<<endl;	
					flag=true;
					break;
				}
			}
			if(flag)break;
		}
		if(flag)continue;
		//00
		//01
		//10
		//11
		cout<<"Case #"<<test<<": "<<"NO"<<endl;
	}
	return 0;
}
