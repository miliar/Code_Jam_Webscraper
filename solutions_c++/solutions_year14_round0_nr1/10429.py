#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int T;
    int ArrPre[5][5],ArrNex[5][5];
    int IntAns1,IntAns2;
    ifstream fin("t.in");
    ofstream fout("r.txt");

    int i=1;
    fin>>T;
    //while(!fin.eof())
    for(i=1;i<=T;i++)
    {

        fin>>IntAns1;
        for(int j=1;j<5;j++)
        {
            for(int k=1;k<5;k++)
            {
                fin>>ArrPre[j][k];
            }
        }

         fin>>IntAns2;
        for(int j=1;j<5;j++)
        {
            for(int k=1;k<5;k++)
            {
                fin>>ArrNex[j][k];
            }
        }

        //finish input

        int cc=0,num=0;
        for(int j=1;j<5;j++)
        {
            int tmp=ArrPre[IntAns1][j];
            for(int k=1;k<5;k++)
            {
                if(tmp==ArrNex[IntAns2][k])
                {
                    cc++;
                    num=tmp;
                }
            }
        }

        //cout the result
        if(cc==1)
        {
            //fine
            fout<<"Case #"<<i<<": "<<num<<endl;
          //  i++;

        }
        else if(cc==0)
        {
            fout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
           // i++;
        }
        else if(cc>1)
        {
            fout<<"Case #"<<i<<": Bad magician!"<<endl;
            //i++;
        }
        else
        {

            fout<<"error"<<endl;
            //i++;
        }



    }

    return 0;
}
