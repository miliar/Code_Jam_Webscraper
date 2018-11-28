#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	
	for(int i=1; i<=cases; i++) {
		cout<<"Case #" << i << ": ";
		
		int first, second;
		cin >> first;
		
		int tab1[4];
		
		for(int j=1; j<=4; j++) {
			for(int k=0; k<4; k++) {
				int tmp;
				cin >> tmp;
				if(j==first) {
					tab1[k] = tmp;
				}
			}
		}
		
		cin >> second;
		int tab2[4];
		
		for(int j=1; j<=4; j++) {
			for(int k=0; k<4; k++) {
				int tmp;
				cin >> tmp;
				if(j==second) {
					tab2[k] = tmp;
				}
			}
		}
		
		for(int x=0; x<4; x++) {
		//	cout<< tab1[x] << " " <<tab2[x]<<endl;
		}
		
		int counter=0;
		int score;
		
		for(int j=0; j<4; j++) {
			for(int k=0; k<4; k++) {
				if(tab1[j] == tab2[k]) {
					score=tab1[j];
					counter++;
				 }
			}
		}
		
		if(counter==0) cout<< "Volunteer cheated!" <<endl;
		else if(counter > 1) cout<< "Bad magician!" <<endl;
		else if(counter == 1) cout<< score << endl;
	}
	
	return 0;
}
