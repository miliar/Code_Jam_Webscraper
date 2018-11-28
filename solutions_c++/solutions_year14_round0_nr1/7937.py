#include<iostream>
#include<fstream>
using  namespace std;
int main()
{
    ifstream file("A-small-attempt1.in");
    ofstream ofile("ooooo.txt");
    int t,a1,a2,a[4][4],b[4][4];
    file>>t;
    for(int i=0;i<t;i++)
    {
       file>>a1;
       a1--;
       for(int h=0;h<4;h++)
       {
           for(int k=0;k<4;k++)
           {
               file>>a[h][k];
           }
       }
       file>>a2;
       a2--;
       for(int h=0;h<4;h++)
       {
           for(int k=0;k<4;k++)
           {
               file>>b[h][k];
           }
       }
       int d[7];
       for(int dfg=0;dfg<7;dfg++)
        d[dfg]=0;
       int c[8]={a[a1][0],a[a1][1],a[a1][2],a[a1][3],b[a2][0],b[a2][1],b[a2][2],b[a2][3]};
       for(int y=0;y<7;y++)
       {
            for(int w=y+1;w<8;w++)
            {
                if(c[y]==c[w])
                    d[y]++;
            }
       }
       int A=0,t;
       for(int ff=0;ff<7;ff++)
       {
           if(d[ff]==1)
           {
               t=c[ff];
               A++;
           }
       }
        ofile<<"Case #"<<i+1<<": ";
        if(A==0)
            ofile<<"Volunteer cheated!\n";
        else if (A==1)
            ofile<<t<<"\n";
        else
            ofile<<"Bad magician!\n";
    }
    return 0;
}
