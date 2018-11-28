#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        string s;
        cin>>s;
        int l = s.length();
        int flips = 0,i = 0;
        /*Case 1: initial seq of '-' */
        if(s[i] == '-' )
        {
            flips = 1;
            i++;
            while(s[i] == '-' && i != l)
                i++;
        }
        /*Case 2: seq of '-' after any '+'*/
        while( i != l)
        {
            while(s[i] == '+' && i != l)
                i++;
            if(s[i] == '-')
            {
                flips += 2;
                while(s[i] == '-' && i != l)
                    i++;
            }  
        }
        cout<<"Case #"<<t<<": "<<flips<<endl;
    }
}
