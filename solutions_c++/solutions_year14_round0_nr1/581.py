#include<iostream>
#include<cmath>
#include<fstream>

using namespace std;

int main()
{
    int T,x,r1[4],r2[4],i,j,y1,y2,k1,k2;
    string pass;
    fstream input;
    fstream output;
    input.open("A-small.txt",ios::in);
    output.open("A-small-out.txt",ios::out);
    input>>T;
    for (x=1;x<=T;x++)
    {
        input>>y1;
        for(j=1;j<y1;j++)
        {
            input>>i;
            input>>i;
            input>>i;
            input>>i;
        }
        input>>r1[0];
        input>>r1[1];
        input>>r1[2];
        input>>r1[3];
        for(j=j+1;j<5;j++)
        {
            input>>i;
            input>>i;
            input>>i;
            input>>i;
        }
        input>>y2;
        for(j=1;j<y2;j++)
        {
            input>>i;
            input>>i;
            input>>i;
            input>>i;
        }
        input>>r2[0];
        input>>r2[1];
        input>>r2[2];
        input>>r2[3];
        for(j=j+1;j<5;j++)
        {
            input>>i;
            input>>i;
            input>>i;
            input>>i;
        }
        i=0;
        for (y1=0;y1<4;y1++)
        {
            for(y2=0;y2<4;y2++)
            {
                if (r1[y1]==r2[y2])
                {
                    i++;
                    k1=y1;
                    k2=y2;
                }
            }
        }
        if (i==0)
            output<<"Case #"<<x<<": Volunteer cheated!"<<endl;
        else if (i==1)
            output<<"Case #"<<x<<": "<<r1[k1]<<endl;
        else
            output<<"Case #"<<x<<": Bad magician!"<<endl;
    }
    input.close();
    output.close();
    return 0;
}
