#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-large1.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,m=1;
	cin>>t;
	char s[101];
	while(m<=t){
		cin>>s;
		int len=strlen(s),flag=1,count=0;
		while(flag){
			int i;
			for(i=1;i<len;i++){
				if(s[0]!=s[i]){
					break;
				}
			}
			if(i!=len||s[0]=='-'){
				count++;
				for(int j=0;j<i;j++){
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
			}
			flag=0;
			for(int k=0;k<len;k++){
				if(s[k]=='-'){
					flag=1;
					break;
				}
			}
		}
		cout<<"Case #"<<m<<": "<<count<<endl;
		m++;
	}
	return 0;
}
