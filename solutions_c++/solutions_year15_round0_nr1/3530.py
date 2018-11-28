//in the name of god!
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <fstream>
using namespace std;
#define pb push_back
#define x first
#define y second
#define mk make_pair
string s;
int T;
int main()
{	
	ios_base::sync_with_stdio(0);
	cin>>T;
	for(int t=0;t<T;t++){
		s.erase();
		int smax;
		cin>>smax>>s;
		long long ans = 0,cur = 0;
		if(s[0]=='0'){
			ans++;
			cur++;
		}
		cur+=s[0]-'0';
		for(int i=1;i<s.size();i++){
			//cerr<<cur<<" "<<i<<" "<<s[i]<<endl;
			if(i>cur){
				ans++;
				cur+=i-cur;
			}
			cur+=s[i]-'0';
		}
		cout<<"Case #"<<t+1<<": "<<ans<<endl;
	}
	return 0;
}

