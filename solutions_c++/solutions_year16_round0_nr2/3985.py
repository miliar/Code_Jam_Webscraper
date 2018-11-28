#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <fstream>
using namespace std;

int getval(char a)
{
    if(a=='-')
        return 0;
    else
        return 1;
}

int rev(int a)
{
    if(a==0)
        return 1;
    else
        return 0;
}

int main()
{
    ifstream input;
    ofstream output;
    input.open("input.txt");
    output.open("output.txt");
    
    int t;
    input>>t;
    
    for(int i=1 ; i<=t ; i++)
    {
        string s;
        input>>s;
        int len=s.size();
        int state;
        int ans=0;
        if(s[0]=='-')
            state=0;
        else
            state=1;
        int j=1;
        while(j<len || state==0)
        {
            if(getval(s[j])==state)
            {
                j++;
                continue;
            }
            else
            {
                ans++;
                state=rev(state);
            }
        }
        output<<"Case #"<<i<<": "<<ans<<endl;
    }
    output.close();
    input.close();
    return 0;
} 
