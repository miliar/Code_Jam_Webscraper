#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

using namespace std;

vector <int> positions;
	
string write_result (unsigned int K, unsigned int C, unsigned int S)
{
    stringstream stream_;
    for (unsigned i = 1; i <= K; i++)
    {
	stream_ << " " << i;
    }	
    return stream_.str();	
}


int main (int argc, char* argv[])
{
   unsigned int n; 
   cin >> n;
   for (unsigned int i=0;i<n;i++)  
   { 
      unsigned int K = 0;
      cin >> K;
      unsigned int C = 0;
      cin >> C;
      unsigned int S = 0;
      cin >> S; 
	  
       string result =write_result (K, C, S);
      cout << "Case #"<< i+1 <<":" << " " << result << endl;
   }

}   

