#include<iostream>
#include<string>
using namespace std;

int main()
{
	int T;
	cin>>T;
	int sm;
	string str;
	int t=0;
	while(T){
		cin>>sm;
		cin>>str;
		int s=0;
		int in=0;
		int i=0;
		int l=0;
		for(i=0;i<str.length();i++){
			if(s>=i){
				s=s+(str[i]-'0');
			}
			else{
				in +=i-s;
				s=s+(i-s)+(str[i]-'0');
			}
		}
		cout<<"Case #"<<++t<<": "<<in<<endl;
		T--;
	}
}
