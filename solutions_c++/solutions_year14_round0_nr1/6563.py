#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  string line;
  int T; int find,find1,row1,row2,nope;
  string tab1[4]; string tab2[4]; 
  ifstream myfile ("A-small-attempt0.in");
  std::ofstream out("out.txt");
  std::streambuf *coutbuf = std::cout.rdbuf();
  std::cout.rdbuf(out.rdbuf());
  if (myfile.is_open())
  {
    myfile >> T;
    //cout << "number of case :" << T << endl;
    for(int k=0;k<T;k++)
    {
	    find=0;find1=0;
            myfile >> row1;
            //cout << "row" << row1<< endl;
            for (int i = 0; i < 4; i++) 
	    for (int j = 0; j < 4; j++) 
	    if(i==(row1-1))myfile >> tab1[j];
            else myfile >> nope;
            myfile >> row2;
            //cout << "row" << row2<< endl;
            for (int i = 0; i < 4; i++) 
	    for (int j = 0; j < 4; j++) 
	    if(i==(row2-1))myfile >> tab2[j];
            else myfile >> nope;
            // lines  

            for (int i = 0; i < 4; i++)
            {
		     for (int j = 0; j < 4; j++)
                    {
                      if(tab1[i]==tab2[j]){if(find!=0){find1=1;} find=i+1;}
                 
                    }
            } 

            if((find!=0) && (find1==1)){cout<<"Case #"<<k+1<<": Bad magician!" << endl;}
            else if(find!=0){cout<<"Case #"<<k+1<<": " << tab1[find-1] << endl;}
            else  {cout<<"Case #"<<k+1<<": Volunteer cheated!" << endl;}
     }
     myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
