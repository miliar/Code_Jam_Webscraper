#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>
#include <iomanip>
#include <limits.h>
//#include <sys/time.h>
//#include <time.h>
using namespace std;
#define ll long long

int main(void)
{
	int T;
	cin>>T;
	for(int _t=1;_t<=T;++_t)
	{
		string s;
		ll n;
		cin>>s;
		cin>>n;

		ll len=s.length();

		ll result=0;
		ll l=0, cnt=0;
		char v[5]={'a','i','u','e','o'};
		for(int i=0;i<len;++i){

			bool vow=false;
			for(int j=0;j<5;++j){
				if(s[i]==v[j]){
					vow=true;
					break;
				}
			}

			if(vow){
				cnt=0;
			}else{
				++cnt;
			}
			if(cnt>=n){
				ll left=i-n-l+2;
			//	cout<<i<<";"<<n<<";"<<l<<";"<<left<<endl;
			//	if(left>1)++left;
				result+=left*(len-i);	
				l=i-n+2;
			}
		}
		
		
		cout<<"Case #"<<_t<<": "<<result<<endl;
		cerr<<"cerr:"<<_t<<endl;
	}

}


//	cout.setf(ios::fixed);

