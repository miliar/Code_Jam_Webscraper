#include<iostream>
#include<cmath>
#include <set>
#include <vector>
#include <fstream>
#include <string>
using namespace std;
int main (){
	ifstream fin ("B-large.in");
	ofstream fout ("out.txt");
    int t,test,i,lenght;
    fin >> t;
    string s;
    for (test=1;test<=t;test++) {
    	//no skill only luck...
		fin >> s;
		lenght = 0;
		for (i=0;i<s.size();i++){
			//cout << "lenght=" << lenght << endl;
			while(s[i] == s[i+1]){
				i++;
				//cout << "i=" << i << endl;
			}
			lenght++;		
		}
		if(s[s.size()-1]=='-')
			fout << "Case #" << test << ": " << lenght << endl;
		else{
			fout << "Case #" << test << ": " << lenght-1 << endl;
		}
	}
    
    
    return 0;
}
































































/////////kek\\\\\\\\\
