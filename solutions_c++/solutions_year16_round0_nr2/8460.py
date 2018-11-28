#include <iostream>
#include <string>
#include <algorithm>
#include <stack>

using namespace std;
 string task(string str,int start,int end){
	stack <char> s;

	for(int i = end; i >= start ; i--){
	//cout<<"Rotate&Reverse\n";	
		if( str[i] == '-')
			s.push('+');
		else
			s.push('-');
	}	

	for(int i = end; i >= start ; i--){
		str[i] = s.top();
		s.pop();
	}
	return str;
	}

int main(){
int T;
cin>>T;

for(int t = 0; t < T; t++){
	string stack;
	std::string::size_type isthere;	
	cin>>stack;
	int len = stack.length() -1,count=0;
	bool finish = false;
	while(1){
		//cout<<"Checking\n";
		if( stack[0] == '-' ){
			//cout<<"In - \n"<<stack<<"\n";
			for( int i = len ; i >= 0;i--){

			if( stack[i] == '-'){
				stack = task(stack,0 , i);
				len = i;
				count++;
				//cout<<"In - a4 : "<<stack<<"\n";
				break;
				}


				}  

		}
		else{ //cout<<"In +\n"<<stack<<"\n";
	for( int i = len ; i >= 0;i--){
		/*if( stack[i] == '+'){
		stack = task(stack,0,i);
		//len = i;
		break;
		}else 
		*/if( stack[i] == '-' && stack[i - 1] == '+'){
				stack = task(stack,0 , i - 1);
				count++;
				//cout<<"In + a4 : "<<stack<<"\n";
				break;
				}else{
				continue;
				//stack = task(stack,0 , i);
				//len = i;		
				//count++;
				//cout<<"In + a4 : "<<stack<<"\n";
				//break;
				

			}

		}		
		}
		//cout<<"In Main\n"<<stack<<"\n";
		isthere = stack.find('-');
		if(isthere == std::string::npos){
		finish = true;
		cout<<"Case #"<<t+1<<": "<<count<<"\n"; 
		break;
		}	
		}

		}
	
	}
