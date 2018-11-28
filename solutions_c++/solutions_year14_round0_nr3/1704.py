#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<vector>
#include<complex>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<numeric>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>
 
#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};

int bitcount(long bits)
{
	bits = (bits & 0x55555555) + (bits >> 1 & 0x55555555);
	bits = (bits & 0x33333333) + (bits >> 2 & 0x33333333);
	bits = (bits & 0x0f0f0f0f) + (bits >> 4 & 0x0f0f0f0f);
	bits = (bits & 0x00ff00ff) + (bits >> 8 & 0x00ff00ff);
	return (bits & 0x0000ffff) + (bits >>16 & 0x0000ffff);
}

void solve(vector<string> &str,int x,int y){
	if(str[y][x] != '.' && str[y][x] != 'C'){
		return ;
	}
	int bomcnt = 0;
	for(int i=-1;i<=1;i++){
		for(int j=-1;j<=1;j++){
			if((i==0&&j==0) || x+j < 0 || y+i < 0 || str[0].size() == x+j || str.size() == y+i){
				continue;
			}

			if(str[y+i][x+j] == '*'){
				bomcnt++;
			}
		}
	}
	
	if(bomcnt == 0){
		str[y][x] = bomcnt+'0';
		for(int i=-1;i<=1;i++){
			for(int j=-1;j<=1;j++){
				if((i==0&&j==0) || x+j < 0 || y+i < 0 || str[0].size() == x+j || str.size() == y+i){
					continue;
				}
				solve(str,x+j,y+i);
			}
		}
	}else{
		str[y][x] = bomcnt+'0';
	}
}


int main(){
	int n;
	cin >> n;

	rep(loop,n){
		int r,c,m;
		cout << "Case #" << (loop+1) << ":" << endl;

		cin >> r >> c >> m;
		int mapsize = r*c;
		bool notflag = true;
		rep(i,1<<(mapsize-1)){
			int usenum = i;
			usenum <<= 1;
			if(bitcount(i) != m){
				continue;
			}
			vector<string> str;
			rep(j,r){
				string buf = "";
				rep(k,c){	
					if(usenum & (1 << (j*c+k))){
						buf += "*";
					}else{
						buf += ".";
					}

					if(j+k == 0){
						buf[0] = 'C';
					}
				}
				str.pb(buf);
			}

			solve(str,0,0);
			bool flag = true;
			rep(j,r){
				rep(k,c){
					if(str[j][k] == '.'){
						flag = false;
					}else if('0' <= str[j][k] && str[j][k] <= '9'){
						str[j][k] = '.';
					}
				}
			}
			str[0][0] = 'C';
			if(flag){
				rep(j,r){
					cout << str[j] << endl;
				}
				notflag = false;
				break;
			}
		}
		if(notflag){
			cout << "Impossible" << endl;
		}
	}
}