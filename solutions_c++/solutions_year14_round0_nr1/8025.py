//-------------include
#include<cstdio>
#include<string>
#include<iostream>
#include<cstring>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<climits>
#include<vector>
#include<list>
#include<deque>
#include<functional>
#include<sstream>

//-------------define
#define ALL(a)  (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define SORT(c) sort((c).begin(),(c).end())
#define DUMP(x)  cerr << #x << " = " << (x) << endl;
#define CLR(a) memset((a), 0 ,sizeof(a))
#define rep(i,n) for(int i=0;i<(int)n;i++)
#define fi first
#define se second

//-------------namespace
using namespace std;

//-------------inline
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//-------------typedef
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;

//-------------var
int dx[]={0,-1,0,1,1,1,-1,-1},dy[]={1,0,-1,0,1,-1,1,-1};

int main()
{
	int n;
	cin >> n;
	
	for(int k=0;k<n;k++){
		int row1,row2;
		cin >> row1;

		int m[4][4];
		int num[17];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cin >> m[i][j];
				num[m[i][j]]=i;
			}
		}

		string ans="v";
		cin >> row2;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				int in;
				cin >> in;
				if(num[in]==row1-1 && i==row2-1){
					if(ans=="v"){
						ans=toString(in);
					}else{
						ans="b";
					}
				}
			}
		}

		cout << "Case #" << k+1 << ": ";
		if(ans=="b")cout << "Bad magician!";
		else if(ans=="v")cout << "Volunteer cheated!";
		else cout << ans;
		cout << endl;
	}

	return 0;
}