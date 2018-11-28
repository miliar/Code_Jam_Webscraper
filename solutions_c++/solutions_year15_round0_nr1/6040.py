#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main(){
	int T;
	int Smax;
	
	char people;
	cin >> T;
	
	for(int i=0;i<T;i++){
		vector<int> audi;
		int friends_required=0;
		int people_standing =0;
		cin >> Smax;
		for(int j=0;j<Smax+1;j++){
			cin >> people;
			audi.push_back(int(people-'0'));
			//cout << people-'0' << " ";
		}
		
		// input for case#i : taken 

		for(int j=0;j<Smax+1;j++){
			
			if(people_standing<j){
				
				friends_required = friends_required + j - people_standing ;
				people_standing = people_standing + audi[j]+j - people_standing;
			}
			else if (people_standing >=j){
				
				people_standing = people_standing + audi[j];
			}

			
		}

		cout << "Case #" << i+1 <<": "<< friends_required <<"\n";
	}
}