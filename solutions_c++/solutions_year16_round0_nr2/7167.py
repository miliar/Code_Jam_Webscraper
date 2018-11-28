#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int t,k=1,c=0,i,j,l;
    char a[120];
    cin>>t;
    while(t--)
    {
        cin>>a;
        l=strlen(a);
        c=0;
        i=0;
        while(i<l-1)
        {
            i=0;
            while(a[i]==a[i+1])
                i++;

            if(i<l-1)
            {
                c++;
                for(j=0;j<=i;j++)
                {
                    if(a[j]=='+')
                        a[j]='-';
                    else
                        a[j]='+';
                }

            }
        }
        if(a[0]!='+')
           c++;
        cout<<"CASE #"<<k++<<": "<<c<<endl;


    }
    return 0;
}
