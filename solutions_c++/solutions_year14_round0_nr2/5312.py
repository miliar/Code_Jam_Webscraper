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

int main(){
	int n;
	cin >> n;

	rep(loop,n){
		cout << "Case #" << (loop+1) << ": ";

		double c,f,x;
		cin >> c >> f >> x;
		double cookie = 2.0;
		double min_time = x / cookie;
		double old_time = 0.0;
		while(true){
			double use_time = c / cookie;
			cookie += f;
			old_time += use_time;
			double next_time = x / cookie;
			next_time += old_time;
			if(next_time < min_time){
				min_time = next_time;
			}else{
				break;
			}
		}
		printf("%.7f\n", min_time);
	}
}