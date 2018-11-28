#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    fstream f;
    f.open("A.in");
    fstream o;
    o.open("o.txt");
    int t;
    f>>t;
    int cs=1;
    while(cs<=t)
    {
        int a,b;
        f>>a;
        int ar[4],ar1[4];
        int idx1=0;
        int tmp;
        for(int i=1;i<=4;i++)
        {
                for(int j=1;j<=4;j++)
                {
                    f>>tmp;
                    if(i==a)
                    {
                        ar[idx1++]=tmp;
                    }
                }


        }
        idx1=0;
        f>>a;
        //cout<<"asd "<<a<<endl;
        for(int i=1;i<=4;i++)
        {
                for(int j=1;j<=4;j++)
                {
                    f>>tmp;
                    if(i==a)
                    {
                        ar1[idx1++]=tmp;
                    }
                }


        }

        ////////////////
        /*for(int y=0;y<4;y++)
        cout<<ar[y]<<" ";
        cout<<endl;
        for(int y=0;y<4;y++)
        cout<<ar1[y]<<" ";*/

        int cnt=0;

        int v;
        for(int y=0;y<4;y++)
        {
            for(int x=0;x<4;x++)
            {
                if(ar[y]==ar1[x])
                {

                    cnt++;
                    v=ar[y];
                }

            }
        }
        o<<"Case #"<<cs++<<": ";
        if(cnt==1)
        o<<v<<endl;
        else if(cnt==0)
        o<<"Volunteer cheated!\n";
        else
            o<<"Bad magician!\n";
    }

}
