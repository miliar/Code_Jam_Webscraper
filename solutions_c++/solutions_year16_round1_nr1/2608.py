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
    int t,cc=1;
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
    
    int n;
    string s,ans;
    infile>>t;
    while(t--)
    {
        infile>>s;
        ans=s[0];
        for(int i=1;i<s.length();i++)
        {
            if(ans[0]<=s[i])
                ans=s[i]+ans;
            else
                ans+=s[i];
        }
        
        outfile<<"Case #"<<cc++<<": "<<ans<<endl;
      //  cout<<ans<<endl;
        
        
    }
   
    
    
   //         outfile<<"Case #"<<cc++<<": "<<f<<endl;
        //cout<<"Case #"<<cc++<<": "<<f<<endl;
   
    outfile.close();
    infile.close();
    return 0;
}
