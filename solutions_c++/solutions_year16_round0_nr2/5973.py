#include <bits/stdc++.h>
#include <cstring>
using namespace std;
string cup;
int main(){
	int t,flag,flag1,st,l;
	cin>>t;
	for(int v=0;v<t;v++){
		flag=0;
		st=0;
		cin>>cup;
		l=cup.size();
		while(flag==0){
			flag1=0;
			for(int i=0;i<l;i++){
				if(flag1==0&&cup[i]=='-'){
					flag1=1;
				}
				if(flag1==1&&(i+1==l||cup[i+1]=='+')){
					st++;
					for(int j=0;j<=i;j++){
						if(cup[j]=='-') cup[j]='+';
						else cup[j]='-';
					}
					break;
				}
				if(flag1==0&&i+1==l){
					flag=1;
					break;
				}
			}
		}
		cout<<"Case #"<<v+1<<": "<<st<<endl;
	}
	return 0;
}
