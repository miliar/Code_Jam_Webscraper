#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int T;

	double Block1[1000];
	double Block2[1000];

	cin>>T;
	
	for(int TCN = 1; TCN<=T; TCN++){
		int NoB;
		int DeW=0, NoW=0;
		cin>>NoB;

		for(int j = 0; j<NoB; j++)
			cin>>Block1[j];
		for(int j = 0; j<NoB; j++)
			cin>>Block2[j];

		sort(Block1, Block1+NoB);
		sort(Block2, Block2+NoB);

		int target = NoB-1;
		for(int j = NoB-1; j>=0; j--){
			for(int k = target; k>=0; k--){
				if(Block1[j] > Block2[k]){
					DeW++;
					target--;
					break;
				}
				target--;
			}
		}
		target = 0;
		for(int j = 0; j<NoB; j++){
			for(int k = target; k<NoB; k++){
				if(Block2[k] > Block1[j]){
					NoW++;
					target++;
					break;
				}
				target++;
			}
		}

		cout<<"Case #"<<TCN<<": "<<DeW<<" "<<NoB-NoW<<endl;



	}
	return 0;
}