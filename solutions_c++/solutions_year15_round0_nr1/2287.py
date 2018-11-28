#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outputQR1.txt","w",stdout);
	int t,n,i,s,c,tc=1;
	string str;
	cin>>t;
	while(t--) {
		cin>>n;
		cin>>str;
		c = 0;
		s = 0;
		for(i = 0; str[i]; i++) {
			if(s < i && str[i]-48 > 0) {
				c += (i-s);
				s = i+str[i]-48;
			}
			else if(s >= i){
				s += str[i]-48;
			}
		}
		cout<<"Case #"<<tc<<": "<<c<<endl;
		tc++;
	}
}
