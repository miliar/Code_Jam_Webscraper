

#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;


int main(int argc, const char * argv[]) {
   freopen("/Users/sangwoo/Desktop/cpp/cpp/input","r",stdin);
   freopen("/Users/sangwoo/Desktop/cpp/cpp/output","w",stdout);
    
    int tt;
    
    cin >> tt;
    for(int t=1;t<=tt;t++)
    {
        string inp,outp;
        
        cin >> inp;
        
        outp+=inp[0];
        
        for(int j=1;j<inp.length();j++)
        {
            if(outp[0]>inp[j])
            {
                outp = outp + inp[j];
            }
            else{
                outp = inp[j] + outp;
            }
        }
        cout<<"Case #" << t << ": " << outp<<endl;
        
    }
    
    
    

    return 0;
}