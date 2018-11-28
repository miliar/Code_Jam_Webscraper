#include <iostream>
#include <stdio.h>
#include <string>
 
using namespace std;

main(){
	freopen("in.txt","r", stdin);
	freopen("out.txt","w", stdout);
	int T,Smax,i,j,Sum,RS;
	string S;
	cin>>T;
	for (i=1;i<=T;i++){
		cin>>Smax;
		cin>>S;
		Sum=0;j=0;RS=0;
		while(j<=Smax){
			if (Sum < j && S[j]!='0'){
				RS += j-Sum;
				Sum = j;
			}
			Sum += int(S[j])-int('0');
			j++;
		}
		cout<<"Case #"<<i<<": "<<RS<<endl;
	}
}