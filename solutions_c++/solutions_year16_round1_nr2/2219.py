#include <iostream>
#include <algorithm>
using namespace std;

int main() {
      freopen("B-large.in","r",stdin);
     freopen("gcj1.out","w",stdout);
	   long long t,n;long long b,c[251];long long flag;
       cin>>t;long long y=1;
       while(y<=t)
       {long long a[2505]={'0'}; 
       	cin>>n;flag=0;
       for(long long i=1;i<=n*(2*n-1);i++)
       {cin>>b;
       	a[b]++;if(b>flag)
       	flag=b;
       } 
       
       cout<<"Case #"<<y<<": ";
       for(long long i=1;i<=flag;i++)
      	if(a[i]%2==1)
       	cout<<i<<" ";
       //for(int i=1;i<=6;i++)
       //cout<<a[i]<<" ";
       	y++;
       	cout<<endl;
       }
	return 0;
}
