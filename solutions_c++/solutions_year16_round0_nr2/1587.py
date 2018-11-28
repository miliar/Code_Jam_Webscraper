#include<iostream>
#include<cstring>
using namespace std;

int t,T,i,n,flips;
char s[105],previous;

int main(){
	cin>>T;
	for(t=1;t<=T;++t){
		flips=0;
		cin>>s;
		n=std::strlen(s);
		previous=s[0];
		for(i=1;i<n;++i){
			if(s[i]!=previous){
				++flips;
				previous=s[i];
			}
		}
		if(s[n-1]=='-')
			++flips;
		cout<<"Case #"<<t<<": "<<flips<<'\n';
	}
	return 0;
}