#include <iostream>
#include <string>
using namespace std;

int main(){
	int tCase;
	cin>>tCase;
	int t=1;
	while(t<=tCase){
		string Str,StrRes;
		cin>>Str;
		int len = Str.length();
		StrRes+=Str[0];
		for(int i =1;i<len;i++){
			char tchar;
			tchar = Str[i];
			if(StrRes[0]>tchar){
				StrRes+=tchar;
			}
			else
			{
				string tempStr;
				tempStr+=tchar;
				tempStr+=StrRes;
				StrRes=tempStr;
			}
		}
		cout<<"Case #"<<t<<": "<<StrRes<<"\n";
		t++;
	}
	
}
