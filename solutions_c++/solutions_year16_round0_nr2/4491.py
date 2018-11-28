#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    int t,t1=1,len,i,count;
    cin>>t;
    while(t1<=t)
    {
        cin>>s;
        len=s.size();
        i=0;
        count=0;
        while(i<len)
        {
            while(i<len && s[i]=='+')
            {
                i++;
            }
            if(i<len && s[i]=='-')
            {
                while(i<len && s[i]=='-')
                {
                    i++;
                }
                count++;
            }
        }
        if(s[0]=='+')
        {
            cout<<"Case #"<<t1<<": "<<count*2<<endl;
        }
        else
        {
            cout<<"Case #"<<t1<<": "<<count*2-1<<endl;
        }
        t1++;
    }
    return 0;
}
