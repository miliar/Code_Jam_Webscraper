#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

int main() {
	int t;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		std::vector<int> v(smax+10),cum(smax+10);
		v[0]=cum[0]=s[0]-'0';
		for (int i = 1; i <=smax ; ++i)
		{
			v[i]=s[i]-'0';
			cum[i]=cum[i-1]+v[i];
		}	
		int numPeople=cum[smax];
		int lo=0;
		int hi=smax+10;
		int ans=1e9;
		while(lo<=hi){
			int mid=lo+(hi-lo)/2;
			int cur=mid+v[0];
			bool pos=1;
			for (int i = 1; i <= smax; ++i)
			{
				if(cur<i) {pos=0;break;}
				cur+=v[i];
			}
			if(pos){
				ans=min(ans,mid);
				hi=mid-1;
			}
			else{
				lo=mid+1;
			}
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}