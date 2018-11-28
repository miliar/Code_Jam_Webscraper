#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <iomanip>
using namespace std;

int main(int argc, char const *argv[])
{
	ifstream infile("D-large.in");
	ofstream outfile("D-large-out.ot");
	int N = 0;
	infile >> N;
	for(int i = 1; i <= N; ++i){
		int num = 0; 
		infile >> num;
		std::vector<double> naomi(num,0);
		std::vector<double> ken(num,0);
		for(int j = 0; j < num; ++j)
			infile >> naomi[j];
		for(int j = 0; j < num; ++j)
			infile >> ken[j];
		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());

        int opt = 0; 
        int dopt = 0;
        for(int j = 0; j < ken.size(); ++j){
        	if(ken[j] > naomi[opt])
        		opt ++;
        }
        
        for(int j = 0; j < ken.size(); ++j){
        	if(naomi[j] > ken[dopt])
        		dopt ++;
        }       

        outfile << "Case #" << i << ": " << dopt << " " << num - opt;
        if(N != i)
        	outfile << "\n";

		// for(int j = 0; j < naomi.size(); ++j)
		// 	cout << naomi[j] << " ";
		// cout <<endl;

		// for(int j = 0; j < naomi.size(); ++j)
		// 	cout << ken[j] << " ";
		// cout <<endl;		

	}
    
    infile.close();
    outfile.close();
    return 0;
}