#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	ofstream outfile;
	outfile.open("dwar.out");
	ifstream infile;
	infile.open("D-large.in");
	int testCase;
	infile>>testCase;
	for(int i=1;i<testCase+1;++i) {
		int naomiWarScore = 0;
		int naomiDWarScore = 0;
		int NoBlocks;
		infile>>NoBlocks;
		vector<double> naomi;
		vector<double> ken;	
		double temp;
		for(int j=0;j<NoBlocks;++j) {
			infile>>temp;
			naomi.push_back(temp);
		}
		for(int j=0;j<NoBlocks;++j) {
			infile>>temp;
			ken.push_back(temp);
		}		
		sort(ken.begin(),ken.end());	//sort the mass of the blocks that ken has
		sort(naomi.begin(),naomi.end());
		vector<double> warKen(ken);
		//if war is played
		std::vector<double>::iterator up;
		for(int j=0;j<NoBlocks;++j) {
			up = upper_bound (warKen.begin(), warKen.end(), naomi[j]);
			if(up==warKen.end()) {	//every element is smaller
				++naomiWarScore;
				warKen.erase(warKen.begin());	//put the block with the smallest weight on the scale
			}
			else
				warKen.erase(up);
		}
		//if dwar is played
		for(int j=0;j<NoBlocks;++j) {
			up = upper_bound (ken.begin(), ken.end(), naomi[j]);
			if(up==ken.begin()) {		//every element is larger
				ken.pop_back();
			}
			else {				
				++naomiDWarScore;
				ken.erase(ken.begin());	//put the block with the smallest weight on the scale
			}
		}
		outfile<<"Case #"<<i<<": "<<naomiDWarScore<<" "<<naomiWarScore<<endl;
	}
	
}
