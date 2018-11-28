#include <iostream>
#include <string>

using namespace std;

int main(){
	string shylevels;
	int shypeople, maxLevel, testcases, friends=0; 
	int standing=0;
	
	cin >> testcases;

	for (int j=1; j <= testcases; j++){
		cin >> maxLevel;

		cin >> shylevels;
		for(int i=0; i <= maxLevel; i++){
			shypeople = shylevels[i]-'0';
			if (standing >= i)
				standing += shypeople;
			else{ 
				friends += (i-standing);
				standing += ((i-standing) + shypeople);
			}
		}
		cout << "Case #"<< j << ": " << friends << endl;

		friends = 0;
		standing = 0;
	}
	return 0;
}