//
// Created by smalldog on 16/4/9.
//

#include "2.h"

#include<iostream>
#define MAX 105;
#include<string>
#include<vector>

using namespace std;

int* a;   //up
int* b;   //down

int minFilp(string s)
{

    long len=s.size();
    a=new int[len];
    b=new int[len];
    a[0]=0;
    b[0]=0;
    for(int i=1;i<=len;i++)
    {
        if(s[i-1]=='+')
        {
            a[i]=min(a[i-1],b[i-1]+1);
            b[i]=min(a[i-1]+1,b[i-1]+2);
        }
        if(s[i-1]=='-')
        {
            a[i]=min(a[i-1]+2,b[i-1]+1);
            b[i]=min(b[i-1],a[i-1]+1);
        }

    }

    return min(a[len],b[len]+1);

}
int main()
{
    int T;
    string str;
    vector<string> vec;
    cin>>T;
    for(int i=T;i>0;i--)
    {
        cin>>str;
        vec.push_back(str);
    }
    for(int i=0;i<T;i++)
    {
        string tmp=vec[i];
        int res=minFilp(tmp);
        cout<<"Case #"<<i+1<<": "<<res<<endl;

    }
    return 0;

}