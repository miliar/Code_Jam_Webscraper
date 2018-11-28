#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
	ofstream out("file.txt");
	int t,p=0;
	cin>>t;
	while(t--)
	{
		int m;
		cin>>m;
		string s;
		cin>>s;
		int k=s.size();
		int a[k],sum=0,ans=0;
		for(int i=0;i<k;i++){
			sum=sum+s[i]-'0';
			a[i]=sum;
			if(i!=0){
				if(a[i-1]<i && a[i]>a[i-1]){
					ans+=(i-a[i-1]);
					a[i]+=ans ;sum=a[i];
				}
				
				
		    }
		    //cout<<ans<<" ff " <<endl;
	    }
		out<<"Case #"<< p+1 <<": "<< ans << endl;
		//cout<<ans<<endl;
		p++;
	}
	return 0;
}
