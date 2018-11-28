#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    int t,m,n,count;count=0;int card=0;
    int a[15][15];int b[15][15];
    ifstream in("small.in");ofstream out("small2f.txt");
    in>>t;
    for(int i=0;i<t;i++)
    {
        in>>n;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
            in>>a[j][k];
            in>>m;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
            in>>b[j][k];
            for(int k=0;k<4;k++)
                for(int j=0;j<4;j++)
                if(a[n-1][k]==b[m-1][j])
                {


                 count++;
                 card=a[n-1][k];
                }
if(count==1)
out<<"Case #"<<(i+1)<<": "<<card<<endl;
if((count>1)&&(count<=4))
out<<"Case #"<<(i+1)<<": Bad magician!"<<endl;
if(count==0)
out<<"Case #"<<(i+1)<<": Volunteer cheated!"<<endl;
count=0;

    }

    return 0;
}
