#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	string str;
	int i,t,T,ctr,ctr2,n;
	cin>>T;
	for(t=1;t<=T;t++){
		cin>>n;
		cin>>str;
		ctr=ctr2=0;
		for(i=0;str[i]!='\0';i++){
			if(ctr< i && (str[i]-'0' > 0))
			{	ctr2+=(i-ctr); ctr=i;	}
			ctr+= int(str[i]-'0');
		}
		cout<<"Case #"<<t<<": "<<ctr2<<endl;
	}
	return 0;
}
