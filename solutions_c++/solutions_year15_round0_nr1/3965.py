#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 
#include <fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

int sum[1005];
int main() {
	int T;
	int kase=1;
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	cin>>T;
	while(T--) {
		memset(sum,0,sizeof(sum));
		int d;string s;
		cin>>d>>s;
		for(int i=0;i<s.size();i++) sum[i]=s[i]-'0';
		for(int i=1;i<s.size();i++) sum[i]+=sum[i-1];
		int ans=0;
		for(int i=1;i<s.size();i++) {
			if(sum[i-1]<i) {
				ans+=i-sum[i-1];
				for(int j=i;j<s.size();j++) sum[j]+=i-sum[i-1];
			}
		}
		cout<<"Case #"<<kase++<<": "<<ans<<endl;
	}
	return 0;
}
