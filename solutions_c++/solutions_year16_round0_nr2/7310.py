#include<bits/stdc++.h>
using namespace std;

void fun(bool cake[],int l,int r){
	for(int i=l;i<=r;i++)
		cake[i]=!(cake[i]);
	while(l<r){
		swap(cake[l],cake[r]);
		l++;
		r--;
	}
}


int main(){
	ios::sync_with_stdio(false);
    freopen("B-large.in","r",stdin);
	freopen("code2.out","w",stdout);
	
	int t,n;
	cin>>t;
	for(int i=1;i<=t;i++){
		string str;
		cin>>str;
		n=str.length();
		bool cake[n];
		for(int j=0;j<n;j++){
			if(str[j]=='+')
				cake[j]=true;
			else
				cake[j]=false;
		}
		
		long long int count=0;
		int r=n-1,l=0;
		while(r>=0){
			if(cake[r]==true)
				r--;
			else if(cake[r]==false and cake[l]==false){
				fun(cake,l,r);
				count++;
			}
			else{
				int k=r;
				while(cake[k]!=true)
					k--;
				fun(cake,l,k);
				count++;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
		
	}
	
}
