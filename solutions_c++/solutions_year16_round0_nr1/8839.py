#include <iostream>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <string>
#include <cstring>

#define endl '\n'
    
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1; i <= t; i++)
    {
        //cout<<"fads"<<endl;
        int x;
        int v;
        string str;
        cin>>x;
        //cout<<x<<endl;
        char digarr[] = "0000000000";
        //cout<<digarr<<endl;
        if( x == 0 )
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            
        }
        else
        {
            
            //cout<<"abe"<<'\n';
            for(int j=1; strcmp(digarr,"1111111111"); j++)
            {
                //cout<<digarr<<endl;
                v = x*j;
                str = to_string(v);
                //cout<<v<<endl;
                for(int k=0; k<str.length(); k++)
                {
                    //cout<<str[k]<<endl;
                    digarr[str[k] - '0'] = '1';
                }
            }
            cout<<"Case #"<<i<<": "<<v<<endl;
        }
    }
    
        return 0;
}

