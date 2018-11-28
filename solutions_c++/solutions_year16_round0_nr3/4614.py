#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <map>
#include <cmath>
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

long getBaseNintepretation(string onesAndZeros, int base)
{
    long number = 0;
    int length = onesAndZeros.length();
    for(long i = 0; i < length; i++)
    {
        int binary = int(onesAndZeros[length-i-1] - '0');
        number += binary * pow(base, i);
    
    }
    return number;
}

long getSmallestFactor(long number)
{
    for(long i=2;i<=sqrt(number);i++)
    {
        if(number%i==0)
            return i;
    }
    return -1;  // case where the number is prime
}


int main() {
  long t;
  int N = 16;
  int J = 50;
    // need to generate all possible strings of length N-2
    // 2^(N-2) possible
   
  int strLength = N-2; 
  vector<string> permuPre;;
  for(int i = 0; i<= strLength ; i++ )
  {
    string testString="";
    for(int j=0;j<(strLength-i);j++)
    {
        testString+="0";
    }
    for(int j =0;j<i;j++)
    {
        testString+="1";
    }
    permuPre.push_back(testString);
  }
  
  vector<string> allPermus;
  
  for(int i =0; i< permuPre.size();i++)
  {
    string permuBase = permuPre[i];
    int len = permuBase.length();
    do {
        allPermus.push_back(permuBase);
    } while (next_permutation(permuBase.begin(), permuBase.end())); 
  }
  
  vector<string>        jamcoins;
  vector<vector<int> >  Allfactors;
  for(int i =0; i< allPermus.size();i++)
  {
    allPermus[i]="1"+allPermus[i]+"1";
    //cout << allPermus[i] << endl;
    string testString = allPermus[i];
    //cout << testString << endl;
    vector<int> factors;
    // get interpretations
    bool prime=false;
    for(int j =2; j<= 10;j++)
    {
        long interp = getBaseNintepretation(testString,j);
        int smallestFac=getSmallestFactor(interp);
        if (smallestFac == -1)
        {
            prime= true;
            break;
        }
        //cout << "interp: " << interp << " factor: " << smallestFac<< endl;
        factors.push_back(smallestFac);
    }
    if(prime) continue;

    // string is a jam coin!
    jamcoins.push_back(testString);
    Allfactors.push_back(factors);
    if(jamcoins.size() == J) break;
  }
  
  cout << "Case #1:" << endl;
  for(int i =0; i< J ;i++)
  {
    cout <<jamcoins [i];
    for (int j=0;j<Allfactors[0].size();j++)
    {
        cout << " " << Allfactors[i][j];
    }
    cout << endl;
  }
  
  string testString="1011001000000011";
  //cout << testString << endl;
  for(int j =2; j<= 10;j++)
    {
        int interp = getBaseNintepretation(testString,j);
        int smallestFac=getSmallestFactor(interp);
        if (smallestFac == -1)
        {
            //prime= true;
            break;
        }
        //cout << " base: "<<j<<" interp: " << interp << " factor: " << smallestFac<< endl;
        //cout << interp/2.0 << endl;
        //factors.push_back(smallestFac);
    }
  


  //string N;
  //cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  //for (int i = 1; i <= t; ++i) {
  //  cin >> (N) ;  // read n and then m.
  //  cout << "Case #" << i << ": " << count << endl;
  //}
}
