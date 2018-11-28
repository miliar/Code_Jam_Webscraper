#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <M_APM.H>

using namespace std;

map<MAPM,MAPM> sqrts;
set<MAPM> fairSquares;
set<MAPM> palindromes;

bool isPalindrome(const MAPM bigNum){
    if(palindromes.find(bigNum) != palindromes.end())
        return true;

    char iobuf[102];

    bigNum.toIntegerString(iobuf);

    string bigNumStr(iobuf);
    //string::const_iterator fwd = bigNumStr.begin(); 
    //string::const_reverse_iterator rev = bigNumStr.rbegin();
    //while(fwd >= rev.base()){
    //    if(*fwd != *rev)
    //            return false;
    //    ++fwd; --rev;
    //}
    if( equal(bigNumStr.begin(), bigNumStr.begin() + bigNumStr.size()/2, bigNumStr.rbegin()) ){
        palindromes.insert(bigNum);
        //cout << "Adding palindrome : " << bigNumStr << endl;
        return true;
    }
    else
        return false;
}

int main(){

    int numTests;

    cin >> numTests;

    vector<int> results(numTests);

    for(int i = 0; i < numTests; ++i){
        string lower, higher;
        cin >> lower >> higher;
        const MAPM lowerLimit = MAPM(lower.c_str());
        const MAPM higherLimit = MAPM(higher.c_str())+1;
        MAPM current = lowerLimit;
        
        while(current < higherLimit){
            if(fairSquares.find(current) != fairSquares.end()){
                //char obuf[102];
                //current.toIntegerString(obuf);
                //cout << "Adding fair sqaure number : " << obuf << endl;
                results[i]++;
            }
            else if(isPalindrome(current)){
                MAPM sqrtCurrent = 0;
                map<MAPM,MAPM>::const_iterator it = sqrts.find(current);
                if(it != sqrts.end())
                    sqrtCurrent = it->second;
                else {
                    sqrtCurrent = current.sqrt();
                    sqrts.insert(make_pair(current, sqrtCurrent));
                }
                
                if((sqrtCurrent.is_integer() && isPalindrome(sqrtCurrent))){
                    fairSquares.insert(current);
                    //char obuf[102];
                    //current.toIntegerString(obuf);
                    //cout << "Adding fair sqaure number : " << obuf << endl;
                    results[i]++;
                }
            } 
            ++current;
        }

    }

    for(int i = 0; i < numTests; ++i){
        cout << "Case #" << i+1 << ": " << results[i] << endl;
    }

    return 0;
}
