#include <fstream>
#include <iostream>
#include <string>
#include <set>
using namespace std;
bool hasnConsonants(
    std::string::const_iterator beg, 
    std::string::const_iterator & end, 
    int length, int n)
{
    int cnt =0;
    bool prevCon(false);
    for(;beg!=end && cnt<n ;++beg)
    {
        if(*beg == 'a' ||
            *beg == 'e' ||
            *beg == 'i' ||
            *beg == 'o' ||
            *beg == 'u')
        {
            prevCon = false;
            cnt = 0;
        }
        else
        {
            if(prevCon)
            {
                prevCon=true;
                cnt++;
            }
            else
            {
                prevCon=true;
                cnt = 1;
            }
        }
    }
    if(cnt >= n)
    {
        return true;
    }
    return false;
}
void printChars(std::string::const_iterator beg, std::string::const_iterator endBeg)
{
    for(;beg!=endBeg; ++beg)
    {
        cout << *beg;
    }
    std::cout << std::endl;
}

int getNRank(std::string const & input, int n)
{
    int cnt = 0;
    int leng = input.length();
    for(int subLen = leng-1; subLen>=n-1; --subLen)
    {
        std::string::const_iterator beg(input.begin());
        std::string::const_iterator endBeg(beg+subLen);        
        for(; endBeg!=input.end(); ++beg)
        {
            ++endBeg;
            //printChars(beg, endBeg);
            if(hasnConsonants(beg, endBeg, subLen, n))
            {
                ++cnt;
            }
        }

    }

    //hasnConsonants(string, n);
    return cnt;
}

int main()
{
   std::string input;
   int numberOfconsonants;
   int numberOfTC;
   cin >> numberOfTC;
   for(int k=1; k<=numberOfTC; ++k)
   {
       cin >> input;
       cin >> numberOfconsonants;
       cout << "Case #" << k << ": " << getNRank(input,numberOfconsonants) << std::endl;
   }
   return 0;
}

