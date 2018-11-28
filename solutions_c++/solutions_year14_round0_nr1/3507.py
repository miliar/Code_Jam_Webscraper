#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int n1,n2,t,a[17],b[17],same,num;
    ifstream in("A-small.in");
    ofstream out("A-small.out");
    in>>t;
    for (int i=0;i<t;i++)
    {
        same=0;
        in>>n1;
        for (int j=0;j<16;j++)
        {
            in>>a[j];
        }
        in>>n2;
        for (int j=0;j<16;j++)
        {
            in>>b[j];
        }
        for (int j=(n1-1)*4;j<4*n1;j++)
        {
            for (int k=(n2-1)*4;k<4*n2;k++)
            {
                if (a[j]==b[k]) {same++;num=a[j];}
            }
        }
        if (same>1)
        {
            out<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }
        if (same<1)
        {
            out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }
        if (same==1)
        {
            out<<"Case #"<<i+1<<": "<<num<<endl;
        }
    }
    return 0;
}
