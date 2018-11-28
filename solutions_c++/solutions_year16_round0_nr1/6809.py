#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
#include <functional>
using namespace std;

#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define ll long long
#define ld long double
#define mod 1000000007
#define inf 1061109567LL
#define pii pair< int, int >
#define pll pair< ll, ll >
#define psi pair< string, int >
bool vis[10];
int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	int T=1;
	while(t--){
		CLR(vis);
		string s;
		cin>>s;
		if(s=="0"){
			cout<<"Case #"<<T<<": "<<"INSOMNIA"<<endl;
			T++;
			continue;
		}
		int cnt = 0;
		int j = 2;
		string s1=s;
		while(cnt<10){
			for(int i=0;i<s1.size();i++){
				if(!vis[s1[i]-'0']){
					vis[s1[i]-'0'] = true;
					cnt++;
				}
			}
			if(cnt>=10)
				break;
			int carry = 0;
			s1 = s;
			for(int i=s1.size()-1;i>=0;i--){
				int c = s1[i]-'0';
				c*=j;
				c=c+carry;
				s1[i] = '0'+(c%10);
				carry = c/10;
			}
			j++;
			while(carry){
				char c = (carry%10) + '0';
				s1 = c+s1;
				carry/=10;
			}
			//cout<<s1<<endl;
		}
		cout<<"Case #"<<T<<": "<<s1<<endl;
		T++;
	}
	return 0;
}