#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll eval(int mask,int base){
	ll res = 0;
	int cnt = 0;
	ll p = 1;
	while(mask>0){
		res += (mask&1)*p;
		p =  p*base;
		mask >>= 1; 
	}
	return res;
}
int main(int argc, char const *argv[])
{	
	int T;
	cin>>T;
	int S = 1;
	while(T--){

		int N,J;
		cin>>N>>J;
		int mask = 0;
		mask = mask | (1<<0);
		mask = mask | (1<<(N-1));
		int i=1;
		vector<pair<int,int> > v;
		while(i<N-1){
			v.push_back(make_pair(i,i+1));
			i+=2;
		}
		// for(int i=0;i<v.size();i++){
		// 	cout<<v[i].first<<" "<<v[i].second<<endl;
		// }
		vector<int> div;
		for(int i=2;i<=10;i++){
			div.push_back(i+1);
		}

		int num = (N-1)/2;
		int lt = (1<<num)-1;
		//cout<<num<<" "<<lt<<endl;
		int ans = 0;
		cout<<"Case #"<<S++<<":"<<endl;
		for(int i=0;i<=lt;i++){
			int j = i;
			int t = mask;
			int cnt = 0;
			while(j > 0){
				if(j&1){
					t = t | (1<<v[cnt].first);
					t = t | (1<<v[cnt].second);
				}
				cnt++;
				j >>= 1;
			}
			
			// for(int j=2;j<=10;j++){
			// 	ll temp = eval(t,j);
			// 	cout<<"eval: base: "<<j<<" val: "<<temp<<endl;
			// 	assert(temp%(j+1) == 0);
			// }
			cout<<bitset<32>(t)<<" ";
			for(int k=0;k<div.size();k++)
				cout<<div[k]<<" ";
			cout<<endl;
			ans++;
			if(ans == J)break;
		}
	}	
	return 0;
}