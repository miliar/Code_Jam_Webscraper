#include<iostream>
#include<string.h>
#include<algorithm>
#include<fstream>
using namespace std;

int main(){
	ofstream fout("ans6.txt");
	ifstream fin("inp6.IN");
	int t;
	fin>>t;
	int tt=0;
	while(tt++!=t){
		char a[1002];
		fin>>a;
		string ans="";
		int len=0;
		while(a[len]!='\0')
			++len;
		if(len>0){
			ans=ans+a[0];
			for(int i=1;i<len;++i){
				char temp=a[i];
				if((ans+a[i])>=(temp+ans)){
					ans=ans+a[i];
				}else{
					ans=temp+ans;
				}
			}	
		}	
		
		fout<<"Case #"<<tt<<": "<<ans<<"\n";	
//		cout<<"\n\n\n\n\n";	
		
	}

}
