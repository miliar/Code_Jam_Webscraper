#include<iostream>
using namespace std;
int main()
{
 int t;
cin>>t;

int u[34*t];
for(int h=1;h<=34*t;h++)
   cin>>u[h];

for (int q=1,o=1;q<=34*t;q=q+34,o++)
{
    int p,r,v,s;
    int a[16],b[16];
    int c=0,m=0;
    p=u[q];
    for(int k=1;k<=16;k++)
        a[k]=u[q+k];
    r=u[q+17];
    
    for(int g=1;g<=16;g++)
        b[g]=u[q+17+g];

   

    for( s=4*p;s>4*p-4;s--)
        for( v=4*r ;v>4*r-4;v--)
            {
          if (a[s]==b[v])
               {


                c++;
                   m=a[s];
               }
             
            }


    if(c==1)
       cout<<"Case #"<<o<<": "<<m<<"\n";
    else if (c==0)
        cout<<"Case #"<<o<<": "<<"Volunteer cheated!"<<"\n";
    else
        cout<<"Case #"<<o<<": "<<"Bad magician!"<<"\n";

}

    return 0;
}
