#include <iostream>

using namespace std;

int main(){
	int T;

	cin>>T;

	for(int TCN = 1; TCN<=T; TCN++){
		long long P, Q;

		char s;

		int cnt=-1;

		cin>>P>>s>>Q;

		long long arr[41];
		arr[0] = 1;
		for(int i = 1; i<41; i++){
			arr[i] = arr[i-1]*2;
		}

		int possible = 0;
		int possibleNum;

		for(int i = 0; i<41; i++){
			if(Q == arr[i]){
				possible = 1;
				possibleNum = i;
				break;
			}
		}

		
		if(possible == 1){
			for(int i = 0; i<41; i++){
				if(P<arr[i]){
					cnt = possibleNum - (i-1);
					break;
				}
			}
		}else{
			if(Q%P == 0){
				int target = Q/P;
				for(int i = 0; i<41; i++){
					if(target == arr[i])
						cnt = i;
				}
			}
		}



		if(cnt>=0)
			cout<<"Case #"<<TCN<<": "<<cnt<<endl;
		else
			cout<<"Case #"<<TCN<<": impossible"<<endl;

	}



	return 0;
}