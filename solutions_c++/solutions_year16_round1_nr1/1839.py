#include<iostream>
using namespace std ;
int main()
{
    int t,x ;
    cin>>t ;
    x=t;
    while(t--)
    {
        string s ;
        cin>>s;
        int len ,i,k=0,j ;
        len = s.length();
        char a[len];
        a[0]=s[0];
        for(i=1;i<len;i++)
        {
            if(s[i]>=a[0])
            {
                for(j=k;j>=0;j--)
                {
                    a[j+1]=a[j];
                }
                a[0]=s[i];
            }
            else
            {
                a[k+1]=s[i];
            }
            k++;
        }
        cout<<"Case #"<<x-t<<": " ;
        for(i=0;i<len;i++)
        {
            cout<<a[i];
        }
        cout<<endl;
    }
}
