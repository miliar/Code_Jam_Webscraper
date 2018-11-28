#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	//freopen("A-large.in","r",stdin);
	char shy[1005];
	int c=1,t,l,s,i,p;
	cin>>t;
	while(c<=t){
		s = i = 0;
		cin>>l>>shy;
		s += shy[0]-48;
		for(int k=1;k<=l;k++){
			p = shy[k]-48;
			if(s>=k){
				s += p;
			}else if(p>0){
				i += k-s;
				s += k-s+p;
			}
		}
		cout<<"Case #"<<c++<<": "<<i<<endl;
	}
	return 0;
}

