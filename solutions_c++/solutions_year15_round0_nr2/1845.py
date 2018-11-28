/* attention to overflow */
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <queue>
#include <sstream>
#include <set>
#include <map>
#include <cmath>
#include <numeric>
#include <tuple>
#include <iomanip>

#define dump(x) cerr<< #x << " = " << x <<endl
#define ALL(container) (container).begin(),(container).end()

using namespace std;
const int INF = 1 << 25;
void io() { cin.tie(0); ios::sync_with_stdio(false);}
template <class S,class T> ostream& operator<<(ostream& os, const pair <S,T> &s){return os<<'('<<s.first<<','<<s.second<<')';}
/*printf("%.9Lf\n",cf);*/
const int MOD = 1000000007;
const double EPS=1e-8;

const int MAX_N=2010;
int bit[MAX_N+1],n;

int sum(int i){
	int s=0;
	while(i>0){
		s+=bit[i];
		i-=i&-i;
	}
	return s;
}

void add(int i,int x){
	while(i<=n){
		bit[i]+=x;
		i+=i&-i;
	}
}

int main() {
	io();
	int N;
	cin>>N;
	n=1010;
	for(int i=0;i<N;i++){
		int d;
		cin>>d;

		fill_n(bit,MAX_N,0);
		for(int j=0;j<d;j++){
			long long a;
			cin>>a;
			add(a,1);
		}

		/*for(int j=0;j<10;j++){
			cerr<<sum(j)<<endl;
		}*/

		int ret=INF;
		for(int j=1;j<=1000;j++){
			int tmp=j;
			for(int k=j;k<=1000;k+=j){
				tmp+=(sum(min(1010,k+j))-sum(k))*(k/j);
			}
			//cerr<<j<<' '<<tmp<<endl;
			ret=min(ret,tmp);
		}

		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}

	return 0;
}