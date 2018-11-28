
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int n=0;
    cin>>n;
    for(int x=0;x<n;x++)
    {
        char s[100];
        cin>>s;
        int count=0;


        for(int z = strlen(s)-1;z>=0;z--)
        {
            if(s[z]=='-')
            {
                for(int k = z;k>=0;k--)
                {
                    if(s[k]=='-')
                        s[k]='+';
                    else
                        s[k]='-';
                }
                count++;
            }
        }
        cout<<"Case #"<<x+1<<": "<<count<<"\n";
    }
    return 0;
}


