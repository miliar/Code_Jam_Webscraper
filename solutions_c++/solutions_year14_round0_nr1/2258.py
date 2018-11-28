#pragma comment(linker,"/STACK:102400000,102400000")
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>
#include <cctype>
#include <list>
#include <stack>
#include <sstream>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <vector>
using namespace std;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define mset(a) memset(a,0,sizeof(a))
#define mmset(a) memset(a,-1,sizeof(a))
#define mcpy(a,b) memcpy(a,b,sizeof(a))
const int inf=1e9+7;
const long long linf=1e18;
const double pi=acos(-1.0);
typedef long double lf;
typedef vector <int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<long long,long long> pll;
typedef vector<int> vi;
int a[5][5];
int b[5][5];

int main()
{
	ios::sync_with_stdio(false);
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;cin>>t;
	for (int tt=1;tt<=t;tt++){
		int t1;cin>>t1;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
				cin>>a[i][j];
		int t2;cin>>t2;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
				cin>>b[i][j];
		int ans=0;
		int temp=0;
		for (int i=1;i<=4;i++)
			for (int j=1;j<=4;j++)
				if (a[t1][i]==b[t2][j]) ans++,temp=a[t1][i];
		cout<<"Case #"<<tt<<": ";
		if (ans==1) cout<<temp<<endl;
		else if (ans==0) cout<<"Volunteer cheated!"<<endl;
		else cout<<"Bad magician!"<<endl;
	}
	//system("pause");
    return 0;
}        