#include <iostream> 
#include <fstream> 
#include <math.h>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

void print(vector<int> v){
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";
	cout << "\n";
}

int findMax(vector<int> v){
	int pos = 0;
	for (int i = 1; i < v.size(); i++)
		if (v[i] > v[pos])
			pos = i;
	return pos;
}


int main() {	
	ifstream input("A-large.in");
	ofstream output("output.ou");

	int sets, n;
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
			int N, total = 0;
			vector<int> v1, v2;
			input >> N;
			
			for (int i = 0; i < N; i++){
				int temp;
				input >> temp;
				
				total += temp;
				v1.push_back(temp);
				v2.push_back(i);
			}
			
			output << "Case #" << n << ": ";
			while (v1.size() > 0){
				
				if (v1.size() == 2 && v1[0] == v1[1]){
					v1[0]--;
					v1[1]--;
					output << char(v2[0] + 65) << char(v2[1] + 65);
					if (v1[0] == 0){
						v1.clear();
						v2.clear();
					}
					else{
						output << " ";
					}
				}
				else{
					int pos = findMax(v1);
					v1[pos]--;
					output << char(v2[pos] + 65) << " ";
					if (v1[pos] == 0){
						v1.erase(v1.begin() + pos);
						v2.erase(v2.begin() + pos);
					}	
				}
				
			}
			output << "\n";
					
			
			//cout << "Case #" << n << ": " << solve(v, total) << "\n";
			//output << "Case #" << n << ": " << N << "\n";
			
		
			sets--;
			n++;
		}
		
		input.close();
		output.close();
	}
	
	return 0; 
}
