#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main()
    {
//--+-
int t;
cin>>t;
    int j=1;
while(t--)
    {
   string s;
    cin>>s;
    int count=0;
    int l=s.length();
    char g=s[0];
    for(int i=1;i<l;i++)
        {
        if(s[i]!=g)
            {
            g=s[i];
            count++;
        }
    }
    if(g=='-')
        count++;
    cout<<"Case #"<<j<<": "<<count<<endl;
    j++;
}
    return 0;
}
    
