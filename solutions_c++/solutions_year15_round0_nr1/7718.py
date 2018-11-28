#include<stdio.h>
#include<iostream>
using namespace std;
int main ()
{
    int T,caseno,sm,stand,borrow,i;
    char man[1020];
    freopen("A-large.in","r",stdin);
    freopen("co.out","w",stdout);
    scanf("%d",&T);
    for(caseno=1; caseno<=T; caseno++)
    {
        cin>>sm>>man;
        stand=0;
        borrow=0;
        for(i=0; i<=sm; i++)
        {

            if(stand>=i)
            {
                stand=stand+man[i]-48;
            }
            else
            {
                borrow=borrow + (i-stand);
                stand=stand+(i-stand);
                stand=stand+(man[i]-48);
            }
        }
        cout<<"case #"<<caseno<<": ";

        cout<<borrow<<endl;
    }
}
