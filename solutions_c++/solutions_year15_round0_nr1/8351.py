#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;

int main() {
	int num;
	cin>>num;
	for (int ti=1; ti<=num; ti++) {
		int smax; string str;
		cin>>smax>>str;
		vector<int> v(smax+1);
		for (int i=0; i<str.size(); i++) { char ch=str[i]; v[i]=atoi(&ch); }
		int x=0, y=0;
		for (int i=0; i<v.size(); i++)
		{
			if (x<i) {
				y+=(i-x);
				x+=(i-x);
			}
			x+=v[i];
		}
		cout<<"Case #"<<ti<<": "<<y<<'\n';
	}
	return 0;
}