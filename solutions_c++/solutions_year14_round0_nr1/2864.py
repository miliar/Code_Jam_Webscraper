#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <string.h>
#include <queue>
#include <iomanip>
#include <map>
#include <string>
#include <time.h>
#include <stack>
 
using namespace std;
#define LL long long
#define MAXN 110
#define MAXE 55000
#define MOD 1000000007
#define ENTER putchar('\n');
#define TAB "\t"
#define PRINT(x) cout<<(x);
#define MAX(x,y) ((x)>(y)?(x):(y))
#define MIN(x,y) ((x)<(y)?(x):(y))
#define ABS(x) ((x)>0?(x):-(x))
#define EPS 1E-3
#define INF 0x3f3f3f3f
#define DEBUG for(int i=1;i<=20;i++){for(int j=1;j<=20;j++) {	cout << mp[i][j] << " ";	}	cout << endl;}
#define DEB(value) for(int i=1;i<=n;i++){PRINT(value[i]);TAB;}ENTER;
#define EINF 1E10
#define PI 3.1415926535
#define ULL unsigned long long

int mp[4][4];
vector<int> arr;
void init() {
	int row; cin >> row; row--;
	for(int i=0;i<4;i++) for(int j=0;j<4;j++) cin >> mp[i][j];
	arr.clear();
	for(int i=0;i<4;i++) arr.push_back(mp[row][i]);
	cin >> row; row--;
	for(int i=0;i<4;i++) for(int j=0;j<4;j++) cin >> mp[i][j];

	int cntfind=0,ans=0;
	for(int i=0;i<4;i++) {
		int cad=arr[i];
		//cout << "test " << cad << endl;
		for(int j=0;j<4;j++) {
			if(cad==mp[row][j]) {
				//cout << row << TAB << j << endl;
				cntfind++;
				ans=cad;
				break;
			}
		}
	}
	if(cntfind==0) cout << "Volunteer cheated!" << endl;
	else if(cntfind==1) cout << ans << endl;
	else cout << "Bad magician!" << endl;
}

int main(){
    freopen("A-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	int cas=0;
	int t; cin >> t;
	while(t--) {
		printf("Case #%d: ",++cas);
		init();
	}
}