#include <iostream>
#include <string>
using namespace std;

long long solution(string s)
{
    long long r = 0;
    if(s[0] == '-')
        r++;
    for(int i=1;i<s.length();++i)
    {
        if(s[i]=='-' && s[i-1]=='+')
            r+=2;
    }
    return r;
}

int main()
{
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<t+1<<": "<<solution(s)<<endl;
    }
    return 0;
}
