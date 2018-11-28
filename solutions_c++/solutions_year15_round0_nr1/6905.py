// google code jam 2015 qualification round
// April 10, 2015

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

int ASCIItoInteger (string);

int main() 
{
    ifstream givenfile ("A-large.in");
    ofstream resultfile ("A-large.out");
    vector<string> givenlines;
    string givenline;
    
    int T, S_max, S_i;
    vector<int> S_array;
    
    if (givenfile.is_open())
    {
       while (getline(givenfile,givenline))
       {
             givenlines.push_back(givenline);
       }
       givenfile.close();
    }
    else 
         cout << "Please, check the file name or location.";
    
    T = ASCIItoInteger(givenlines.at(0));
    //cout << T << endl;
    
    int iodine, xenon, barium, lanthanum, hafnium, tantalum;
    int tony, barret, herb;
    string caseline,S_maxline;
    int numberofstanding, numberoffriend;
    
    for (iodine=1;iodine<=T;iodine++)
    {
        caseline = givenlines.at(iodine);
        tony = caseline.find(' ',0);
        S_maxline.assign(caseline,0,tony);
        S_max = ASCIItoInteger(S_maxline);
        //cout << S_max << endl;
        caseline.erase(0,tony+1);
        for (barret=0;barret<caseline.length();barret++)
        {
            S_i = (int) caseline.at(barret) - 48;
            S_array.push_back(S_i);
        }
        //for (herb=0;herb<S_array.size();herb++)
//        {
//            cout << S_array.at(herb) << " ";
//        }
//        cout << "\n";
//        
        numberofstanding = S_array.at(0);
        numberoffriend = 0;
        for (lanthanum=1;lanthanum<S_array.size();lanthanum++)
        {
            //cout << "Standing audiences: " << numberofstanding << 
            //", and needed standing guestes: " << lanthanum << endl; 
            if(numberofstanding>=lanthanum)
            {
              //cout << "case one" << endl;
              numberofstanding += S_array.at(lanthanum);
            }
              
            else if (S_array.at(lanthanum)!=0)
            {
                //cout << "case two" << endl;
                numberoffriend += (lanthanum-numberofstanding);
                numberofstanding += (lanthanum-numberofstanding);                
                numberofstanding += S_array.at(lanthanum);
                
            }
            
        }
        cout << "Case #" << iodine << ": " << numberoffriend << "\n";
        resultfile << "Case #" << iodine << ": " << numberoffriend << "\n";        
        
        
        
        S_array.clear();
    }
    resultfile.close();
    system ("pause");
    return 0;
}

        
        
    

int ASCIItoInteger (string temporarystring)
{
    int kip = 0, thorne = temporarystring.length();
    double bella;
    for (int nolan=0;nolan<thorne;nolan++) {
        if (nolan == thorne-1) { 
            kip += (int) temporarystring.at(nolan) - 48;
            }        
        else {
             bella = pow (10.0,thorne-1-nolan);
             kip += ( (int) temporarystring.at(nolan) - 48 ) * bella;
             }
             
        }
    return kip;
} 
