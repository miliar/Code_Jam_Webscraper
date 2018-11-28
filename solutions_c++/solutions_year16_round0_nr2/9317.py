#include<stdio.h>
#include<fstream>
#include<iostream>
#include<string>
#include<sstream>
#include<array>

using namespace std;

int main()
{
    char filename[32];
    int i, j, k;
    int n = 0;
   
    
    
    cin >> filename;
    ifstream in(filename);
    ofstream out("B_large.out");
    string s, t;
    stringstream iss;
    
    getline(in, s);
    int noc = stoi(s);
    cout << "number of cases: " << noc << endl;
    

    for(int i = 0; i < noc; i++){
	
	getline(in, s);
	s = s + '+';
	for(j=0; j<s.size()-1; j++){
	  if(s[j] != s[j+1])
	    n = n + 1;
	}
	
	
	
	cout << n << endl;
	
	out << "Case #" << i+1 << ": " << n << endl;
	
	n = 0;
	  
	
    }

 
    return 0;
}

