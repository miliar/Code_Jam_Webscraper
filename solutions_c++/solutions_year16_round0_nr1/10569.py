#include<bits/stdc++.h>
#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
string IntToString(long number);

string IntToString(long number)
{
    ostringstream oss;
    oss<< number;
    return oss.str();
}
int main()
{
    int T,t;
    scanf("%d",&T);
    for(t=1; t<=T; t++)
    {
        long long result=0;
        set<int>s;
        bool flag=true;
        int i=1;
        long long N;
        scanf("%lld",&N);
        if(N==0)
            cout<<"Case"<<" #"<<t<<": "<<"INSOMNIA"<<endl;
        else
        {
            while(flag==true)
            {
                long long x=N*i;
                i++;
                string ss=IntToString (x);
                for(int i=0; i<ss.size(); i++)
                {
                    s.insert(ss[i]);
                    if(s.size()==10)
                    {
                        flag=false;
                        result=x;
                        break;
                    }
                }
            }

            cout<<"Case"<<" #"<<t<<": "<<result<<endl;
        }
    }
    return 0;
}
