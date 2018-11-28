#include<bits/stdc++.h>
using namespace std;
int c1,c2,l,c;
int main()
{

   // freopen("input.in","r",stdin);
    //freopen("out.txt","w",stdout);

    char cad[1005];
    cin>>c1;
    c=0;
    for(int i=0;i<c1;i++)
    {
        cin>>l>>cad;
        int suma=0;
        int falta=0;

        for(int j=0;j<l+1;j++)
        {
            int val=cad[j]-'0';
            if(suma+val>=j+1)
            {
                suma+=val;
            }
            else
            {
                falta++;
                suma++;

            }
        }

        c++;
        cout<<"Case #"<<c<<": "<<falta<<endl;

    }

    //fclose(stdin);
    //fclose(stdout);

    return 0;
}
