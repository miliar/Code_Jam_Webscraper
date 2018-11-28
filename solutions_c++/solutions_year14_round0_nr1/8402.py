#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
int a[5], b[5];
int i,j,l,t,a1,b1,k;
    cin>>t;
    ofstream cout("output.txt");
    for (l=1; l<=t; l++)
    {
        int c=0;
        cin>>a1;
        for (i=1; i<=4; i++)
        for (j=0; j<4; j++) 
        {
        if (a1==i) cin>>a[j]; 
        else cin>>k;
        }
        cin>>b1;
        for (i=1; i<=4; i++)
        for (j=0; j<4; j++) 
        {
         if (b1==i)  cin>>b[j]; 
         else cin>>k;
        }
        for (i=0; i<4; i++)
        for (j=0; j<4; j++)
        if (a[i]==b[j]) {
                        c++;
                        k=a[i];}
        if (c==1) cout<<"Case #"<<l<<": "<<k<<endl;
        else if (c>1) cout<<"Case #"<<l<<": Bad magician!"<<endl;
        else if (c==0) cout<<"Case #"<<l<<": Volunteer cheated!"<<endl;
    }
system("pause");
return 0;
}
