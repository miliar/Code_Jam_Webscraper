#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream IN("A-large.in");
	ofstream OUT("A-large.out");
	int numberOfCase;
	IN >> numberOfCase;
	for(int k=0;k<numberOfCase;k++){
		int max_level;
		IN >> max_level;
		int audience[max_level+1];
		for(int i=0;i<=max_level;i++){
			char c; IN >> c;
			audience[i]=c-'0';
		}
		int standing_accumulated=audience[0], additional_friends=0;
		for(int level=1;level<=max_level;level++){
			if(standing_accumulated<level){
				int delta=level-standing_accumulated;
				standing_accumulated+=audience[level]+delta;
				additional_friends+=delta;
			}else{
				standing_accumulated+=audience[level];
			}
		}

		OUT << "Case #" << k+1 << ": " << additional_friends << endl;
	}
	return 0;
}
