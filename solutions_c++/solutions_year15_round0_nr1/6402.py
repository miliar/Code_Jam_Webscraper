#include <bits/stdc++.h>
using namespace std;
int main()
{
    int casos, caso=1;
    cin>>casos;
    while(casos--)
    {
        int shyM, resp=0, personas=0;
        string queso;
        cin>>shyM>>queso;
        for(int i=0; i<shyM+1; i++)
        {
            int acum=0;
            for(int j=i-1; j>=0; j--)
            {
                acum+= (queso[j]-'0');
            }
            if(acum<i)
            {
                resp+=i-acum;
                queso[i]+=i-acum;
            }

        }

        printf("Case #%d: %d\n",caso,resp);
        caso++;
    }

    return 0;
}
