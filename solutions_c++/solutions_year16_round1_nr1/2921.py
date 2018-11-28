#include <iostream>
#include <stdio.h>
#include <vector>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <fstream>
#include <string.h>
#include <stdlib.h>
#include <bitset>

using namespace std;

int main()
{
    ifstream input;
    ofstream output;
    input.open("input.txt");
    output.open("output.txt");
    int T;
    input>>T;
    for(int t=1 ; t<=T ; t++)
    {
        string a;
        input>>a;
        string ans;
        ans = ans+a[0];
        char last = a[0];
        for(int i=1 ; i<a.size() ; i++)
        {
            if(a[i]>=last)
            {
                ans=a[i]+ans;
                last = a[i];
            }
            else
                ans=ans+a[i];
            
        }
        output<<"Case #"<<t<<":"<<ans<<endl;
        
    }
    output.close();
    input.close();
    return 0;
}