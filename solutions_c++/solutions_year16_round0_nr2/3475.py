#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t,t1;
    cin>>t;
    for(t1=1;t1<=t;t1++)
    {
        long long int n,i,j=0,k=0;
        string str;
        cin>>str;
        for(i=0;i<str.size();i++)
        {
            if(str[i]=='-'&&k==0)
            {
                j++;
                k++;
            }
            else
            {
                if(str[i]=='+')
                    k=0;
            }
        }
        if(str[0]=='-')
            j=2*j-1;
        else 
            j=2*j;
        cout<<"Case #"<<t1<<": "<<j<<"\n";
    }    
    return 0;
}
