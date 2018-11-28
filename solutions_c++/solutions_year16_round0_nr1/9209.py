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
    int nv = 0;
    int count = 0;
    array<int, 10> d;
    
    
    cin >> filename;
    ifstream in(filename);
    ofstream out("A_large.out");
    string s, t;
    stringstream iss;
    
    getline(in, s);
    int noc = stoi(s);
    cout << "lines " << noc << endl;
    

    for(int i = 0; i < noc; i++){
	
	
	for(j=0;j<10;j++){
	  d[j] = 0;
	}
      
      
	getline(in, s);
	n = stoi(s);
	cout << n << endl;
	nv = n;
	if (n == 0){
	  out << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
	  continue;
	}
	
	while(d[0]*d[1]*d[2]*d[3]*d[4]*d[5]*d[6]*d[7]*d[8]*d[9] == 0){
	  count = count + 1;
	  nv = count * n;
	  cout << "nv :" << nv << endl;
	  while(nv!=0){
	    k = nv % 10;
	    d[k] = 1;
	    cout << "d: " << k << endl;
	    nv = nv / 10;
	  }
	}
	out << "Case #" << i+1 << ": " << count*n<< endl;
	//cout << "Case #" << i+1 << ": " << count*n << endl;
	count = 0;
	  
	
    }

 
    return 0;
}

