#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.txt", "w", stdout);
    int t,counter;
    char s[101],a ;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        counter=0;
        cin>>s;
        int sz=strlen(s)-1;
        for(int j=sz; j>=0; j--)
        {
            if(s[j]=='-')
            {
                if(s[0]=='-')
                {
                    for(int m=j, n=0; m>=n; m--,n++)
                    {
                        a=s[n];
                        s[n]=s[m];
                        s[m]=a;
                    }
                    for(int k=0; k<=j; k++)
                    {
                        if( s[k]=='+') s[k]='-';
                        else s[k]='+';
                    }
                }
                else
                {
                    for(int l=j-1; l>=0; l--)
                    {
                        if(s[l]=='+')
                        {
                            for(int m=l, n=0; m>=n; m--,n++)
                            {
                                a=s[n];
                                s[n]=s[m];
                                s[n]=a;
                            }
                            for(int k=0; k<=l; k++)
                            {
                                if( s[k]=='+')
                                    s[k]='-';
                                else
                                    s[k]='+';
                            }
                            break;
                        }
                    }
                }
                counter++;
            }
        }
        cout<<"case #"<<i<<": "<<counter<<endl;
    }
}

