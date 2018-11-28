#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>
#include <string>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <cmath>
#include <cstdio>
#include <map>

using namespace std;
int p[1020];

int main()
{
	int T;
	cin>>T;
	for(int t = 1; t <=T ;++t) {
		int S;
		cin>>S;
		string tmp;
		cin>>tmp;
		for(int i = 0; i <= S; ++i) {
			p[i] = tmp[i]-'0';
		}
		long long sol = 0;
		long long stand = p[0];
		for(int i = 1; i <= S; ++i) {
			if(p[i] == 0) continue;
			if(stand < i) {
				sol += (i-stand);
				stand += (i-stand) + p[i];
			} else {
				stand+=p[i];
			}
		}

		cout<<"Case #"<<t<<": "<<sol<<endl;
		
	}
}
