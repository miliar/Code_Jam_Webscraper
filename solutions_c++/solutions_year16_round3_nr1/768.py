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
int main(void)
{
    int t,n,cc=1,acc,x,mx,a,b;
    
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
    
    string s;
    infile >> t;
    while(t--)
    {
        infile>>n;
        s="";
        v.clear();
        acc=0;
        for(int i=0;i<n;i++)
        {
            infile>>x;
            v.pb(x);
            acc+=x;
        }
        while(true)
        {
            mx=0;
            a=-1;b=-1;
            for(int i=0;i<n;i++)
            {
                if(v[i]>mx)
                  { mx=v[i];
                      a=i;
                      b=-1;
                  }
                else if(v[i]==mx)
                { b=i;}
            }
            if(a==-1)
                break;
            printf("%d %d\n",a,b);
            s+='A'+a;
            v[a]--;
            acc--;
            if(b!=-1 && acc-1!=1)
            { s+='A'+b;
                v[b]--;
                acc--;
            }
            s+=" ";
        }
        
        
      outfile<<"Case #"<<cc++<<": "<<s<<endl;
       //cout<<"Case #"<<cc++<<": "<<s<<endl;

    }
                    
    outfile.close();
    infile.close();
    return 0;
}

