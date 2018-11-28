#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas = 1,t;
	long long unsigned num, tem, c;
	cin>>t;
	while (t--) {
		cin >> num;
		cout<<"Case #"<<cas++<<": ";
		c = 1;
		if(num==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		int A[10] = {0};
		while (1) {
			tem = num * c;
			while(tem>=1)
			{
				A[tem%10]++;
				tem /= 10;
			}
			bool yes=1;
			for (int i = 0; i < 10; ++i) {
				if(A[i]==0)
				{
					yes=0;
					break;
				}
			}
			if(yes)
			{
				cout<<num*c<<endl;
				break;
			}
			c++;
		}
	}
}
