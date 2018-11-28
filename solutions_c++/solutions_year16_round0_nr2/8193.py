#include <iostream>
using namespace std;

int getRightOfLeftMost(string str){
	int s=0;
	while(s < str.size() && str[s]=='+'){
		s++;
	}
	while(s < str.size() && str[s]=='-'){
		s++;
	}
	if(s-1 >= 0 && str[s-1] == '-'){
		return s-1;
	}else{
		return s;
	}
}


string flipTill(string theStack, int i){
	for (int j = 0; j <=i; ++j)
	{
		if(theStack[j]=='-')
			theStack[j]='+';
		else
			theStack[j]='-';
	}
	return theStack;
}

int main(){
	int T;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		cout<<"Case #"<<t+1<<": ";
		string theStack;
		cin>>theStack;
		int i = 0;
		int count = 0;
		while(i<theStack.size()){
			i = getRightOfLeftMost(theStack);
			if(i<theStack.size()){
				theStack = flipTill(theStack, i);
				count++;
			}
		}
		cout<<count<<endl;
	}
	return 0;
}