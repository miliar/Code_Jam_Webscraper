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
    
    int t,d[10],a[27],cc=1;
    string s,ans;
    infile >> t;
    cout<<t<<endl;
    while(t--)
    {
        infile>>s;
        cout<<s<<endl;
        for(int i=0;i<10;i++)
            d[i]=0;
        for(int i=0;i<27;i++)
            a[i]=0;
        for(int i=0;i<s.length();i++)
        {
            a[s[i]-'A']++;
        }
        while(a['Z'-'A']!=0)
        {
            d[0]++;
            a['Z'-'A']--;
            a['E'-'A']--;
            a['R'-'A']--;
            a['O'-'A']--;
            
        }
        while(a['W'-'A']!=0)
        {
            d[2]++;
            a['T'-'A']--;
            a['W'-'A']--;
            a['O'-'A']--;
        }
        while(a['X'-'A']!=0)
        {
            d[6]++;
            a['S'-'A']--;
            a['I'-'A']--;
            a['X'-'A']--;
        }
        while(a['G'-'A']!=0)
        {
            d[8]++;
            a['E'-'A']--;
            a['I'-'A']--;
            a['G'-'A']--;
            a['H'-'A']--;
            a['T'-'A']--;
        }
        while(a['U'-'A']!=0)
        {
            d[4]++;
            a['F'-'A']--;
            a['O'-'A']--;
            a['U'-'A']--;
            a['R'-'A']--;
            
        }
        while(a['O'-'A']!=0)
        {
            d[1]++;
            a['O'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
        }
        while(a['R'-'A']!=0)
        {
            d[3]++;
            a['T'-'A']--;
            a['H'-'A']--;
            a['R'-'A']--;
            a['E'-'A']--;
            a['E'-'A']--;
        }
        while(a['F'-'A']!=0)
        {
            d[5]++;
            a['F'-'A']--;
            a['I'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
            
        }
        while(a['S'-'A']!=0)
        {
            d[7]++;
            a['S'-'A']--;
            a['E'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
            a['N'-'A']--;
        }
        while(a['N'-'A']!=0)
        {
            d[9]++;
            a['N'-'A']--;
            a['I'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
        }
       ans="";
        for(int i=0;i<10;i++)
        {
            while(d[i]!=0)
            { ans+='0'+i;
                d[i]--;
            }
        }
 
        cout<<ans<<endl;
        outfile<<"Case #"<<cc++<<": "<<ans<<endl;
   }
    outfile.close();
    infile.close();
    return 0;
}
