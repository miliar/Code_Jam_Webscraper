#include<iostream>
#include<string>
using namespace std;
int main(){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int t;
	string pancakes;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>pancakes;
		bool side=false;
		int ans=0;
		for(int i=pancakes.size()-1;i>=0;i--)
		{
			if(pancakes[i]=='-'&&side==false)
			{
				ans++;
				side=true;
			}
			if(pancakes[i]=='+'&&side==true)
			{
				ans++;
				side=false;
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<"\n";
	}
	return 0;
}
