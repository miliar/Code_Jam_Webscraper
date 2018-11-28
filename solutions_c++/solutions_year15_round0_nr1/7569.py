#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int people=0,frnd=0;
        for(int i=0;i<n;i++)
        {
            people=people+(s[i]-48);
            if(people<(i+1))
            {
                frnd=frnd+(i+1-people);
                people=i+1;
            }
        }
        cout<<"Case #"<<j<<": "<<frnd<<endl;
    }
    return 0;
}
