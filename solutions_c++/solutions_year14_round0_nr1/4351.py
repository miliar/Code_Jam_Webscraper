#include<iostream>
using namespace std;
int main()

 
{
   int t;
   cin>>t;
   for(int aa=1;aa<=t;aa++)
{


    int p,r,v,s;
    int a[16],b[16];
    int c=0,m=0;
    cin>>p;
    for(int k=1;k<=16;k++)
        cin>>a[k];
    cin>>r;
    
    for(int g=1;g<=16;g++)
        cin>>b[g];

   

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
       cout<<"Case #"<<aa<<": "<<m<<"\n";   
    else if (c==0)
        cout<<"Case #"<<aa<<": "<<"Volunteer cheated!"<<"\n";
    else
        cout<<"Case #"<<aa<<": "<<"Bad magician!"<<"\n";


}
    return 0;
}
