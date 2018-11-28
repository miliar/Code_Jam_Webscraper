#include <iostream>

using namespace std;

int main()
{
    int i,j,t,m,n,ns;
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>m;
        char s[m+1];
        cin>>s;
        ns=s[0]-48;
        n=0;
        for(j=1;j<m+1;j++)
        {
            if(ns<j&&(s[j]-48)!=0)
            {
                n=n+(j-ns);
                ns=ns+n+(s[j]-48);
            }
            else
            {
                ns=ns+(s[j]-48);
            }
        }
        cout<<"Case #"<<i+1<<": "<<n<<endl;
    }
    return 0;
}
