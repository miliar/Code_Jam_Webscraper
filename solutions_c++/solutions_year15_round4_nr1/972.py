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
#define X real()
#define Y imag()

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef complex<double> point;

const int maxn=100+10;
char C[maxn][maxn];
int cnt[maxn][2];
int t,r,c;
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin>>t;
	for(int l=1;l<=t;l++){
		memset(cnt,0,sizeof(cnt));
		cin>>r>>c;
		int ans=0;
		for(int i=1;i<=r;i++){
			for(int j=1;j<=c;j++){
				cin>>C[i][j];
				if(C[i][j]!='.')cnt[i][0]++;
				if(C[i][j]!='.')cnt[j][1]++;
			}
		}
		cout<<"Case #"<<l<<": ";
		bool f=false;
		for(int i=1;i<=r;i++){
			for(int j=1;j<=c;j++){
				if(C[i][j]=='<'){
					if(cnt[i][0]==1 && cnt[j][1]==1)f=true;
					else ans++;
					break;
				}
				else if(C[i][j]!='.')break;
			}
			for(int j=c;j>=1;j--){
				if(C[i][j]=='>'){
					if(cnt[i][0]==1 && cnt[j][1]==1)f=true;
					else ans++;
					break;
				}
				else if(C[i][j]!='.')break;
			}
		}
		for(int j=1;j<=c;j++){
			for(int i=1;i<=r;i++){
				if(C[i][j]=='^'){
					if(cnt[i][0]==1 && cnt[j][1]==1)f=true;
					else ans++;
					break;
				}
				else if(C[i][j]!='.')break;
			}
			for(int i=r;i>=1;i--){
				if(C[i][j]=='v'){
					if(cnt[i][0]==1 && cnt[j][1]==1)f=true;
					else ans++;
					break;
				}
				else if(C[i][j]!='.')break;
			}
		}
		if(f)cout<<"IMPOSSIBLE";
		else cout<<ans;
		cout<<endl;
	}
	return 0;
}
