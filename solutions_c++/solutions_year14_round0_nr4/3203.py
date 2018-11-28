#include <iostream> 
#include <fstream>
#include <set>
#include <math.h>

using namespace std;

int main() {
	ifstream input("D-large.in");
	ofstream output("output.ou");
	
	int sets, n;
	int blocks;
	double temp;
	
	set<double> naomi_set1, naomi_set2;
	set<double> ken_set1, ken_set2;
	
	set<double>::iterator it1, it2;
	
	int naomi_score;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
			naomi_set1.clear();
			naomi_set2.clear();
			ken_set1.clear();
			ken_set2.clear();
			
			input >> blocks;
			
			for(int i = 0; i < blocks; i++){
				input >> temp;
				naomi_set1.insert(temp);
				naomi_set2.insert(temp);
			}
			
			for(int i = 0; i < blocks; i++){
				input >> temp;
				ken_set1.insert(temp);
				ken_set2.insert(temp);
			}
			
			/*cout << "Naomi's set: ";
			
			for(it1 = naomi_set1.begin(); it1 != naomi_set1.end(); it1++){
				cout << *it1 << " "; 
			}
			cout << "\n";
			
			cout << "Ken's set: ";
			for(it1 = ken_set1.begin(); it1 != ken_set1.end(); it1++){
				cout << *it1 << " "; 
			}
			cout << "\n";*/
			
			naomi_score = 0;
			while(!naomi_set1.empty()){
				it1 = naomi_set1.begin();
				it2 = ken_set1.begin();
				
				while(*it2 > *it1 && it1 != naomi_set1.end()){
					it1++;
				}
				
				if(*it2 < *it1){
					naomi_score++;
				}
				else{
					break;
				}
				
				naomi_set1.erase(it1);
				ken_set1.erase(it2);
			}
			cout << "Case #: " << n << "\n";
			cout << "Naomi's score 1: " << naomi_score << "\n";
			output << "Case #" << n << ": " << naomi_score << " ";
			
			naomi_score = blocks;
			while(!naomi_set2.empty()){
				it1 = naomi_set2.begin();
				it2 = ken_set2.begin();
				
				while(*it2 < *it1 && it2 != ken_set2.end()){
					it2++;
				}
				
				//if(*it2 < *it1){
				//	it2 = ken_set1.begin();
				//	naomi_score++;
				//}
				if(*it2 < *it1){
					break;
				}
				
				naomi_score--;
				naomi_set2.erase(it1);
				ken_set2.erase(it2);
				
			}
			
			cout << "Naomi's score 2: " << naomi_score << "\n";
			output << naomi_score << "\n";
			
			
			cout << "\n\n";
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
