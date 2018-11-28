#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int t1=0;t1<t;t1++)
    {
        string s;
        cin>>s;
        int k,f=0;
        cin>>k;
        int n=s.length();
        int co=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                if(i+k-1<n)
                {
                    for(int j=0;j<k;j++)
                    {
                        if(s[i+j]=='-')
                        s[i+j]='+';
                        else
                        s[i+j]='-';
                    }
                    co++;
                }
                else
                f=1;
            }
        }
        if(f==1)
        cout<<"Case #"<<t1+1<<": "<<"IMPOSSIBLE\n";
        else
        cout<<"Case #"<<t1+1<<": "<<co<<endl;
        
    }
    return 0;
}
