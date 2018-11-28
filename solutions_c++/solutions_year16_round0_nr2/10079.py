#include<iostream>
#include<vector>
#include<string>
#include<conio.h>
#include<string.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int z=1; z<=t; z++)
    {
        string tmp;cin>>tmp;
        int c=0;
        char s[100];
        strcpy(s,tmp.c_str());
        for(int i =sizeof(s); i>-1; i--)
        {
            if(s[i]=='-')
            {
                for(int j=0; j<=i; j++)
                {
                    if(s[j]=='-')
                    {
                        s[j]='+';

                        //cout<<s<<" ";
                    }
                    else
                    {
                        s[j]='-';

                       // cout<<s<<" ";
                    }
                }
            c++;}
        }
    cout<<"Case #"<<z<<": "<<c<<endl;}
}
