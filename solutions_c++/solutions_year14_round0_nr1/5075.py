#include<cstdio>
#include<cstring>
#include<iostream>

using namespace std;

int main(){
	
	int i,a[17],b[17],flag[17],t,ans1,ans2,count,ans,cas=1;
	
	cin>>t;
	
	while(t--){
		
		cin>>ans1;
		
		for(i=1;i<=16;i++)
			cin>>a[i];
			
		cin>>ans2;
		
		for(i=1;i<=16;i++)
			cin>>b[i];
			
		memset(flag,0,sizeof(flag));
			
		for(i=(ans1-1)*4+1;i<=(ans1-1)*4+4;i++)
			flag[a[i]]++;
			
		for(i=(ans2-1)*4+1;i<=(ans2-1)*4+4;i++)
			flag[b[i]]++;
		
		count=0;
		for(i=1;i<=16;i++){
			if(flag[i]==2){
				count++;
				ans=i;
				}
			}
			
		if(count==1)
			cout<<"Case #"<<cas<<": "<<ans<<endl;
			
		else if(count>1)
			cout<<"Case #"<<cas<<": "<<"Bad magician!"<<endl;
			
		else if(count==0)
			cout<<"Case #"<<cas<<": "<<"Volunteer cheated!"<<endl;
			
		cas++;
		
		}
		
	return 0;}
		
		