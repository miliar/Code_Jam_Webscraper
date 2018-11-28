#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <map>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main() {

  int t;
  string N;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  string spellNum[] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
  for (int i = 1; i <= t; ++i) {
    cin >> (N) ;  // read n and then m.
    //cout << "Case #" << i << ": " << N << endl;
    //cout << word << endl;
    //cout << "Case #" << i << ": " << word << endl;
    // check for zero, check for one, etc.
    // then check for n-9
    string phoneNumber="";
    //cout << "current N:" << N << endl;
    int l = 0;
    string BackupN = N;
    phoneNumber="";
    N=BackupN;
    vector<int> currentNums;
    vector<string> phoneBefore;
    vector<string> Nbefore;
    for(int j =l ; j < 10;j++)
    {
        string currentNum = spellNum[j];
        bool found = true;
        string oldN = N;
        //cout << "current string: " << oldN <<endl;
        for(int k =0; k< currentNum.length();k++)
        {
            if (oldN.find(currentNum[k]) != std::string::npos) {
                //cout << "found "<< currentNum[k] << " in " << oldN <<endl;
                oldN.erase(oldN.find(currentNum[k]),1);
                continue;
            }
            else
            {
                //cout << "didn't find " << currentNum << " in " << oldN << endl; 
                found = false;
                break;
            }
        }
        if(found)
        {
            //cout << "found " << currentNum << " in " << N << endl;
            currentNums.push_back(j);
            phoneBefore.push_back(phoneNumber);
            Nbefore.push_back(N);
            phoneNumber+=to_string(j);
            j=j-1;
            N=oldN;
        }
    }
    if (N != "")
    {
        for(int PLUSTIME=1;PLUSTIME<10;PLUSTIME++)
        {
        bool flag=false;
        for(int p = currentNums.size() -1;p>=0;p--)
        {
            N=Nbefore[p];
            phoneNumber=phoneBefore[p];
            int startNum=currentNums[p] + PLUSTIME;
            for(int j =startNum ; j < 10;j++)
            {
                string currentNum = spellNum[j];
                bool found = true;
                string oldN = N;
                //cout << "current string: " << oldN <<endl;
                for(int k =0; k< currentNum.length();k++)
                {
                    if (oldN.find(currentNum[k]) != std::string::npos) {
                        //cout << "found "<< currentNum[k] << " in " << oldN <<endl;
                        oldN.erase(oldN.find(currentNum[k]),1);
                        continue;
                    }
                    else
                    {
                        //cout << "didn't find " << currentNum << " in " << oldN << endl; 
                        found = false;
                        break;
                    }
                }
                if(found)
                {
                    //cout << "found " << currentNum << " in " << N << endl;
                    phoneNumber+=to_string(j);
                    j=j-1;
                    N=oldN;
                }
            }
            if(N != "" ) continue;
            else 
            {
                flag=true;
                break;
            }
            //cout << "Case " << i << ": " << phoneNumber << endl;
        }
        if (flag) break;
        }
    
    }
    if (N=="") cout << "Case #" << i << ": " << phoneNumber << endl;
    else cout << "ERROR" << endl;
  }
}
