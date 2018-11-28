#include<bits/stdc++.h>

using namespace std;

int main(){
	
	ofstream out("out.txt");
	
	int t,a[1010],smax;
	string temp;
	
	cin>>t;
	
	for(int j=1;j<=t;j++){
		
		cin>>smax;
		cin>>temp;
		
		for(int i=0;i<temp.length();i++)
			a[i]=temp[i]-'0';
			
		int ans=0,count=a[0];
		
		for(int i=1;i<temp.length();i++){
			if(count<=i){
				ans+=(i-count);
				count=i;
			}
			
			count+=a[i];
		}
		
		out<<"Case #"<<j<<": "<<ans<<endl;
	}
	
	return 0;
}
		
		
	
	
