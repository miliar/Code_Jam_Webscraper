#include<iostream>
#include<string.h>
using namespace std;

char stack[100]={0};
void flip(int max_height){
	for(int i= 0;i<=max_height;i++){
		
		if(stack[i]=='-')
			stack[i]='+';
		else if(stack[i]=='+')
			stack[i]='-';
	}
	for(int i=0;i<=max_height/2;i++){
		char temp;
		temp= stack[i];
		stack[i]=stack[max_height-i];
		stack[max_height]=temp;
	}
}
int main(){
	int t;
	cin>>t;
	for (int test=1;test<=t;test++){
		cin>>stack;
		cout<<"Case #"<<test<<": ";
		int flips=0;
		int len = strlen(stack);
		for(int s=0;s<len-1;s++){
			if(stack[s]!=stack[s+1]){
				flip(s);
				flips++;
				s=0;
			}
		}
		if(stack[0]=='+')
			cout<<flips<<endl;
		else if(stack[0]=='-')
			cout<<flips+1<<endl;	
		else
			cout<<"Kuch to gadbad hai daya\n";
	}
	return 0;
}
