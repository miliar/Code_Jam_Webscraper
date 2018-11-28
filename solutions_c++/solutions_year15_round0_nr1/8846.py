#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("c:\A-large.in");
    ofstream out("output_cj");
    if(!in){cout<<"can't open";return 1;}

    int x,j,c,total,n,i,z;


        in>>n;
        for(i=0;i<n;i++)
        {
            total=c=0;
            in>>x;
            char a[x+1];
            in>>a;
            for(j=0;j<x+1;j++)
            {
                z=0;
                if(j>total&&a[j]>0){z+=j-total;}
                c+=z;
                total+=a[j]-48+z;
            }
        out<<"Case #"<<i+1<<": "<<c<<"\n";
        }
        in.close();
        out.close();
    return 0;
}
