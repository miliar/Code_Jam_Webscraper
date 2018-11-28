#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main()
{
	int t,max,ans,i,j,psf;
	cin>>t;
	string q;
	for(j=1;j<=t;j++){
		cin>>max;
		cin>>q;
		ans=psf=0;
		psf+=q[0]-'0';
		for(i=1;i<q.length();i++)
		{
			if(psf<i){
				ans+=i-psf;
				psf+=i-psf;
			}
			psf+=q[i]-'0';	
		}
		cout<<"Case #"<<j<<": "<<ans;
		cout<<endl;
		cout<<endl;
	}
	return 0;
}
