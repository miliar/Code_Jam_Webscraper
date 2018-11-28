#include <iostream>
#include <cmath>
using namespace std;
int main(){
	int n,length,instances;
	cin >> n >> length >> instances;
	long long int powers[9];
	for(int l=0;l<9;l++){
		powers[l]=pow(l+2,16)+1;
	}
	string substring[8],str[512];
	substring[0]="000";
	substring[1]="001";
	substring[2]="010";
	substring[3]="100";
	substring[4]="011";
	substring[5]="101";
	substring[6]="110";
	substring[7]="111";
	for(int i=0;i<8;i++){
		for(int j=0;j<8;j++){
			for(int k=0;k<8;k++){
				str[64*i+8*j+k]="100000"+substring[i]+substring[j]+substring[k]+"1";
			}
		}
	}
	cout << "Case #1:" << endl;	
	for(int i=0;i<500;i++){
		cout << str[i]+str[i];
		for(int k=0;k<9;k++){
			k!=8 ? cout << " " << powers[k] : cout << " " << "10000000000000001";
		}
		cout << endl;
	}
	return 0;
}