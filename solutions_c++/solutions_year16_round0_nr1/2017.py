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
    int t,n,cc=1,mask;
    int seen,temp;
    long long ans,f;
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
    mask=1023;
   
    infile >> t;
    bool flag;
    while(t--)
    {
        infile>>n;
        if(n==0)
        {
            outfile<<"Case #"<<cc++<<": "<<"INSOMNIA"<<endl;
          //  cout<<"Case #"<<cc++<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        seen=0;
        temp=110;
        ans=n;
        while(temp--)
        {
            f=ans;
            while(f!=0)
            {
                seen =seen | (1<<(f%10));
                f=f/10;
            }
            if(seen == mask)
                break;
            ans+=n;
            
        }
       
         if(seen==mask)
         {outfile<<"Case #"<<cc++<<": "<<ans<<endl;
           //  cout<<"Case #"<<cc++<<": "<<ans<<endl;
         }
        
        else
        {  outfile<<"Case #"<<cc++<<": "<<"INSOMNIA"<<endl;
          //cout<<"Case #"<<cc++<<": "<<"INSOMNIA"<<endl;
        }
        
    }
    outfile.close();
    infile.close();
    return 0;
}
