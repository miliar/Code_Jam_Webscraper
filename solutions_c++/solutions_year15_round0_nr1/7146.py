#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T, t=1;
	int maxn, res;
	string s;
	cin>>T;

	while(t <= T){
		res=0;
		cin>>maxn;
		cin>>s;

		int all = s[0]-'0';
		for(int i=1;i<=maxn;++i){
			int tmp = 0;
			if(i > all){
				tmp = i-all;
				res += (tmp);
			}
			all += (tmp+s[i]-'0');
		}
		cout<<"Case #"<<t<<": "<<res<<endl;
		++t;
	}
	return 0;
}
