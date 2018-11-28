// INFEMP ACIO
#include<iostream>
#include<fstream>
using namespace std;

main()
{
    ofstream output;
    ifstream input;

    output.open("result.txt");
    input.open("input.txt");

    int ntc,x,y,a[4][4],b[4][4],flag1,flag2,num,ser=0;
    input>>ntc;
    while(ntc--)
    {
        flag1=0;
        flag2=0;

        input>>x;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                input>>a[i][j];
            }
        }

        input>>y;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                input>>b[i][j];
            }
        }

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[x-1][i]==b[y-1][j] && flag1==0)
                {
                    num=a[x-1][i];
                    flag1=1;
                }
                else if(a[x-1][i]==b[y-1][j] && flag1==1)
                {
                    flag2=1;
                    break;
                }

            }
        }
            if(flag1==1 && flag2==0)
            {
                output<<"Case #"<<ser+1<<": "<<num<<endl;
            }
            else if(flag1==1 && flag2==1)
            {
                output<<"Case #"<<ser+1<<": "<<"Bad magician!"<<endl;
            }
            else if(flag1==0 && flag2==0)
            {
                output<<"Case #"<<ser+1<<": "<<"Volunteer cheated!"<<endl;
            }
    ser++;
    }
    output.close();
    input.close();
}

