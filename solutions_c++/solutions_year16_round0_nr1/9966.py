#include<iostream>
using namespace std;

int main(){
	int t,i;
	cin>>t;
	int ans[t];
	for(i=0;i<t;i++){
		int n;
		int count=1;
		cin>>n;
		int seen[10]={0,0,0,0,0,0,0,0,0,0};
		if(n==0){
			ans[i]=0;		
		}
		else{
		    while(!(seen[0]&&seen[1]&&seen[2]&&seen[3]&&seen[4]&&seen[5]&&seen[6]&&seen[7]&&seen[8]&&seen[9])){
			n=n*count;
			int ch=n;
			while(ch!=0){
				int a=ch%10;
				seen[a]=1;
				ch/=10;
			}
			n/=count;
			count++;
		     }	
			ans[i]=n*(count-1);		
		}
			
	}
	for(i=0;i<t;i++){
		if(ans[i]==0){
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;		
		}
		else{
			cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;		
		}			
	}
return 0;
}
