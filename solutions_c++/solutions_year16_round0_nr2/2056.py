#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <cassert>
#include <iostream>

#define pb push_back
#define mk make_pair
#define F first
#define S second
#define MOD 1000000007
using namespace std;
int main(void)
{
    int t,f,st,cc=1;
    string s;
    ifstream infile;
    infile.open("in.txt");
    if (!infile)
    {
        // Print an error and exit
        cerr << "Uh oh, Sample.dat could not be opened for reading!" << endl;
        exit(1);
    }
    
    ofstream outfile;
    outfile.open("out.txt");
   
   
    infile >> t;
    while(t--)
    {
        f=0;
        infile>>s;
        //cout<<s<<endl;
        st=(s[0]=='-'?1:0);
        for(int i=1;i<s.length();i++)
        {
            if(s[i]==s[i-1])
                continue;
            f++;
            st=(s[i]=='-'?1:0);
        }
        f+=st;
        outfile<<"Case #"<<cc++<<": "<<f<<endl;
        //cout<<"Case #"<<cc++<<": "<<f<<endl;
        
    }
    outfile.close();
    infile.close();
    return 0;
}
