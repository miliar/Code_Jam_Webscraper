#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("inp.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int temp, num, tt = 0;
	string st;
	cin>>temp;
	while (temp--) {
		cin>>num>>st;
		int a = 0;
		int c = 0;
		for (int i = 0; i <= num; i++) {
			if(c >= i) {
				c += st[i]-'0';
			} else {
				a += i-c;
				c += i-c+st[i]-'0';
			}
		}
		cout<<"Case #"<<++tt<<": "<<a<<endl;
	}
	return 0;
}
