#include <iostream>
using namespace std;

int main() {int t,s,temp,ans,sum;
cin>>t;
for(int i=1;i<=t;i++)
{sum=0;ans=0;
    cin>>s;
    char a[s+2];
    cin>>a;
    
    for(int j =0;j<=s;j++)
    {if(sum-j<0)
    {ans=ans+j-sum;
    sum=j;}
    
        sum=sum+a[j]-48;
       // cout<<sum<<" ";
        
    }
    cout<<"Case #"<<i<<": "<<ans<<endl;
}
	// your code goes here
	return 0;
}
