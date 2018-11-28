#include <bits/stdc++.h>

using namespace std;

int main(){
	long long int t,k=1,n,z,i,d,orig;
	cin>>t;
	while(t--){
		set<int>nums;
		for(i=0;i<=9;++i)
			nums.insert(i);
		cin>>n;
		orig=n;
		cout<<"Case #"<<k++<<": ";
		if(n==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		//cout<<"YES"<<endl;
		while(true){
			z=n;
			//cout<<"Yes";
			//cout<<z<<endl;
			while(z){
				d = z%10;
				if(nums.find(d)!=nums.end())
					nums.erase(d);
				z/=10;
			}
			if(nums.empty())
				break;
			n+=orig;
		}
		cout<<n<<endl;
	}
}