#include <bits/stdc++.h>

using namespace std;

int main(){
    
int tc;
    cin>>tc;
    
for(int t=1;t<=tc;t++){
	
long long n,count=0,tmp1,tmp2;
	string str;
	
cin>>n>>str;
		
tmp1=(int)str[0]-'0';
		
for(int i=1;i<=n;i++){
			 
tmp2=(int)str[i]-'0';
			if(tmp1<i){
				
count+=(i-tmp1);
			tmp1=i;}
			
tmp1+=tmp2;}
	
cout<<"Case #"<<t<<": "<<count<<endl;
	}
	
return 0;

}
