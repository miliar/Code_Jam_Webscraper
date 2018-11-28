#include<iostream>
using namespace std;
#include<fstream>
#include<cstdlib>


int main()
{
    int T;
    int row_choice;
    int card_arrangement[4][4];
    int row1[4],row2[4];
    int card;
    int found;
    int flag=0;
    int cnt=0;
    int res[100];
    //char fileName[60];
    ifstream infile("A-small-attempt1.in");
    ofstream outfile("b.txt");

    infile>>T;

    if (T>0 && T<=100)
    {
        for (int index=0;index<T;index++)
        {
            card=0;
            flag=0;
            cnt=0;

            infile>>row_choice;
            row_choice--;
            for (int i=0;i<4;i++)
            {
                for (int j=0;j<4;j++)
                {
                    infile>>card_arrangement[i][j];
                }
            }

            for (int i=0;i<4;i++)
            {
                for (int j=0;j<4;j++)
                {
                    row1[i]=card_arrangement[row_choice][i];
                }
            }

            infile>>row_choice;
            row_choice--;
            for (int i=0;i<4;i++)
            {
                for (int j=0;j<4;j++)
                {
                    infile>>card_arrangement[i][j];
                }
            }

            for (int i=0;i<4;i++)
            {
                for (int j=0;j<4;j++)
                {
                    row2[i]=card_arrangement[row_choice][i];
                }
            }

            //checking for required output
            for (int inner=0;inner<4;inner++)
            {
                card=row1[inner];

                for (int outer=0;outer<4;outer++)
                {
                    if (row2[outer]==card)
                    {
                        found=card;
                        cnt++;
                        flag=1;
                    }
                }
            }

            if (flag==1)
            {
                if (cnt==1)
                    res[index]=found;
                else
                    res[index]='m';
            }
            else
                res[index]='v';
        }


        for (int index=0;index<T;index++)
        {
            outfile<<"Case #"<<index+1<<": ";

            if (res[index]=='m')
                outfile<<"Bad magician!";
            else if (res[index]=='v')
                outfile<<"Volunteer cheated!";
            else
                outfile<<res[index];
            outfile<<endl;
        }
    }
    cout<<"Done!";
}
