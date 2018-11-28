#include <iostream>
#include <fstream>
#include <string>
#include<stdio.h>
#include<stdlib.h>
#include <vector>

using namespace std;

int main () {
	int T;
	int it;
	int flips, firstMinus;
	string S;
	int i;
	
	string line;
	
	// ifstream in ("input.txt");
	ifstream in ("B-large.in");
	if(!in.is_open()){
		cout << "Unable to open file"<<endl; 
		system("pause");
        return 0;
	}
	// ofstream out("output.txt", ios::out);
    ofstream out("B-large.out", ios::out);
	
	getline (in,line);
    T=atoi(line.c_str());
    for(it=1;it<=T;it++){
        getline(in,line);
        S=line;
        // cout<<S<<endl;
        flips=0;
        firstMinus=-1;
        
        for(i = (S.length()-1); i>=0; i--) {
            if(S[i]=='-'){
                firstMinus=i;
				flips++;
				break;
			}
        }
        
		for(i = firstMinus; i>0; i--) {
            if(S[i]!=S[i-1]){
				flips++;
			}
		}
        
        out<<"Case #"<<it<<": "<<flips<<endl;
    }
    
	in.close();
    out.close();

    // system("pause");
	return 1;
}
