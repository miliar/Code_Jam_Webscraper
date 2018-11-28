#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("inputl.txt","r",stdin);
    freopen("outputl.txt","w",stdout);
    int t,i,j,counter;
    string s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s;
        counter = 0;
        for(j=0;j<s.length()-1;j++)
            if(s[j]!=s[j+1])
                counter++;

        if(s[s.length()-1]=='-')
            counter++;

        cout<<"Case #"<<i<<": "<<counter<<endl;
    }
    return 0;
}
