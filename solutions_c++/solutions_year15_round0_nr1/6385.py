#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  string line;
  int T; int Smax;
  ifstream myfile ("A-large.in");
  std::ofstream out("out.txt");
  std::streambuf *coutbuf = std::cout.rdbuf();
  std::cout.rdbuf(out.rdbuf());
  if (myfile.is_open())
  {
    myfile >> T;
    //cout << "T:" << T << endl;
    for(int k=0;k<T;k++)
    {
	    myfile >> Smax;
            //cout << "Smax:" << Smax << endl;
            string S;
	    myfile >> S;
            int N=0; int sum=0;
            for (int i = 0; i <= Smax; i++)
            {  
               //cout << "#i " << i <<": sum " << sum <<": N " << N ;
               if (sum<i) {N=N+(i-sum); sum=i+(int)S[i]-48;}
               else sum=sum+(int)S[i]-48;
            } 
            //cout << endl;
            cout << "Case #" << k+1 <<": " << N << endl;
     }
     myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
