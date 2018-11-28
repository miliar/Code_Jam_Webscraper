#include<iostream>
#include<cstring>
#include<algorithm>
#include<fstream>

using namespace std;

int main(){
     ofstream myfile;
     myfile.open("ovation.txt");
     int t;
     cin >> t;
     for (int j = 0; j < t; j++){
	  int p;
	  cin >> p;
	  string s;
	  cin >>  s;
	  long req = 0;
	  long standing = 0;
	  for (int i = 0; i <= p; i++) {
	       long zero = 0;
	       long diff = max(zero, i - standing);
	       req += diff;
	       // cout << i << " " << req << " " << standing << endl;
	       standing += int(s[i])-48 + diff;
	  }
	  myfile << "case #" << j+1 << ": " << req << endl;
     }
     myfile.close();
     return 1;
}
	       
	  

	  
     
