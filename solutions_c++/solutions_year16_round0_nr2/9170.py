#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main()
    {
int n;
cin>>n;
    int j=1;
while(n--)
    {
   string s;
    cin>>s;
    int count=0;
    int l=s.length();
    char t=s[0];
    for(int i=1;i<l;i++)
        {
        if(s[i]!=t)
            {
            t=s[i];
            count++;
        }
    }
    if(t=='-')
        count++;
    cout<<"Case #"<<j<<": "<<count<<endl;
    j++;
}
    return 0;
}
    
