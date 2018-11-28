#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;


int main()
{


    int t, smax;
    string str;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        cin>>smax>>str;
        int total = 0;
        int req = 0;
        for(int j=0; j<=smax; j++)
        {
            if(j<=total)
            {
                total+=str[j]-'0';
            }else if(str[j]!='0')
            {
                req += j-total;
                total+= req+str[j]-'0';

            }
        }
        cout<<"Case #"<<i<<": "<<req<<endl;

    }
}
