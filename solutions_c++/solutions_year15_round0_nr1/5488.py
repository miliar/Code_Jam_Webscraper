#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    ifstream in;
    in.open("A-small-attempt0.txt");
    ofstream out;
    out.open("output.txt");
    int t;
    in>>t;
    for(int j=0; j<t; j++)
    {
        int max;
        in>>max;
        string s;
        in>>s;
        int c=0,count=0;
        for(int i=0; i<s.size(); i++)
        {
            int n=s[i]-'0';
            if(n>0)
                if(i>c)
                    {count+=i-c;c+=i-c;}
            c+=n;
        }
        out<<"Case #"<<j+1<<": "<<count<<endl;
    }
    return 0;
}
// END KAWIGIEDIT TESTING
