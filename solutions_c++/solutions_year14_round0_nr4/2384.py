#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <iomanip>
#include <utility>
#include <algorithm>
using namespace std;



//ifstream fin ("test.in");
//ofstream fout ("test.out");

ifstream fin ("D-large.in");
ofstream fout ("D-large.out");

int t;
int n;

float nao[1000];
float ke[1000];

vector <float> naomi;
vector <float> ken;

vector <float> naomidw;
vector <float> kendw;


int war(){
	int nw = 0;
	int kw = 0;
	
	bool found = false;
	for(int i = n-1; i>= 0; i--){
		for (int j = 0; j < ken.size(); j++){
			if ( ken[j] > naomi[i] )
			{
				kw++;
				//cout<<"erasing "<<ken[j]<<" "<<naomi[i]<<endl;
				ken.erase(ken.begin() + j);
				naomi.erase(naomi.begin() + i);	
				found = true;
				break;
			}
		}
			
		if(!found){
			//cout<<"erasing "<<ken[0]<<" "<<naomi[i]<<endl;
			ken.erase(ken.begin());
			naomi.erase(naomi.begin() + i);
			
			nw++;
		}
		found = false;
	}
	
	//cout << "naomi wins: "<<nw<<" while ken wins: "<<kw<<endl;
	return nw;

}

int decwar(){
	int nw = 0;
	int naomiminmax;
	float fake;
	bool won;
	
	int z = kendw[kendw.size()-1];
	for ( int i = 0; i < naomidw.size(); i++){
		for ( int j = 0; j < naomidw.size(); j++)
		{
			if ( naomidw.size() == 1)
			{
				if(naomidw[0] > kendw[0])
					nw++;
				
				return nw;
			}
			
			if ( naomidw[i] > kendw[j]){
				naomidw.erase(naomidw.begin() + i);
				kendw.erase(kendw.begin() + j);
				nw++;
				i--;
				break;
			}
		}	
	}
	
	return nw;
}


int main() { 
	fin >> t;
	
	float temp ; 
	for (int i = 0; i < t; i++){
		fin >> n;
		for ( int j = 0; j < n; j++){
			fin >> nao[j];
			naomi.push_back(nao[j]);
		}
		//cout << endl;
		
		
		for ( int j = 0; j < n; j++){
			fin >> ke[j];
			ken.push_back(ke[j]);
		}

		sort(ken.begin(),ken.end());
		sort(naomi.begin(),naomi.end());
		
		for ( int j = 0; j < ken.size(); j++){
			kendw.push_back(ken[j]);
			naomidw.push_back(naomi[j]);
		}
		
		fout<<"Case #"<<i+1<<": "<<decwar()<<" "<<war()<<endl;
		
		naomi.clear();
		naomidw.clear();
		ken.clear();
		kendw.clear();
	}
	
	return 0;
}
