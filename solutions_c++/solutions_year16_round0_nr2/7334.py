#include<iostream>
#include<string.h>
using namespace std;
 
long long manouver(char *pancakes, int len){
long long count=0;
for(int i=len-1;i>=0;i--){
	if(pancakes[i]=='-'){
		count++;
		for(int j=0;j<=i;j++){
			if(pancakes[j]=='+')
			pancakes[j]='-';
			else if(pancakes[j]=='-')
			pancakes[j]='+';
		}
	}	
}
 
return count;
}
 
int main(){
long long t,curr=1, len;

cin>>t;
while(t--){
char pancakes[100];
cin>>pancakes;
len = strlen(pancakes);
cout<<"Case #"<<curr<<": "<<manouver(pancakes, len)<<endl;
curr++;
}
return 0;
}