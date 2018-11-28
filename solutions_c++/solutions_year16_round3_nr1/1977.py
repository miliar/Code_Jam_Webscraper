#include<bits/stdc++.h>
using namespace std;
#define Int long long
#define p 1000000007
int main(){
	int t,T,i,n,sum,j,m,max;
	cin>>T;
	for(t=1;t<=T;t++){
		cin>>n;vector< pair<int,char> > v;m = 100000; max=0;
		for(i=0;i<n;i++){
			cin>>j;
			v.push_back(make_pair(j,'A' + i));
			if(j<m)m = j;
			if(j>max)max=j;
		}
		printf("Case #%d: ",t );
		sort(v.begin(),v.end());
		for(j=0;j<max;j++){
			for(i=n-1;i>=0;i--){
				if(v[i].first>m){
					cout<<v[i].second<<" ";
					v[i].first--;
				}
			}
		}
		if(n%2==0){
			for(i=0;i<n;i+=2){
				while(v[i].first>0){
					cout<<v[i].second<<v[i+1].second<<" ";
					v[i].first--;v[i+1].first--;
				}
			}
		}else{
			while(v[0].first>0){
				cout<<v[0].second<<" ";
				v[0].first--;
			}
			for(i=1;i<n;i+=2){
				while(v[i].first>0){
					cout<<v[i].second<<v[i+1].second<<" ";
					v[i].first--;v[i+1].first--;
				}
			}
		}
		cout<<endl;
	}
	return 0;
}