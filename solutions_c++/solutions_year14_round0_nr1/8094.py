#include<iostream>
#include<map>
using namespace std;
int main() {
	int T;
	int guessed1, guessed2;
	cin>>T;
	for(int i=0;i<T;++i) {
		map<int,bool> mappedElements;
		int firstCards[4][4];
		int secondCards[4][4];
		int elementFound = -1;
		bool isBadMagician = false;
		cin>>guessed1;
		--guessed1;
		for(int j=0;j<4;++j){
			for(int k=0;k<4;++k) {
				cin>>firstCards[j][k];
				if(j==guessed1)
					mappedElements.insert(pair<int,bool>(firstCards[j][k],true));
			}
		}
		cin>>guessed2;
		--guessed2;
		for(int j=0;j<4;++j){
			for(int k=0;k<4;++k) {
				cin>>secondCards[j][k];
				if(j==guessed2) {
					if(elementFound == -1) {
						if(mappedElements.find(secondCards[j][k])!=mappedElements.end())
							elementFound = secondCards[j][k];
					}
					else {
						if(mappedElements.find(secondCards[j][k])!=mappedElements.end()){
							isBadMagician = true;
						}
					}
				}
			}
		}
		if(elementFound == -1) {		
			cout<<"Case #"<<i+1<<": Volunteer Cheated!\n";
		}
		else if(isBadMagician == false)
			cout<<"Case #"<<i+1<<": "<<elementFound<<"\n";
		else
			cout<<"Case #"<<i+1<<": Bad magician!\n";
	}
}
