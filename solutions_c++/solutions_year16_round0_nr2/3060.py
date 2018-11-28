
#include <cstdio>
#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <string.h>
#include <cstring>
#include <InfInt.h>

using namespace std;

char reverse_sign(char c)
{
    if(c=='-')
        return '+';
    else if(c=='+')
        return '-';
}

int main()
{
    int t, u, i, n, j, no_of_plus, no_of_man;
    
    freopen("BL.in", "rt", stdin);
    freopen("BL.out", "wt", stdout);
    
    cin>>t;
    u=1;
    while(u<=t)
    {
        char str[102];
        cin>>str;
        n=strlen(str);
        
        no_of_plus=0;
        for(i=0;i<n;i++)
                if(str[i]=='+')
                    no_of_plus++;
       
        no_of_man=0;
        while(no_of_plus!=n)
        {
            for(i=n-1;i>=0;i--)
                if(str[i]=='-')
                {
                    for(j=0;j<=i;j++)
                        str[j]=reverse_sign(str[j]);
                    no_of_man++;
                    break;
                }
            no_of_plus=0;
            for(i=0;i<n;i++)
                if(str[i]=='+')
                    no_of_plus++;
        }
      
        cout<<"Case #"<<u<<": "<<no_of_man<<endl;
        u++;
    }
    return 0;
}

/**/

