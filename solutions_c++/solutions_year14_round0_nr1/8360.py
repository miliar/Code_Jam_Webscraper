
#include <iostream>
#include <fstream>
using namespace std;


int main()
{

    int i,j,k,l,m,n,g=0;



    ifstream infile;
    infile.open("in.in");

    ofstream out;
    out.open("card0.txt");

    infile>>k;
    while(!k==0)
    {
         int f=0;
        int d=0;
        int a[4][4],b[4][4],c[4];
        infile >> m;
            for(i=0; i<4; i++)
            {
                for(j=0; j<4; j++)
                {
                    infile>>a[i][j];
                }

            }

            infile >> n;
            for(i=0; i<4; i++)
            {
                for(j=0; j<4; j++)
                {
                    infile>>b[i][j];
                }

            }

            for(i=m-1; ; )
            {
                for(j=0;j<4;j++)
                {
                    c[j]=a[i][j];

                }
                break;
            }


                f=0;

                for(j=0;j<4;j++)
                {
                    for(i =0;i<4;i++)
                    if(c[j]==b[n-1][i])
                    {
                        l=c[j];
                        f++;
                    }


                }


            if(f==1)
            {
                out<<"Case #"<<g+1
                    <<": "<<l<<"\n";

            }
            if(f>1)
            {
                out<<"Case #"<<g+1
                    <<": "<<"Bad magician!"<<"\n";

            }
            if(f==0)
            {
                out<<"Case #"<<g+1
                <<": "<<"Volunteer cheated!"<<
                "\n";

            }


                k--;
                g++;
                //cout<<g;

    }





    return 0;

}
