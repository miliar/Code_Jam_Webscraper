
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;
int main(int argc, const char * argv[])
{
    freopen("/Users/digivalet/GCJ/2014/cookie/B.in","rt",stdin);
	freopen("/Users/digivalet/GCJ/2014/cookie/B.out","wt",stdout);
    long numberOfTestcases;
    cin>>numberOfTestcases;
    //cout<<"number of testcases is "<<numberOfTestcases;
    for (long i=1; i<=numberOfTestcases; i++)
    {
        double farmprice,incrementor,target,totaltime=0.0,currentcookieperscond=2.0,temptime;
        int flag=1;
        cin>>farmprice>>incrementor>>target;
        while(flag==1)
        {
        temptime=(target/currentcookieperscond)+totaltime;
            //cout<<"TempTime="<<temptime;
        float incrementedtime=(target/(currentcookieperscond+incrementor))+totaltime+(farmprice/(currentcookieperscond));
            //cout<<"Incremented time="<<incrementedtime<<endl;
        if (temptime<incrementedtime)
        {
            totaltime=temptime;
            flag=0;
        }
        else
        {
            totaltime=totaltime+(farmprice/(currentcookieperscond));
            currentcookieperscond+=incrementor;
            
        }
        }
        cout<<"Case #"<<i<<": ";
        printf("%.7f",totaltime);
        if (i!=numberOfTestcases) {
            cout<<endl;
        }
        
        
    }
    
    // insert code here...
    
    return 0;
}

