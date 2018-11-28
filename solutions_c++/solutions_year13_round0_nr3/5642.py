#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<math.h>
using namespace std;
vector<long long> get_str(long long n){
	vector<long long> g;
	while(n>0){
		long long o=n%10;
		g.push_back(o);
		n/=10;
	}
	return g;
}
bool check_pal(vector<long long> n){
	long long j=n.size()-1;
	for(long long i=0;i<n.size()/2;i++){
			if(n[i]!=n[j])
				return false;
			j--;
	}
	return true;
}
bool check(long long n,long long limit){
	vector<long long> line=get_str(n);

	long long koko= pow(n,0.5);
	if(koko>limit||koko*koko<n)
		return false;

	if(check_pal(line)&&check_pal(get_str(koko)))
		return true;
	else
		return false;
}
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t=0;
	cin>>t;
	int count=0;
	while(t--){
		count++;
		long long low=0,high=0;
		cin>>low>>high;
		int result=0;
		for(long long i=min(low,high);i<=max(low,high);i++){
			if(check(i,max(low,high))){
				result++;
			}
		}
		cout<<"Case #"<<count<<": ";
			cout<<result<<endl;
	}
	return 0;
}