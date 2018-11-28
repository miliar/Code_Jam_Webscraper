#include<iostream>
#include<string.h>

using namespace std;

int main()
{

    int t,l,x=1;

    cin>>t;

    while(t--)

    {
        char s[100];

        int c=0;

        cin>>s;

        l = strlen(s);

        for(int i=1;i<l;i++)
        {
            if(s[i-1]!=s[i])
                c++;

        }

        if(s[l-1]=='-')
            c++;

        cout<<"Case #"<<x<<": "<<c<<"\n";

        x++;

    }

    return 0;

}

