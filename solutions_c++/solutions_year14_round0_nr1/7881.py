#include<iostream>
#include<vector>
using namespace std;

int main(){
	int T;
	cin >> T;
	int arra[T][16];
	int arrb[T][16];
	int a[T],b[T];
	for(int i = 0;i<T;i++){
		cin >> a[i];
		for(int j = 0;j<16;j++)
			cin >> arra[i][j];
		cin >> b[i];
		for(int j = 0;j<16;j++)
			cin >> arrb[i][j];
	}
	for(int i = 0;i<T;i++){
		vector<int> cnt(17,0);
		for(int j = 0;j<4;j++)
			cnt[ arra[i][4*a[i]-4 +j] ] +=1;
		for(int j = 0;j<4;j++)
			cnt[ arrb[i][4*b[i]-4 +j] ] +=1;
		vector<int> card;
		for(int j = 1;j<=16;j++){
			if(cnt[j]==2)
				card.push_back(j);
		}
		if(card.size()>1)
			cout << "Case #" <<i+1 << ": Bad magician!" << endl;
		else if(card.size() ==1)
			cout << "Case #" <<i+1 << ": " << card[0] << endl;
		else if(card.size() ==0)
			cout << "Case #" <<i+1 <<": Volunteer cheated!" << endl;
		
	}
	
	return 0;
}
