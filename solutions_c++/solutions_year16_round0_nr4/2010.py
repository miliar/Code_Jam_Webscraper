#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int j = 0; j < t; ++j)
	{
		
	long long int s,c,k;
	cin>>s>>c>>k;
	cout<<"Case #"<<j+1<<": ";
	if((s+c - 1)/c > k) cout<<"IMPOSSIBLE"<<endl;
	else {
		long long int cur = 1;
		int flag = 0;
		for (int 	i = 1; i <= s; i++) {
			cur = (cur - 1)*s + (lli)i;
			if(i%c == 0) {
				cout<<cur<<" ";
				cur = 1;
				flag = 1;
			} else
				flag = 0;
		}
		if(!flag) cout<<cur<<endl;
		else cout<<endl;
	}
}
	return 0;
}