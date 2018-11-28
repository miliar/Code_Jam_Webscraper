#include<iostream>
using namespace::std;

int main() {
	int T, Smax, sumprev, str[1001],result;
	char temp;

	cin>>T;
	for(int i=1;i<=T;i++){
		result=0;
		cin>>Smax;
		for(int k=0;k<=Smax;k++){
			cin>>temp;
			str[k]=temp-'0';
		}
		sumprev=str[0];
		for(int j=1 ; j<=Smax ; j++){
			if (j > sumprev){
				result+= j - sumprev;
				sumprev+= j - sumprev ;
			}
			sumprev+=str[j];
		}

		cout<<"Case #"<<i<<": "<<result<<endl;
	}
	return 0;
}
