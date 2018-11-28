#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	int nTestCases;
	//auto &input = cin;
	ifstream input("A-large.in");
	
	input>>nTestCases;

	for(int i = 0; i < nTestCases; i++){
		int friendsInvited = 0;
		int standing = 0;
		int maxShyness;
		string shyString;
		input>>maxShyness;
		input>>shyString;
		for(int j = 0; j <= maxShyness; j++){
			while(friendsInvited+standing<j)
			{
				friendsInvited+= j-(friendsInvited+standing);
			}
			standing += static_cast<int>(shyString[j]-'0'); 
		}
		
		cout<<"Case #"<<i+1<<": "<<friendsInvited<<endl;
	}
	
	return 0;
}

