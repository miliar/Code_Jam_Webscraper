#include <iostream>
#include <stdio.h>

using namespace std;

int ROP(string &A)
{
    int ans = 0;
    for(unsigned int i=0; i<A.length(); i++)
    {
        bool flag = 0;
        if(i==0)
        {
            while(i<A.length() && A[i] == '-')
            {
                flag = 1;
                i++;
            }
            if(flag)
                ans++;
        }
        else
        {
            while(i<A.length() && A[i]=='-')
            {
                flag = 1;
                i++;
            }
            if(flag)
                ans += 2;
            //cout<<"Added 2"<<endl;
        }
    }
    return ans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    string str;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        cin>>str;
        cout<<"Case #"<<i+1<<": "<<ROP(str)<<endl;
    }
    return 0;
}
