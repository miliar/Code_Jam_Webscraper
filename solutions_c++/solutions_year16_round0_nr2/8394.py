#include <iostream>
using namespace std;
int main(){
	long a,l,n,tmp=0,m=0,p=0;
	bool cek=true;
	string str;
	cin>>n;
	
	for (int i=1;i<=n;i++){
		cin>>str;
		m=0; cek=true; p=0; tmp=0;
		if(str[0]=='-') m=1;
		
		l=str.length();
		while (p<l){
		
			while (str[p]=='-'){
				if (cek==false){
					tmp=tmp+2; p++; cek=true;
				} else{
					p++;
				}
			}
			if (str[p]=='+') {
				cek=false; p++;
			}
			
		}
			cout<<"Case #"<<i<<": "<<tmp+m <<endl;
	}
	return 0;
}
