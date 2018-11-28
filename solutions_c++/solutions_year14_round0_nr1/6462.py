#include<iostream>
#include<cstdio>

using namespace std;

int main(){
	int ch;
	int a[5],b[5];
	int temp;
	int temp2;

	cin >> ch;
	for(int i=1;i<=ch;i++){
		cin >> temp;
		for(int j=1;j<=4;j++){
			if(j == temp){
				cin >> a[1] >> a[2]>>a[3]>>a[4];
			}
			else {
				cin >> temp2 >> temp2 >> temp2 >> temp2;
			}
		}

		cin >> temp;
		for(int j=1;j<=4;j++){
			if(j == temp){
				cin >> b[1] >> b[2]>>b[3]>>b[4];
			}
			else {
				cin >> temp2 >> temp2 >> temp2 >> temp2;
			}
		}

		int matchedCount = 0;
		int val = -1;

		for(int j =1; j<=4;j++){
			for(int k=1;k<=4;k++){
				if(a[j] == b[k]){
					matchedCount++;
					val = a[j];
				}
			}
		}

		cout << "Case #" << i << ": ";
		switch(matchedCount){
			case 1:
				cout << val<<endl;
				break;
			case 2:
				cout << "Bad magician!" << endl;
				break;
			case 3:
				cout << "Bad magician!" << endl;
				break;
			case 4:
				cout << "Bad magician!" << endl;
				break;
			case 0:
				cout << "Volunteer cheated!" << endl;
		}
	}
	return 0;
}