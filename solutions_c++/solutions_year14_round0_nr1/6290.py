#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int firstcards[20][20],secondcards[20][20],i,j,k,N,first,second,result[110],nambah;

int main()
{
    fstream myfile;
    myfile.open("A-small-attempt1.in",ios::in);
    myfile >> N;
    for(i=1;i<= N;i++)
    {

        nambah = 0;
        myfile >> first;
        for(j=1;j<=4;j++)
        {
            for(k=1;k<=4;k++)
            {
                myfile>>firstcards[j][k];
            }
        }
        myfile >> second;
        for(j=1;j<=4;j++)
        {
            for(k=1;k<=4;k++)
            {
                myfile >> secondcards[j][k];
            }
        }
        for(j=1;j<=4;j++)
        {
            for(k=1;k<=4;k++)
            {
                int zzz = firstcards[first][j];
                int lala = secondcards[second][k];
                if (zzz == lala)
                {
                    nambah++;
                    if(nambah == 1)
                    {
                      result[i] = lala;
                    }
                }
            }
        }
        if(nambah>1)
        {
            result[i] = -1;
        }
        else if(nambah == 0)
        {
            result[i] = 0;
        }

    }
    myfile.close();
    myfile.open("Thesolution.in", ios::out);
    for(i=1;i<=N;i++)
     {
         int lala = result[i];
         if(lala == -1 )
         {
             myfile << "Case #"<<i<<": Bad magician!"<<endl;
         }
         else if(lala==0)
         {
             myfile << "Case #"<<i<<": Volunteer cheated!"<<endl;
         }
         else
         {
             myfile << "Case #"<<i<<": "<< lala<<endl;
         }
     }
     myfile.close();
    return 0;
}
