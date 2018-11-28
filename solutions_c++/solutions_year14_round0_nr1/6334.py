#include <iostream>
using namespace std;

int main() {
	int cases;
	int answer1,answer2,correctans;
	int  arrangement1[4], arrangement2[4], dummy[4];
	bool gotans = false;
	cin >> cases;
	for(int icase = 1 ; icase <=  cases ; icase++){
		gotans = false;
		correctans = 0;
		cin >> answer1;
		for(int cardrow = 0; cardrow < 4; cardrow++){
			for(int i=0;i<4;i++){
				cin>>dummy[i];
			}			
			if(cardrow == answer1-1){
				for(int i=0;i<4;i++){
					arrangement1[i]=dummy[i];
				}
			}
		}
		
		cin >> answer2;
		for(int cardrow = 0; cardrow < 4; cardrow++){
			for(int i=0;i<4;i++){
				cin>>dummy[i];
			}			
			if(cardrow == answer2-1){
				for(int i=0;i<4;i++){
					arrangement2[i]=dummy[i];
				}
			}
		}
		
		for(int i =0;i<4;i++){
			for(int j=0;j<4;j++){
				if(arrangement1[i]==arrangement2[j]){
					if(gotans){
						correctans = -1;
					}
					else{
						correctans = arrangement1[i];
						gotans=true;
					}
				}
			}
		}
		
		if(gotans && correctans!=-1){
			cout << "Case #"<<icase<<": " << correctans<< endl;
		}
		else if(!gotans){
			cout << "Case #"<<icase<<": " << "Volunteer cheated!"<< endl;
		}
		else{
			cout << "Case #"<<icase<<": " << "Bad magician!"<< endl;
		}
		
	}
	return 0;
}