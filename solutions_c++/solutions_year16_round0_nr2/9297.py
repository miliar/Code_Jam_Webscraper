#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int t, h, flag;
    char s[100], ch;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        ch='a';
        cin>>s;
        h=strlen(s); flag=0;
        for(int i=0; i<h-1; i++)
        {
            if(s[i]!=s[i+1])
            {
                for(int x=0; x<i+1; x++)
                {
                   s[x]=s[i+1];
                }
                flag+=1;
            }


        }
        if(s[h-1]=='-')flag+=1;
        cout<<"Case #"<<i<<": "<<flag<<endl;
    }
    return 0;
}

