#include <iostream>
#include <bits/stdc++.h>
#include <cstdlib>
#include <time.h>
using namespace std;
int main()
{
freopen("bl.in","r",stdin);
freopen("output_BL","w",stdout);

    long long int T,N=0,C;
    int i;
    cin>>T;
    while(T--)
    {
    N++;
    string s;
    cin>>s;
    C=0;
    i=0;
    if(s[0]=='-')
    {
      while(s[i]==0)
      i++;
    C=1;
    }
    while(i<s.length())
    {
    if(s[i]=='+'&& s[i+1]=='-')
    C+=2;
    i++;

    }
    cout<<"case #"<<N<<": "<<C<<endl;

    }
    return 0;
}
