#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
typedef long long ll;
#define INF (1<<29)

int main(){
	int n, tc;
	cin >> tc;
	for(int i=0;i<tc;i++){
		cin >> n;
		bool b[10], ch=false;
		int cnt=1, ans=n;
		for(int j=0;j<10;j++)b[j]=false;
		if(n==0)cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		else{
			while(!ch){
				ch=true;
				ostringstream stream;
				stream << ans;
				string s=stream.str();
				for(int j=0;j<s.length();j++)b[s[j]-'0']=true;
				for(int j=0;j<10;j++)if(b[j]==false)ch=false;
				if(!ch){
					cnt++;
					ans=n*cnt;
				}
			}
			cout << "Case #" << i+1 << ": "<< ans << endl;
		}
	}
	return 0;
}

