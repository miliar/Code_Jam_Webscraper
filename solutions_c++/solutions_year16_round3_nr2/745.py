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
    int t,b,cc=1;
    long long m;
    
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
    string s="";
    long long temp;
    while(t--)
    {
        infile>>b;
        infile>>m;
        temp=1;
        temp=temp<<(b-2);
        //cout<<temp<<endl<<m<<endl;
        if(m>temp)
        {
           outfile<<"Case #"<<cc++<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        s="0";
        temp=temp>>1;
        m-=1;
        for(int i=0;i<b-2;i++)
        {
            if(m&temp)
             s+="1";
            else
             s+="0";
            
            temp=temp>>1;
        }
        s+="1";
        outfile<<"Case #"<<cc++<<": "<<"POSSIBLE"<<endl;
        outfile<<s<<endl;
        
        for(int i=1;i<b;i++)
        {
            s="";
            for(int j=0;j<=i;j++)
                s+="0";
            for(int j=i+1;j<b;j++)
                s+="1";
            outfile<<s<<endl;
        }
        
       
    }
                    
    outfile.close();
    infile.close();
    return 0;
}

