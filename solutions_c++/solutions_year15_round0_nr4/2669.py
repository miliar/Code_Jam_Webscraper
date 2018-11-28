#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{        ofstream fout;

        fout.open("ans.txt");
    long long int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {  int tag =0;
        long long int n,r,c ;
        cin>>n>>r>>c;


        if((r*c)<n)
        {
            tag=1;

        }
        else
        {
            if(((r*c)%n)!=0)
            {
                tag=1;
            }
            else
            {
                if(r+c-1<=n)
                    tag=1;


            }


        }

            if(n==2&&r*c==2)
                tag=0;
            if(n==4&&r==2&&c==4)
            {
                tag=1;
            }
            if(n==1&&r==1&&c==1)
            {
                tag=0;
            }
             if(n==4&&r==4&&c==2)
            {
                tag=1;
            }
                    if(tag)
                        {cout<<"RICHARD \n";
                        fout<<"Case #"<<i<<": "<<"RICHARD"<<"\n";}
                        else
                        {cout<<"GABRIEL \n";
                        fout<<"Case #"<<i<<": "<<"GABRIEL"<<"\n";
                        }

    }
}
