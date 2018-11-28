/*Rahul Jain*/
#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<memory>
#include<iterator>
#include<math.h>

#define ll long long
#define ull unsigned long long

using namespace std;

int main()
{
    int t,s;
    cin>>t;for(int k=1;k<=t;k++)
    {
        cin>>s;
        string a;
        cin>>a;
        int temp=(a[0]-48),c=0;
        //cout<<"temp="<<temp<<endl;
        for(int j=1;j<(s+1);j++)
        {
            if(temp==j || temp>j)
            {
                temp=temp+(a[j]-48);
            }
            else
                {
                    c=c+(j-temp);
                    temp=temp+(j-temp);
                    temp=temp+(a[j]-48);
                }
        //cout<<"temp="<<temp<<" "<<"c="<<c<<endl;
        }
        cout<<"Case #"<<k<<": "<<c<<endl;
    }
return 0;
}
