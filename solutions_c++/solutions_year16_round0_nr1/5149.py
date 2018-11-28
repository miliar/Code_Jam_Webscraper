#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <limits.h>
#include <iostream>

using namespace std;

#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define vi vector<int>
#define pb push_back
#define ll long long int
#define gi(x) scanf("%d",&x)
#define ii pair<int,int>
#define CLEAR(x,val) memset(x,val,sizeof(x))
#define SZ(v) (v).size()
#define MOD 1000000007
#define MAXN 1000009
 
long long int findNum(long long int n){
	bool digits[10];
	rep(i,0,10)	digits[i]=false;
	int found = 0;
	int mul = 1;

	while(mul<=100){
		long long tmp = n*mul;
		//cout<<tmp<<endl;
		while(tmp){
			int x = tmp%10;
			tmp = tmp/10;

			if(!digits[x]){
				digits[x] = true;
				found++;
			}
		}
		if(found == 10)	return n*mul;
		mul++;
	}

	return -1;
}

int main() {
	int t;	cin>>t;
	rep(test,1,t+1){
		int n;	cin>>n;
		ll ans = findNum(n);
		cout<<"Case #"<<test<<": ";
		if(ans == -1)
			cout<<"INSOMNIA\n";
		else
			cout<<ans<<"\n";
	}
}