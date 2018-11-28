#include <iostream>
#include <fstream>


using namespace std;

int main()
{
    ofstream fout;
    ifstream fin;
    fin.open("A-small-attempt1.in");
    fout.open ("answers.txt");
    int n;
    fin>>n;
    for(int ctr1=0;ctr1<n;ctr1++)
    {
        int firstRed,secondRed;
        int red1[4],red2[4];
        fin>>firstRed;
        for(int ctr2=0;ctr2<4;ctr2++)
        {
            for(int ctr3=0;ctr3<4;ctr3++)
            {
                int temp;
                fin>>temp;
                if(ctr2==firstRed-1)
                {
                    red1[ctr3]=temp;
                }
            }
        }
        fin>>secondRed;
        for(int ctr2=0;ctr2<4;ctr2++)
        {
            for(int ctr3=0;ctr3<4;ctr3++)
            {
                int temp;
                fin>>temp;
                if(ctr2==secondRed-1)
                {
                    red2[ctr3]=temp;
                }
            }
        }
        int pojavuvanja=0;
        int lastPojavuvanje;
        for(int ctr2=0;ctr2<4;ctr2++)
        {
            for(int ctr3=0;ctr3<4;ctr3++)
            {
                if(red1[ctr2]==red2[ctr3]){
                pojavuvanja++;
                lastPojavuvanje=red1[ctr2];
                }
            }
        }
        fout<<"CASE #"<<ctr1+1<<": ";
        if (pojavuvanja==1)
        {
            fout<<lastPojavuvanje<<endl;
        }
        else if (pojavuvanja==0)
        {
            fout<<"Volunteer cheated!"<<endl;
        }
        else if (pojavuvanja>1)
        {
            fout<<"Bad magician!"<<endl;
        }
    }
    fout.close();
    fin.close();
    return 0;
}
