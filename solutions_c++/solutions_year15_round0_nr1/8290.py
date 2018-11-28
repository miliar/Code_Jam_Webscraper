#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
main(){
freopen ("A-large.in", "r", stdin);
  freopen ("output1.txt", "w", stdout);
	long long int t,max,count,i,ans,j=1,k;
	cin>>t;
	while(t--){
		count=0;ans=0;
		cin>>max;
		char a[max+1];
		cin>>a;
		count=a[0]-48;
		for(i=1;i<=max;i++){
			if(a[i]-48==0){
				//cout<<"1"<<endl;
			}
			else if(count>=i){
				count+=(a[i]-48);
				//cout<<"3"<<endl;
			}
			else
			{
				k=i-count;
				ans+=k;
				count=(a[i]-48)+count+k;
				//cout<<"2"<<endl;
			}
			
		
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	j++;
	}
}
