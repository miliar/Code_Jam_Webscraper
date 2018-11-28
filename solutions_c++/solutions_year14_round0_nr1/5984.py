#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int N; 
	cin>> N ; 

	for(int T = 1 ; T <= N ; T++) {
		int my_row, ma_row;
		int my_card_arr[4][4];
		int ma_card_arr[4][4];

		cin>> my_row;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				cin>>my_card_arr[i][j];

		cin>> ma_row;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				cin>>ma_card_arr[i][j];
		
		int cnt = 0 ;
		int card;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				if( my_card_arr[my_row-1][i] == ma_card_arr[ma_row-1][j]){
					cnt++;
					card = my_card_arr[my_row-1][i];
				}
		if(cnt == 0)
			cout<<"Case #"<<T<<": Volunteer cheated!"<<endl;
		else if(cnt == 1)
			cout<<"Case #"<<T<<": "<<card<<endl;
		else
			cout<<"Case #"<<T<<": Bad magician!"<<endl;
	}
	return 0 ;
}