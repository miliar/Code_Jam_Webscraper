#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
char s[1111];
int x[1111];
int main() {
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		int sm;
		cin>>sm;
		cin>>s;
		for(int i=0;i<=sm;i++)x[i]=s[i]-'0';
		int to=x[0];
		int an=0;
		for(int i=1;i<=sm;i++){
		//cout<<i<<" "<<an<<" "<<to<<endl;
			if(i>to&&x[i]>0){
				an=an+(i-to);
				to=to+(i-to);
			}
			to=to+x[i];
		}
		cout<<"Case #"<<tt<<": "<<an<<endl;
	}
	return 0;
}

