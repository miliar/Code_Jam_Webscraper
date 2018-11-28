#include <algorithm>  
#include <iostream>  
#include <iomanip>  
#include <fstream>  
#include <sstream>  
#include <string>  
#include <list>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <cstring>  
using namespace std;  

#define MAX(a,b) (a>b)?a:b;
#define FOR(i,a,b) for(long i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  

typedef uint64_t Integer;
vector<Integer> numbers;

char buf[200];
string toString(Integer i, int base = 10)
{
    string result;
    Integer q;
    Integer r;
    int digits = 0;
    while (i)
    {
        q = i/base;
        r = i%base;
        string temp;
        buf[digits] = (char)('0' + r);
        ++digits;
        i=q;
    }
    buf[digits] = '\0';

    result= buf;
    reverse(result.begin(),result.end());
   
    if(result.empty())
        result = "0";

    return result;
}

bool isPalindrome(const string& s)
{
    string::const_iterator it1 = s.begin();
    string::const_iterator it2 = s.end();
    --it2;
    while(it1 < it2)
    {
        if(*it1 != *it2)
            return false;
        ++it1;
        --it2;
    }
    return true;
}

Integer base3to10(const string& s)
{
    Integer res = 0;
    int place = 1;
    for(string::const_reverse_iterator it = s.rbegin(); it != s.rend() ; ++it)
    {
        res += (place* (*it - '0'));
        place *= 10;
    }
    return res;
}

void populate()
{
    Integer i = 1;
    numbers.push_back(i);
    i = 4;
    numbers.push_back(i);
    i = 9;
    numbers.push_back(i);
    i = 3;
    while(1)
    {
        ++i;
        string str = toString(i, 3);
        if(!isPalindrome(str)) continue;
        Integer num = base3to10(str);
        Integer sq = num*num;
        if(sq > 100000000000000) break;
        if(!isPalindrome(toString(sq))) continue;
        numbers.push_back(sq);
        
    }
    for(vector<Integer>::iterator it = numbers.begin(); it != numbers.end(); ++it)
        cout << "pushing " << *it <<endl ;
}

int main(int argc, char** argv)
{
    populate();
    if(argc < 3)
    {
        cout << "Args\n";
        return 1;
    }
    ifstream in;
    cout << "Reading " << argv[1] << endl;
    cout << "Writing " << argv[2] << endl;
    in.open(argv[1],ios::in);
    ofstream out;
    out.open(argv[2],ios::out);
    int N = 0;
    in>>N;
    cout << " Total  " << N <<endl;
    REP(caseN,N)
    {
        Integer A,B;
        in >> A;
        in >> B;
        
        vector<Integer>::iterator lb = lower_bound(numbers.begin(), numbers.end(), A);
        vector<Integer>::iterator ub = upper_bound(numbers.begin(), numbers.end(), B);

        long count = ub - lb;
        
        out << "Case #"<<caseN+1<<": " << count;
        
        out << endl;
    }
        
    in.close();
    out.close();
    return 0;
}
