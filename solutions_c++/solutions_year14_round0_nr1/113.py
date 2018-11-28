#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool cards[17];

int main(){
	int nt;
	cin >> nt;
	for(int t=0;t<nt;t++){
		int r;
		memset(cards,0,sizeof(cards));
		cin >> r;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				int tmp;
				cin >> tmp;
				if(i==r){
					cards[tmp]=true;
				}
			}
		}
		cin >> r;
		int result = -1;
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				int tmp;
				cin >> tmp;
				if(i==r && cards[tmp]){
					if(result == -1)
						result = tmp;
					else{
						result = -2;
					}
				}
			}
		}
		cout << "Case #" << t+1 << ": ";
		if(result == -2)
			cout << "Bad magician!";
		else if(result == -1)
			cout << "Volunteer cheated!";
		else
			cout << result;
		cout << endl;
	}
	return 0;
}