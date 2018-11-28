#include<bits/stdc++.h>
using namespace std;
bool revisar (string cad)
{
    for(int i=0;i<cad.size();i++)
        if(cad[i]!='+')
            return false;
    return true;
}
int main()
{
    int casos=0,caso=1;
    long long int resp=0;
    string cad="";
    cin>>casos;
    while(casos--)
    {
        resp=0;
        cin>>cad;
        while(revisar(cad)==false)
        {
            char id=cad[0];
            cad[0]=(cad[0]=='+'?'-':'+');
            for(int i=1;i<cad.size();i++)
                if(cad[i]==id)
                    cad[i]=cad[0];
                else
                    break;
            resp++;
        }
        printf("Case #%d: %llu\n",caso++,resp);

    }
    return 0;
}
