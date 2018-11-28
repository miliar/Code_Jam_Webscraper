#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ofstream mafile;
    mafile.open("codesh.txt");
    long long int i,total,ans,t,l,k=0;
    string s;
    cin>>t;
    while(t--)
    {
        ++k;
        cin>>l>>s;
        ans=0;total=0;
        long long int a[4000]={0};
    for(i=0;i<s.length();i++)
        {
            a[i]=s[i]-'0';
        }
    for(i=0;i<=l;i++)
    {
        if(i==0&&a[i]==0)
        {
           ans=1; total=1;
        }
        else
        {
            if(a[i]!=0)
            {
                if(total>=i||total==0)
                    total=total+a[i];
                else
                {
                    ans=ans+(i-total);
                    total=total+(i-total);
                    total=total+a[i];

                }
            }

        }

        }
        mafile<<"Case #" << k <<": "<<ans <<endl;
    }
    return 0;
}
