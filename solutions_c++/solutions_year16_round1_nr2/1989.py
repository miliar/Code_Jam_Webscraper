#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{
   // cout << "Hello world!" << endl;
    int t,n,q,a[2501],m,i,j,w;
    fstream f2,f1;
    f2.open("input.txt",ios::in);
    f1.open("output.txt",ios::out);
    cin>>t;
    //f2>>t;
    m=1;

    while(m<=t)
    {
       cin>>n;
       //f2>>n;
        for(i=0;i<=2500;i++)
            a[i]=0;
            w=2*n*n-n;
           // cout<<w;
        j=1;
        for(j=1;j<=w;j++)
        {
           cin>>q;
        //    f2>>q;
            a[q]++;
        }
       cout<<"Case #"<<m<<": ";
        //f1<<"Case #"<<m<<": ";
        for(i=1;i<=2500;i++)
        {
            if(a[i]&1!=0)
                cout<<i<<" ";
        //        f1<<i<<" ";
        }
        cout<<"\n";
        //f1<<endl;
        m++;
    }
    return 0;
}
