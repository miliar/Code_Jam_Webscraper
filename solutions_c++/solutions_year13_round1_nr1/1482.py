#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A.txt");
    ofstream out("A_out.txt");
    int po=0;
    in>>po;
    for(int co=0;co<po;co++)
    {
        long long int r,t;
        in>>r>>t;
        long long int ans=0;
        long long int temp=0;
        for(long long int h=(r+1)*2-1;temp<=t;h=h+4)
        {
            if(temp+h>t) break;
            else if(temp+h<=t)
            {
                temp=temp+h;
                ans++;
            }
        }
        out<<"Case #"<<co+1<<": "<<ans<<endl;
    }
    return 0;
}
            
