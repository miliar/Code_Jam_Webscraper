#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>

using namespace std;

int main()
{
    int i,j,k,n,t,Case,ex,cur;
    string s;
    freopen("Input_5.in","r",stdin);
    freopen("Output.txt","w",stdout);
    cin>>t;
    Case=0;
    while(t--)
    {
        Case++;
        cin>>n;
        cin>>s;
        n++;
        ex=0;
        cur=0;
        for(i=0;i<n;i++)
        {
            if(cur<i)
            {
                ex+=i-cur;
                cur=i;
            }
            cur+=s[i]-'0';
        }
        cout<<"Case #"<<Case<<": "<<ex<<endl;
    }
    return 0;
}
