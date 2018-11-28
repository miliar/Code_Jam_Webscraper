#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

vector<string> substrings (string line)
{
	vector<string> ceva;	
	istringstream iss(line);
	while (iss)
	 {
	     string sub;
		    iss >> sub;
			if (sub.length()==0) break;
			ceva.push_back(sub);
		    //cout << "Substring: " << sub << endl;
	  };
		 return ceva;
}

int main()
{
	vector<string> woop;
	string line;
	int value;
	int min;
  ifstream myfile ("A-small-attempt0.in");
  ofstream output ("output.txt");

  if (myfile.is_open()) getline(myfile,line);
  string bla = line;
  istringstream buffer(line);
  buffer >> value;
  //cout << value << "\n" ;

  int i;
  if (myfile.is_open())
  {
	  
	  for (i=0; i<value; i++) {
		int sum=0;
	  getline (myfile,line);
      //cout << line << '\n';
	  woop = substrings(line);
	  min = 0;
	  for (int j=0; j<woop[0][0]-'0'+1; j++)
	  {
		  int x =  woop[1][j]-'0';
		  //cout << x << " " << sum << "\n";
		  if ((sum<j) && (j-sum>min)) min = j-sum; /*cout << " ||minimul nou e " << min << " || ";}*/
		  sum=sum+x;
	  }
	  output << "Case #" << i+1 << ": " << min << "\n";
    }
    myfile.close();
  }
  else cout << "Unable to open file"; 

  output.close();

  //cout << woop[1][0]-'0' << endl;
}


