#include <cstdio>
#include <iostream>

using namespace std;

int main(){
	int T;
	int num[15];
	int ans[15];
	string A;
	scanf("%d%*c",&T);
	for(int h=1;h<=T;++h){
		char ans[700];
		for(int i=0;i<15;++i){
			num[i]=0;
		}
		getline(cin,A);
		for(int i=0;i<A.length();++i){
			switch(A[i]){
				case 'Z' :
					++num[0];
					break;
				case 'W' :
					++num[2];
					break;
				case 'U' :
					++num[4];
					break;
				case 'X' :
					++num[6];
					break;
				case 'G' :
					++num[8];
					break;
				case 'O' :
					++num[1];
					break;
				case 'T' :
					++num[3];
					break;
				case 'F' :
					++num[5];
					break;
				case 'S' :
					++num[7];
					break;
				case 'N' :
					++num[9];
					break;
				default :
					;		
			}
		}

		num[1]-=num[0];
		num[1]-=num[2];
		num[3]-=num[2];
		num[1]-=num[4];
		num[5]-=num[4];
		num[7]-=num[6];
		num[3]-=num[8];
		
		num[9]-=num[1];
		num[9]-=num[7];
		num[9]/=2;

		printf("Case #%d: ",h);
		for(int i=0;i<10;++i){
			for(int j=0;j<num[i];++j){
				printf("%d",i);
			}
		}
		printf("\n");
	}

	return 0;
}
