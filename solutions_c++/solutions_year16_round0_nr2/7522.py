#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;
string flip(string str,int no)
{
    for(int i=0;i<no+1;i++)
    {
        if(str[i]=='-')
            str[i]='+';
        else
            str[i]='-';
    }
    return str;
}

int main() {

    freopen("b-large.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,j,i,n,cnt;
    string abc;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cnt=0;
        cin>>abc;
        for(j=abc.length()-1;j>=0;j--)
        {
            if(abc[j]=='-')
            {
                cnt++;
                abc=flip(abc,j);
            }
        }
        cout<<"Case #"<<i<<": "<<cnt<<endl;
    }
    return 0;
}

