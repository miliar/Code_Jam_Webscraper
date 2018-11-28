#include "iostream"
#include "cstring"
#include "stdio.h"
using namespace std;

int invcnt=0;
bool check_for_plus(char str[]){
	for (int i = 0; i < strlen(str); ++i)
	{
		if(str[i]=='-')
			return false;
	}
return true; 
} 

void change_sign(char *str,int k){
	for (int i = 0; i < k; ++i)
	{
		if(str[i]=='+'){
			str[i]='-';
		}
		else
			str[i]='+';
	}
invcnt++;
}
int main(int argc, char const *argv[])

{
	unsigned long int test;
 	cin>>test;
 	unsigned long int tempt=1;
 	while(test--){
 		invcnt=0;
 		char str[150];
 		scanf("%s",str);
 		
 		bool soln=false;
 		//check for '+'
 		while(soln==false){
	 		if(check_for_plus(str)){
	 			cout << "Case #"<<tempt<<": "<<invcnt<<endl;
	 			tempt++;
	 			soln=true;
	 			break;
	 		}
	 		else{
	 			char firc=str[0];	
	 			//find pos for alike
	 			int i=0;
	 			for ( i = 1; i < strlen(str); ++i)
	 			{
	 				if(str[i]!=firc)
	 					break;
	 			}

	 			
	 			
	 			change_sign(str,i);
	 			

	 				
	 		}
	 	}
 	}
	
	return 0;
}