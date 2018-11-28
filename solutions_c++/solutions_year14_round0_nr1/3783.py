#include <iostream>
#include <fstream>
using namespace std;

int cards[20];
ofstream fout;

ifstream fin;


void initialize() {
    for (int i=0;i<17;i++)
        cards[i]=0;
}

void make_choice() {
        int choice;
        fin>>choice;
        for (int i=1; i<=4;i++)
        {
            for (int j=1; j<=4;j++)
            {
                int tmp;
                fin>>tmp;
                if (i == choice)
                    cards[tmp]++;
            }
        }
}

int main()
{
    fout.open("output.txt",ios::trunc);
    fin.open("A-small-attempt0.in", ios::in);
    int cases;
    fin>>cases;
    for (int CaseNum=0; CaseNum < cases; CaseNum ++)
    {
        initialize();
        make_choice();
        make_choice();
        int num=0;
        int ans=0;
        for (int i=1;i<=16;i++)
            if (cards[i] == 2)
        {
            num++;
            ans=i;
        }
        fout<<"Case #"<<CaseNum+1<<": ";
        if (num == 0)
            fout<<"Volunteer cheated!";
        else if (num ==1)
            fout<<ans;
        else
            fout<<"Bad magician!";
        fout<<endl;
    }
    fin.close();
    fout.close();

    return 0;
}
