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

const int maxn=5000;

string best[13][3];


int main(){
	ios_base::sync_with_stdio(false);
	best[0][0]="P";
	best[0][1]="R";
	best[0][2]="S";
	for(int i=1;i<13;i++){
		string l=best[i-1][0]+best[i-1][1];
		string r=best[i-1][1]+best[i-1][0];
		if(l<r)best[i][0]=l;
		else best[i][0]=r;
		l=best[i-1][1]+best[i-1][2];
		r=best[i-1][2]+best[i-1][1];
		if(l<r)best[i][1]=l;
		else best[i][1]=r;
		l=best[i-1][0]+best[i-1][2];
		r=best[i-1][2]+best[i-1][0];
		if(l<r)best[i][2]=l;
		else best[i][2]=r;
	}
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		cout<<"Case #"<<l<<": ";
		int n,r,p,s;
		cin>>n>>r>>p>>s;
		string ans="#";
		for(int i=0;i<3;i++){
			int cs=0,cr=0,cp=0;
			for(int j=0;j<best[n][i].size();j++){
				if(best[n][i][j]=='P')cp++;
				else if(best[n][i][j]=='R')cr++;
				else cs++;
			}
			if(cs==s && cr==r && cp==p){
				if(ans=="#"){
					ans=best[n][i];
				}
				else if(ans>best[n][i]){
					ans=best[n][i];
				}
			}
		}
		if(ans=="#")cout<<"IMPOSSIBLE";
		else cout<<ans;
		cout<<endl;
	}
	return 0;
}
