#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
#define rr 		freopen("input.txt", "r", stdin)
#define wr 		freopen("output.txt", "w", stdout)

int main() {
    ios::sync_with_stdio(0);
    rr;
    wr;
	int i,j,T,l,m;
	cin>>T;
	for(j=1;j<=T;j++){
		char S[100];
		int k=1;
		cin>>S;
		l=strlen(S);
		m=0;
		for(i=1;S[i]!='\0';i++){
			if(S[i]!=S[m]){
				k++;
				m=i;
			}
		}
		if(k==1){
			if(S[0]=='+')
		    	k=0;
		    else{
		    	k=1;
			}
		}
		else{
			if(S[l-1]=='+'){
				k--;
			}
		}
		cout<<"Case #"<<j<<": "<<k<<endl;
		
	}
	return 0;
}

