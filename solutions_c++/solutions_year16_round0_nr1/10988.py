#include <bits/stdc++.h>
using namespace std;
map<int,int> m1;
int main()
{
	int t;
	cin>>t;
	while(t--) {
		int n,fl=1,c,d,ans=0;
		cin>>n;
	c=n;
		if(n==0){
			cout<<"INSOMNIA"<<endl;
			fl=0;}
		while(fl) {
			while(c && fl) {
			d= c%10;
			m1[d]++;
			c/=10;
			if(m1[0] != 0 && m1[1] != 0 && m1[2] != 0 && m1[3] != 0 && m1[4] != 0 && m1[5] != 0 && m1[6] != 0 && m1[7] != 0 && m1[8] != 0 && m1[9] != 0){
			fl = 0;
			}}
            ans++;
			c=n*(ans+1);
		}
		if(n!=0) cout<<ans*n<<endl;
		m1.clear();
	}


return 0;
}

