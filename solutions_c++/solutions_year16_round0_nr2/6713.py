#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#define ll long long int

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    // std::ios_base::sync_with_stdio(false);
    int t,cases=1,i,j;
    cin>>t;
    while(t--)
    {

        string s;
        int c=0,p=0,pl=-1,tot=0;
        cin>>s;
        cout<<"Case #"<<cases<<": ";
        for(i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                p =1;
                if(pl == 1) tot = 1;
            }
            else
            {
                if(pl==-1) pl=1;
                if(p==1)
                {
                    if(tot==1)
                    {
                        c+=2;
                        tot=0;
                    }
                    else if(c==0) c++;
                    else c+=2;
                    p=0;
                }
            }
        }
        if(p!=0)
        {
            if(tot==1) c+=2;
            else if(c==0) c++;
            else c+=2;
        }
        cout<<c<<endl;



        cases++;
    }


    return 0;
}
