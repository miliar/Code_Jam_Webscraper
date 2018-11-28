#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
#include <vector>
using namespace std;
main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");	
	
	int time;
	fin >> time;
	string str;
	for(int c=1; c<=time; c++){
		int size;
		fin >>size;
		string a, b;
		getline(fin, str);
		getline(fin, a);
		getline(fin, b);
		int i=0, count=0;
		fout << "Case #"<<c<<": ";
		bool run=true;
		while(1){
			if(i<a.size() || i<b.size()){
				if(i<a.size() && i<b.size() &&a[i]==b[i]){
					i++;
					
				}
				else if(i!=0 &&  i<b.size() && a[i-1]==b[i]){
					a.insert(i-1,1, b[i]);
					count++;
				}
				else if(i!=0  &&i<a.size()&& a[i]==b[i-1]){
					b.insert(i-1,1, a[i]);
					count++;
				}
				else{
					fout << "Fegla Won" << endl;
					run=false;
					break;
				}
			}
			else{
				break;
			}
		}
		if(run){
			fout << count << endl;
		}
	}
}

