#include<iostream>
#include<stdio.h>
#define SIZE 4

using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    double C,F,X,f,ti,Ti,ti_next,Tx,tx_next,Ti_next,Tx_next,tx;
    for(int k=1;k<=t;k++)
    {
        cin>>C>>F>>X;
        Ti=0;
        for(int i=0;;i++)
        {
            f=2+F*i;
            tx=X/f;
            tx_next=X/(f+F);
            Tx=Ti+tx;
            ti=C/f;
            ti_next=C/(f+F);
            Ti+=ti;
            Ti_next=Ti+ti_next;
            Tx_next=Ti+tx_next;
            /*
            cout<<"tx="<<tx<<endl;
            cout<<"tx_next="<<tx_next<<endl;
            cout<<"Tx="<<Tx<<endl;
            cout<<"ti="<<ti<<endl;
            cout<<"ti_next="<<ti_next<<endl;
            cout<<"Ti="<<Ti<<endl;
            cout<<"Ti_next="<<Ti_next<<endl;
            cout<<"Tx="<<Tx<<"Tx_next="<<Tx_next<<endl;
*/
            if(Tx<=Tx_next)
            {
                //cout<<"Case #"<<k<<": "<<Tx<<endl;
                printf("Case #%d: %.7lf\n",k,Tx);
                break;
            }
        }
    }

return 0;
}
