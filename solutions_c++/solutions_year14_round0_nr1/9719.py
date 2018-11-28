#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int ct=0, cn=1; cin>>ct; getchar();
	
	while(ct--){
		
		int n=0,cnt=0,first=0,a=0,index=0,r[4];
		
		cin>>n;
		
		for(int i=1;i<=16;i++){
			cin>>a;
			if(i>4*n-4 && i<=4*n) r[index++]=a; 		
		}
	
		cin>>n;
		
		for(int i=1;i<=16;i++){
			cin>>a;
			if(i>4*n-4 && i<=4*n){
				for(int j=0;j<4;j++){
					if(a==r[j]){
						if(cnt==0) first=a;
						cnt++;
					} 
				}
			}			
		}
		
		cnt==0 ? cout<<"Case #"<<cn++<<": Volunteer cheated!"<<endl : 
			( cnt==1 ? cout<<"Case #"<<cn++<<": "<<first<<endl :
			  cout<<"Case #"<<cn++<<": Bad magician!"<<endl );
	}
	
	fclose (stdout);
	
	return 0;
}