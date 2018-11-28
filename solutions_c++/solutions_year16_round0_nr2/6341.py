#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	stack<char> main_stack;
	stack<char> suport_stack;
	stack<char> aux;
	string s;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>s;
		int res=0;
		for(int i=s.size()-1;i>=0;i--){
			main_stack.push(s[i]);
		}
		int frist=0;
		int count_plus=0;
		while(1){
			count_plus=0;
			frist=0;
			char c;
			if(main_stack.size()!=0)
					c=main_stack.top();

			while(c=='+' && main_stack.size()!=0){
				if(frist==0){
					frist=1;
				}
				main_stack.pop();
				suport_stack.push('+');
				if(main_stack.size()!=0)
					c=main_stack.top();
				count_plus++;
			}
			if(count_plus==s.size())
				break;
			if(frist)
				res++;
			frist=0;
			if(main_stack.size()!=0)
					c=main_stack.top();
			while(c=='-' && main_stack.size()!=0){
				if(frist==0){
					res++;
					frist=1;
				}
				main_stack.pop();
				suport_stack.push('+');
				if(main_stack.size()!=0)
					c=main_stack.top();
			}

			while(suport_stack.size()!=0){
				suport_stack.pop();
				main_stack.push('+');
			}
			
		}
		while(main_stack.size()!=0)
			main_stack.pop();
		while(suport_stack.size()!=0)
			suport_stack.pop();
		
		printf("Case #%d: %d\n",k,res);
	}

	return 0;
}