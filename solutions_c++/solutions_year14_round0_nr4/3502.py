#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
using namespace std;
/*
void print(vector<double> &s){
	for(int i=0; i<s.size(); i++){
		cout << s[i] << " ";
	}
	cout << endl;
}
*/
int decieve(vector<double> nomi, vector<double> ken){
	for(int i=0; i<nomi.size(); i++){
		if(nomi[i]<ken[i]){
			nomi.erase(nomi.begin());
			ken.erase(ken.begin()+(ken.size()-1));			
			i=-1;
		}
	}
	return nomi.size();
}
int war(vector<double> nomi, vector<double> ken){
	for(int i=0; i<nomi.size(); i++){
		for(int j=0; j<ken.size(); j++){
			if(nomi[i]<ken[j]){
				ken.erase(ken.begin()+j);
				break;
			}
		}
	}
	return ken.size();
}
main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");
//	ofstream f("input2.txt");
	
	int time;
	fin >> time;
//	f << time << endl;
	for(int c=1; c<=time; c++){
		int size;
		fin >> size;
//		f << size << endl;
		vector<double> nomi, ken;
		for(int i=0; i<size; i++){
			double no;
			fin >> no;
		//	f << no<<" ";
			nomi.push_back(no);
		}
//		f << endl;
		for(int i=0; i<size; i++){
			double no;
			fin >> no;
			//f << no<<" ";
			ken.push_back(no);
		}
//		f << endl;
		sort(nomi.begin(), nomi.end());
		sort(ken.begin(), ken.end());
		fout << "Case #"<< c << ": ";
		int w=war(nomi, ken);
		fout << decieve(nomi, ken)<<" "<< w << endl;
	}
}
