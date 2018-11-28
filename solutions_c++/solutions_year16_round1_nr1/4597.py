#include<iostream>
using namespace std;
int main()
{
 
    int t,i,j,k;
    char d[3000];
    string str;
    int T;
    cin>>t;
 
    for(T=1;T<=t;T++)
    {
        cin>>str;
 
        d[0]=str[0];
        int m=str.size();
 
        for(i=1;i<m;i++)
        {
 
            if(str[i]>=d[0])
            {
 
                for(j=i;j>=0;j--)
                {
                    d[j+1]=d[j];
                }
                d[0]=str[i];
            }
 
            else
            {
                d[i]=str[i];
            }
 
 
        }
        cout<<"Case #"<<T<<": ";
        for(i=0;i<str.size();i++)
        {
            cout<<d[i];
        }
        cout<<endl;
    }
}