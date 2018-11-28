#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	long T,t;
	cin>>T;
	t=T;
	while(T>0){
		long count=0;
		string s;
		cin>>s;
		int flag=1,i;
		if(s.length()==1){
			if(s[0]=='+')
				cout<<"Case #"<<t-T+1<<": "<<count<<"\n";
			else
				cout<<"Case #"<<t-T+1<<": "<<count+1<<"\n";
			flag=0;
		}else{
			while(flag){
				for(i=0;(s[i]==s[i+1])&&(i<s.length()-1);i++);
				if((i==s.length()-1)&&(s[i]=='+'))
					flag=0;
				else{
				char ch = s[i];
				for(int j=0;j<=i;j++){
					if(ch =='+')
						s[j]='-';
					else
						s[j]='+';
				}
				count++;
				}
			}
			cout<<"Case #"<<t-T+1<<": "<<count<<"\n";
		}
		T--;
	}
	return 0;
}
