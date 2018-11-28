#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large (1).in","r",stdin);
	freopen("output1.txt","w",stdout);
	int t,i;
	unsigned int j;
	cin>>t;
	for (i=0;i<t;i++){
		string s;
		cin>>s;
		string st="";
		st=s[0];
		for (j=1;j<s.length();j++){
			int temp1=st[0];
			int temp2=s[j];
			if (temp1>temp2){
				st=st+s[j];
			}
			else{
				st=s[j]+st;
			}
		}
		cout<<"case #"<<i+1<<": "<<st<<endl;
	}
}
