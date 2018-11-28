#include<iostream>
#include<string>
#include<set>
using namespace std;
main(){
int t,j;
cin>>t;
for(j=1;j<=t;j++){
int n,count=0,temp,check,flag=1,i=2,answer;
	cin>>n;
	set<int> hold;
	answer=n;
	check=answer;
	while(1){
	
	while(check!=0){
		temp=check%10;
		hold.insert(temp);
		if(hold.size()==10){
			flag=2;
			break;
			
		}
		check/=10;
		
	}//end of inner
	if(answer==0){
	break;
	}
	else if(flag==1){
	answer=n*i;
	check=answer;
 	i++;
   }
else{
	flag=1;
	i=2;
	break;
}

}//end of outer
if(answer==0){
	cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
}
else{
cout<<"Case #"<<j<<": "<<answer<<endl;
}

}//end of test cases
	
}
