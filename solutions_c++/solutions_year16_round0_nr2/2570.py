#include <string>
#include <map>
#include <sstream>
#include<vector>
#include<iostream>
using namespace std;


int main()
{

    int t,ti;

    cin>>t;
    ti=t;

    for(; t>0; t--)
    {
        string s;
        cin>>s;
        int n=0;

        if(s[s.size()-1]=='-')
        {
            n=n+1;
        }

        for(int i=1; i<s.size(); i++)
        {
            if(s[i-1]!=s[i])
            {//cout<<s[i-1]<<s[i]<<i<<endl;
                n++;
            }
        }

        cout<<"Case #"<<(ti-t+1)<<": "<<n<<endl;

    }

    return 0;
}
