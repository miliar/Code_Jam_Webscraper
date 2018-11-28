#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
	    int s,as[1005];
	    char a[1005];
	    cin>>s>>a;
	    for(int j=0;j<=s;++j) as[j]=a[j]-48;
	    int temp=as[0],ans=0;
	    for(int j=1;j<=s;++j)
	    {
	        if(j>temp && as[j]>0)
	        {
	            ans+=j-temp;
	            temp=temp+ans;
	            temp+=as[j];
	        }
	        else temp+=as[j];
	    }
	    cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
