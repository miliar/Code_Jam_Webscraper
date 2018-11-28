/*
Author: Pushpendra singh
Problem: 
Algorithm:  
*/
 
#include <bits/stdc++.h>
using namespace std;

int main(){
		
	int t,n,pre,current,ans1,ans2,a[1500];
	int rate,temp,count=1,i;
	#ifndef ONLINE_JUDGE
		freopen("inp.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	cin>>t;
	while(t--){
		cout<<"Case #"<<count<<": ";
		cin>>n;
		cin>>a[0];
		ans1=ans2=0;
		rate=temp=0;
		for(i=1;i<n;i++){
			cin>>a[i];
			if(a[i-1] > a[i]){
				ans1+=(a[i-1]-a[i]);
				rate=(a[i-1]-a[i]);
				if((temp)<(rate)) temp=rate;

			}
		}

		for(i=0;i<n-1;i++){
			if(a[i]>=(temp)){
				ans2+=temp;
			}
			else{
				ans2+=a[i];
			}
		}
		cout<<ans1<<" "<<ans2<<endl;
		count++;
	}
	
	
	return 0;
}    
