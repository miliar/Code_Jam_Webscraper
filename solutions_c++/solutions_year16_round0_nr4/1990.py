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
vector<int> v;
vector<long long > ans;
int main(void)
{
    int k,c,s,t,tc,i,cc=1;
    long long temp;
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
    

    infile>>t;
    while(t--)
    {
        infile>>k>>c>>s;
        if(k==1)
        {
            outfile<<"Case #"<<cc++<<": "<<(s>=1?"1":"IMPOSSIBLE")<<endl;
            continue;
        }
        v.clear();ans.clear();
        v.pb(1);v.pb(0);
        for(int i=2;i<k;i++)
            v.pb(i);
        i=0;
        
        while(i<v.size())
        {
          temp=0;
          tc=c;
          while(tc-- && i<v.size())
          {
            temp=temp*k+v[i++];
          }
            ans.pb(temp);
        }
        if(s<ans.size())
        { outfile<<"Case #"<<cc++<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        outfile<<"Case #"<<cc++<<": ";
        for(int i=0;i<ans.size();i++)
            outfile<<ans[i]+1<<" ";
        outfile<<"\n";
        
        
    }
    
   //         outfile<<"Case #"<<cc++<<": "<<f<<endl;
        //cout<<"Case #"<<cc++<<": "<<f<<endl;
   
    outfile.close();
    infile.close();
    return 0;
}
