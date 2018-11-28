#include<bits/stdc++.h>
#define ll   long long

#define md 1000000007

using namespace std;
int a[20];
int main()
{
	ios_base::sync_with_stdio(0);
   #ifndef ONLINE_JUDGE
            freopen("input.txt","r",stdin);
            freopen("output.txt","w",stdout);    
    #endif
      int test;
      cin>>test;
     for(int tst=1;tst<=test;tst++){
     	cout<<"Case #"<<tst<<": ";
     	for(int i=0;i<10;i++)
     		a[i]=0;
     	int ct=10;
     	ll n;
     	cin>>n;
     	if(n==0)
     		cout<<"INSOMNIA\n";
     	else{
     		ll x=n;
     		while(1){
     			ll m=n;
     			while(m){
     				if(a[m%10]==0){
     					ct--;
     					a[m%10]=1;
     				}
     				m/=10;
     			}
     			if(ct==0){
     				cout<<n<<endl;
     				break;
     			}
     			n+=x;
     		}
     	}
     }
    return 0;
    
    
    
}
