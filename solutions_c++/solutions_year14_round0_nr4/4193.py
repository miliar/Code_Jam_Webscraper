#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <fstream>
using namespace std;

int main () {
  ofstream myfile;
  ifstream input;
  input.open("file.in");
   myfile.open ("example.txt");
   	int t;
	input>>t;
	for(int i=1; i<=t; i++){
		int n;
		input>>n;
		double a;
		vector<double> naomi, ken;
		for(int j=0; j<n; j++){
			input>>a;
			naomi.push_back(a);
		}
		for(int j=0; j<n; j++){
			input>>a;
			ken.push_back(a);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int dwar=0, war=0;
		//Deceitful war
		vector <double> naomi2 (naomi.begin(), naomi.end());
		vector <double> ken2 (ken.begin(), ken.end());
				
		for(int j=0; j<n; j++)
		{
			if(naomi2.front()>ken2.front()){
				dwar++;
				naomi2.erase(naomi2.begin());
				ken2.erase(ken2.begin());
			}else{
				naomi2.erase(naomi2.begin());
				ken2.erase(ken2.end()-1);
			}
		}
		double x;
		//War
		
		for(int j=0; j<n; j++)
		{
			
			x=naomi.front();
			naomi.erase(naomi.begin());
			for(int k=0; k<ken.size(); k++){
				if(ken[k]>x){
					ken.erase(ken.begin()+k);
					break;
				}
				if(k==ken.size()-1 && ken[k]<x){
					war++;
					ken.erase(ken.begin());
				}
			}
							
		}
		myfile<<"Case #"<<i<<": ";	
		myfile << dwar << " " << war <<endl;
	}
	 myfile.close();
  input.close();
    return 0;
}
