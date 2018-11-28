#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    int ar1[4][4], ar2[4][4], t, ans1,ans2, temp=0, c=0;
    ifstream fp;
    ofstream op;
    fp.open("test.in");
    op.open("output.in");
    fp>>t;
    for(int k=0; k<t; k++)
    {
    c=0;
    fp>>ans1;
    for (int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            fp>>ar1[i][j];
        }
    }
    fp>>ans2;
    for (int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            fp>>ar2[i][j];
        }
    }for(int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                if(ar1[ans1-1][i]==ar2[ans2-1][j])
                {
                    temp=ar1[ans1-1][i];
                    c++;
                }
            }
        }
        if(c==0)
        {
            op<<"Case #"<<k+1<<": Volunteer cheated!"<<endl;
        }
        if(c==1)
        {
            op<<"Case #"<<k+1<<": "<<temp<<endl;
        }
        if(c>1)
        {
            op<<"Case #"<<k+1<<": Bad magician!"<<endl;
        }
}
    return 0;
}
