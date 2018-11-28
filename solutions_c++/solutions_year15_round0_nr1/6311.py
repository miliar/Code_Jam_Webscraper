#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    int n,i,j;
    for(i=0;i<t;i++)
    {
        cin>>n;
        char a[n+2];
        cin>>a;
        int b[n+1];
        for(j=0;a[j]!='\0';j++)
        {
            b[j]=a[j]-48;
        }
        int s=0;
        int cn=0;
        for(j=0;j<n+1;j++)
        {
            while(true)
            {
                if(b[j]>0 && s>=j)
                {
                    s+=b[j];
                    break;
                }
                else if(b[j]==0)
                break;
                else
                {
                    s++;
                    cn++;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<cn<<endl;
    }
    return 0;
}
