#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    short T,answer;
    short turn[4][4],guess1[4],guess2[4];
    ifstream ifile ("input.in");
    ifile >> T;
    short result[T];
    short res=0;
    for(int i =0; i<T;i++)
    {
        result[i] = 0;
    }
    for(int i = 0;i<T;i++)
    {
        ifile >> answer;
        for(int y = 0; y < 4 ;y++)
        {
            for(int x = 0; x < 4; x++)
            {
                if(y == answer-1)
                {
                    ifile >> guess1[x];
                }
                else
                {
                    ifile >> turn[y][x];
                }
            }
        }
        ifile >> answer;
        for(int y = 0; y < 4 ;y++)
        {
            for(int x = 0; x < 4; x++)
            {
                if(y == answer-1)
                {
                    ifile >> guess2[x];
                    for(int c = 0;c<4;c++)
                    {
                        if(guess1[c]==guess2[x])
                        {
                            if(result[res]==0)
                            {
                                result[res] = guess2[x];
                            }
                            else
                            {
                                result[res] = -1;
                            }
                        }
                    }
                }
                else
                {
                    ifile >> turn[y][x];
                }
            }
        }
        res++;
    }
    ifile.close();
    ofstream ofile ("output.out");
    for(int i =0; i<T;i++)
    {
        ofile << "Case #"<<i+1<<": ";
        if(result[i]>0)
        {
            ofile << result[i];
        }
        else if (result[i] <= 0)
        {
            if(result[i]==-1)
            {
                ofile << "Bad magician!";
            }
            if(result[i]==0)
            {
                ofile << "Volunteer cheated!";
            }
        }
        ofile << endl;
    }
}
