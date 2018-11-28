#include <iostream>
#include <bits/stdc++.h>

#define lli long long int

using namespace::std;

int main(){
	long long int t;
	cin>>t;
	long long int k=1;
	while(t){
		t--;
		cout<<"Case #"<<k<<": ";
		k++;
		lli n;
		cin>>n;
		lli a[n];
		lli sum=0;
		for(lli i=0;i<n;i++){
			cin>>a[i];
			sum+=a[i];
		}
		lli cnt=0;
		while(cnt<sum){
			lli flag=0;
			lli mx=0;
			lli index=0;
			lli zzzzz=0;
			for(lli i=0;i<n;i++){
				if(a[i]!=0){
					zzzzz++;
				}
			}
			if(zzzzz==2){
				lli ind1=-1,ind2=-1;
				for(lli i=0;i<n;i++){
					if(a[i]!=0 && ind1==-1){
						ind1=i;
					}else if(a[i]!=0){
						ind2=i;
					}
				}	
				while(a[ind1]>a[ind2]){
					cout<<(char)(ind1+'A')<<" ";
					a[ind1]--;
					cnt++;
				}
				while(a[ind2]>a[ind1]){
					cout<<(char)(ind2+'A')<<" ";
					a[ind2]--;
					cnt++;
				}
				while(a[ind1]>0){
					cout<<(char)(ind1+'A')<<(char)(ind2+'A')<<" ";
					a[ind1]--;
					cnt+=2;
				}
			}else{
				for(lli i=0;i<n;i++){
					if(mx<a[i]){
						mx=a[i];
						index=i;
						flag=1;
					}
				}
				if(flag==1){
					cnt++;
					a[index]--;
					cout<<(char)(index+'A')<<" ";;
				}
			}
		}
		cout<<endl;
	}
	return 0;
}
