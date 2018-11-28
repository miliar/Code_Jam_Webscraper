#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int ti=0;ti<t;++ti)
    {
        int ms;
        string s;
        cin>>ms>>s;
        int add_req=0;
        int act=s[0]-'0';
        for(int i=1;i<=ms;++i)
        {
            add_req=max(add_req,i-act);
            act+=s[i]-'0';
        }
        cout<<"Case #"<<ti+1<<": "<<add_req<<endl;
    }
    return 0;
}
