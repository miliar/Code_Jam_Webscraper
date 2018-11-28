#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;
int main(){
int t,x,y,i,j,a[20],b[20],arr[20][20],count,ca=0,res;
cin>>t;
while(t--){
	ca++;
	for(i=0;i<20;i++){
		a[i]=0;
		b[i]=0;
		}
	
	
	cin>>x;
	
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			cin>>arr[i][j];
			if(i==(x-1)){
				a[arr[i][j]]++;
			}
		}
	}
	cin>>y;
	
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			cin>>arr[i][j];
			if(i==(y-1)){
				b[arr[i][j]]++;
			}
		}
	}
	count =0;

	
	for(i=1;i<=16;i++){
		if(a[i]==b[i] && a[i]!=0 && b[i]!=0){
			
			count++;
			res = i;	
		}
	}
	
	
	if(count==1){
		cout<<"Case #"<<ca<<": "<<res<<endl;
		
	}else{
		if(count==0){
				cout<<"Case #"<<ca<<": Volunteer cheated!"<<endl;
			
			
		}else{
			cout<<"Case #"<<ca<<": Bad magician!"<<endl;
		
		}
		
	}
	
}

return 0;
}

