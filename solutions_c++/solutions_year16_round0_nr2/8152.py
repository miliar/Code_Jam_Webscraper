#include<bits/stdc++.h>
using namespace std;


int swap(char *str,int n){
	int i,f=0,count=0;
	for(i=0;i<n;i++){
		if(str[i]=='+'){
			str[i]='-';
			f=1;
			}
		}
	if(f==1) count++;
	i=0;
	while(str[i]=='-'){
			f=2;
			str[i++]='+';
		}
	if(f==2) count++;
return count;
}
int main(){
	#ifndef ONLINE_JUDGE
    	freopen("inpu.txt","r",stdin);
    	freopen("out11.txt","w",stdout);
    #endif
	int t,i,j,len,cnt,k=1;
	char str[100];
	cin>>t;
	while(t--){
		int count=0;
		cin>>str;
		len=strlen(str);
		for(i=0;i<len;i++){
			if(str[i]=='-'){
				cnt=0;
				for(j=i;j<len;j++){
					if(str[j]=='+'){
						break;
						}
					cnt++;
					}
					count+=swap(str,i+cnt);
					}
			}
		//for(i=0;i<len;i++)
			//cout<<str[i];
			cout<<"Case #"<<k<<": "<<count<<"\n";
		k++;
		}
	return 0;
}
