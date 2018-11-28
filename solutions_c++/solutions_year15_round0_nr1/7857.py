#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
const int MNAX = 100;


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	getchar();

	for (int t=1;t<=test;++t){
		int n;
		string s;
		cin>>n>>s;

		int invite = 0;
		int res = 0;

		for (int i=0;i<s.length();++i){
			int x = (s[i]-'0');
			if (x!=0 && i>res){
				invite += i-res;
				res += i-res;
			}
			res+=x;
		}


		cout<<"Case #"<<t<<": "<<invite<<'\n';
	}

	return 0;
}
