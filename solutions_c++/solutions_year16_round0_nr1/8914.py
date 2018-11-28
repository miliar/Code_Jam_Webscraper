#include "bits/stdc++.h"
using namespace std;
vector<int> v;
void counting(int i,int n){
	v.clear();
	int c=0,m=n;
	if(n!=0){
		while(v.size()<10){
			int a=n;
			while(a!=0){
				if(std::find(v.begin(), v.end(), (a%10))!=v.end())
					c++;
				else
					v.push_back(a%10);
				a/=10;
			}
			n+=m;
		}
		cout<<"Case #"<<i<<": "<<n-m<<endl;
	}
	else{
		cout<<"Case #"<<i<<": INSOMNIA"<<endl;
	}
}
int main(){
	int t;
	cin>>t;
	for (int i = 1; i <=t; ++i)	{
		int n;
		cin>>n;
		counting(i,n);
	}
	return 0;
}