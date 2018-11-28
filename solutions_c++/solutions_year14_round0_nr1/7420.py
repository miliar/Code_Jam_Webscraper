#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int t;

	ifstream myfile;
	myfile.open ("jotain.in");
	myfile >> t;
	ofstream outf;
	outf.open ("ans.txt");
	int at = t;
	

	while(t--){
		int r = 0;
		int v;
		
		vector<int> r1;
		
		int y1; myfile >> y1;

		for(int i = 1; i < y1; i++){
			for(int u = 0; u < 4; u++){
				int tmp; myfile >> tmp;
			}
		}
		int c = 4;
		while(c--){
			int inn; myfile >> inn;
			r1.push_back(inn);
		
		}
		for(int i = y1+1; i < 5; i++){
			for(int u = 0; u < 4; u++){
				int tmp; myfile >> tmp;
			}
		}
		myfile >> y1;

		for(int i = 1; i < y1; i++){
			for(int u = 0; u < 4; u++){
				int tmp; myfile >> tmp;
			}
		}
		c = 4;
		while(c--){
			int inn; myfile >> inn;
			r1.push_back(inn);
		
		}

		for(int i = y1+1; i < 5; i++){
			for(int u = 0; u < 4; u++){
				int tmp; myfile >> tmp;
			}
		}

		sort(r1.begin(), r1.end());

		for(int i = 0; i < r1.size()-1; i++){
			if(r1[i] == r1[i+1]){
				int e = r1[i]; int e2 =r1[i+1];
				r++;
				v = r1[i];
				i++;
			}
		}

		
	
		if(r == 0)
			outf << "Case #" << at-t << ": Volunteer cheated!\n"; 
		else if(r == 1)
			outf << "Case #" << at-t << ": " << v << "\n"; 
		else
			outf << "Case #" << at-t << ": Bad magician!\n"; 
	
	}

	myfile.close();
	outf.close();
	return 0;

}