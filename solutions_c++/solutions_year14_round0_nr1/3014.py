#include <iostream>

using namespace std;

int main(){
	int count[17];
	int TC,card;
	int sol1,sol2;
	int nSolution,Solution;
	cin>>TC;
	for (int T=1;T<=TC;T++){
		for (int i=0;i<=16;i++){
			count[i]=0;
		}
		cin>>sol1;
		for (int i=0;i<4;i++){
			for (int j=0;j<4;j++){
				cin>>card;
				if (sol1==i+1){
					count[card]++;
				}
			}
		}
		cin>>sol2;
		for (int i=0;i<4;i++){
			for (int j=0;j<4;j++){
				cin>>card;
				if (sol2==i+1){
					count[card]++;
				}
			}
		}

		nSolution=0;
		for (int i=1;i<=16;i++){
			if (count[i]==2){
				nSolution++;
				Solution=i;
			}
		}

		if (nSolution==0){
			cout<<"Case #"<<T<<": Volunteer cheated!\n";
		}
		else if (nSolution ==1){
			cout<<"Case #"<<T<<": "<<Solution<<"\n";
		}
		else{
			cout<<"Case #"<<T<<": Bad magician!\n";
		}
	}
	return 0;
}