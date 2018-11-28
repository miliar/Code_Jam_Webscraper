#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <memory.h>
using namespace std;
int main()
{
    int t;
    ifstream in("input.txt");
    ofstream out("output.txt");
    in>>t;
    for(int t1=0;t1<t;t1++)
    {
        int ar[17];
        int c;
        in>>c;
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                    int k;
                    in>>k;
                    ar[k]=i;
            }
        }
        int g;
        in>>g;
        int ar1[17];
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int k;
                in>>k;
                ar1[k]=i;
            }
        }
        int count=0;
        int pos=0;
        for(int i=1;i<=16;i++)
        {
            if(ar[i]==c && ar1[i]==g)
             {   count++;
                pos=i;
                }
        }
        if(count==0)
            out<<"Case #"<<t1+1<<": Volunteer cheated!"<<endl;
        else if(count>1)
            out<<"Case #"<<t1+1<<": Bad magician!"<<endl;
        else
        {
            out<<"Case #"<<t1+1<<": "<<pos<<endl;
        }
    }

    return 0;
}
