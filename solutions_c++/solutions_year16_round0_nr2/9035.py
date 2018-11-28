#include <iostream>
#include <vector>

using namespace std;

int main(){

	int n;
	cin >> n;
	//vector<int> s1,s2;
	int prev = -1;
	int j=1;
	while(n--){
		string input;
		cin >> input;
		prev = -1;
		int allneg = 0;
		int negtopos=0, postoneg=0;
		int lastOneIsPostoNeg = 0;
		for(int i=0; i<input.length(); i++){
			if(input[i] == '-'){
				if(prev == 1){
					postoneg++; lastOneIsPostoNeg = 1;
				}
				prev = 0;
			} else{
				allneg = 1;
				if (prev == 0){ negtopos++; lastOneIsPostoNeg = 0;}
				prev = 1;
			}
		}
		int numFlips = negtopos + (postoneg > 0 ? postoneg+(1*lastOneIsPostoNeg) : 0) + (allneg==0?1:0);
		cout << "Case #" << j++ << ": " << numFlips << endl;
		
	}
	return 0;
}
