    /*sourav verma(swerve7)   IPG_2013108  ABV IIITM
         Task @ Google Code Jam */
    
#include<bits/stdc++.h>
#define ll  long long int
using namespace std;

int main()
{
    int tc;cin>>tc;
    for(int i=1;i<=tc;i++){
        int n; cin>>n;
		if(n==0) {
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<"\n";
			continue;
		}
		bool flg[11]; for(int j=0;j<11;j++) flg[j]=false;
		int cnt=10; ll p,ans;
		for(int j=1;;j++) {
			p=n*j;
			while(p!=0) {
				int rem=p%10;
				if(!flg[rem]) {
					flg[rem]=true;
					cnt--;
				}
				p/=10;
			}
			if(cnt==0) {
				ans=n*j;
				break;
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<"\n";
    }
    return 0;
}