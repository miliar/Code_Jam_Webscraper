#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;
int main()
{
    freopen("inn.txt","r",stdin);
freopen("ouut.txt","w",stdout);
    int ca , x=0;
    cin>>ca;
    while(ca--)
    {
        int l;
        cin>>l;
        char str[l+1];
        cin>>str;
        int stand=str[0]-'0';
        int add=0 , j=0;
        for(int i=1 ; i<= l ; i++)
        {

            if(stand<i && str[i])
            {
                j=(i-stand);
                add+=j;
            }
            stand+=j+str[i]-'0';
            j=0;



        }
       printf("Case #%d: %d\n",++x,add);
    }
}

