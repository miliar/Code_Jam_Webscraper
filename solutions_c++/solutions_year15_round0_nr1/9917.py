#include <iostream>
using namespace std;
int main(){
	int T;
	cin >> T;
	for(int I=0; I<T; I++){
		int maxLevel, num;
		cin >> maxLevel >> num;
		int audience[1001];
		for(int i=maxLevel; i >= 0; i--){
			audience[i] = num%10;
			num /=10;
		}

//		for(int i=0; i<=maxLevel; i++)
//			cout << audience[i] << ' ';
//		cout << endl;
		int sumStand = audience[0];
//		cout << sumStand << endl;
		
		int inviteNum = 0;
		for(int i=1; i<=maxLevel; i++){
			if(i <= sumStand) 
				sumStand += audience[i];
			else if(audience[i]!=0){
				inviteNum += (i-sumStand);
				sumStand += (i-sumStand);
				sumStand += audience[i];
			}
//			cout << "sumStand:" << sumStand << "; to invite:" << inviteNum << endl;
		}

		cout << "Case #" << I+1 << ": " << inviteNum << endl;
	}
}
