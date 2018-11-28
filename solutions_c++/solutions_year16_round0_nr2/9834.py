#include <bits/stdc++.h>
using namespace std;
#define ll long long

int a[102];

void clear(){
	for(int i=0;i<102;i++)
		a[i]=0;
}

int main() {
		int n,cnt=0,j=0;
		cin>>n;
		int flag=0;
		while(n--){
			j++;
			clear();
			cnt=0;
			flag=0;
			string str;
			cin>>str;
			for(int i=0;str[i]!='\0';i++){
				if(str[i]=='-'){
					a[i]=0;
					flag=1;
				}
				else{
					a[i]=1;
				}
			}// NOW MAKE ALL DIGITS AS 1 ;)
			if(!flag){
			cout<<"Case #"<<j<<": 0"<<endl;
			}
			else{
				for(int i=0;str[i]!='\0';i++){
					if(a[i]==0 && i==0)
						cnt++;
					if(a[i-1]==1 && a[i]==0)
						cnt++;
				}
				if(cnt==1 && a[0]==0){
					cout<<"Case #"<<j<<": 1"<<endl;
					goto end;
				}
				if(cnt==1 && a[0]==1){	
					cout<<"Case #"<<j<<": 2"<<endl;
					goto end;
				}
				if(a[0]==0){
					cout<<"Case #"<<j<<": "<<((cnt-1)*2+1)<<endl;
				}
				else
					cout<<"Case #"<<j<<": "<<((cnt)*2)<<endl;
				end:;
			}
		}
	return 0;
}