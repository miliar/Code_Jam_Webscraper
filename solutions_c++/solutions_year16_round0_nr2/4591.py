#include<iostream>
#include<stdio.h>
#include<cstdlib>
#include<cstring>
using namespace std;

int main(){

int t,i,j,d,x,len,count;
char s[101];
char p;

cin>>t;
for(d=1;d<=t;d++){

cin>>s;
len=strlen(s);
count=0;

x=0;
while(1){

p=s[x];

for(i=x+1;i<len;i++){
if(s[i]!=p){
x=i;
break;
}
}

if(i< len){

	if(p=='+'){
	for(j=0;j<x;j++)
	s[j]='-';
	}
	else if(p=='-'){
	for(j=0;j<x;j++)
	s[j]='+';

	}
count++;

}else{

	if(p=='-'){	
		for(j=0;j<len;j++)
		s[j]='+';
		count++;
		}
	break;
}


}

cout<<"Case #"<<d<<": "<<count<<endl;



}




return 0;

}
