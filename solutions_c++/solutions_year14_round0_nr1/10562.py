#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main (void)
{
    //ifstream fin("A-small-attempt4.in");
    ofstream fout("A-small-attempt5.out");

    int test_case;
    cin >> test_case;

    for(int i=1; i<=test_case;i++)
    {
        int which_row_1;
        cin >> which_row_1;

        int number1[5][5];
        for(int j=1;j<5;j++)
        {
            for(int k=1;k<5;k++)
            {
                cin >> number1[j][k];
            }
        }

        int which_row_2;
        cin >> which_row_2;

        int number2[5][5];
        for(int j=1;j<5;j++)
        {
            for(int k=1;k<5;k++)
            {
                cin >> number2[j][k];
            }
        }


        int same_number=0;
        int answer;

        for(int j=1;j<=5;j++)
        {
            for(int k=1;k<=5;k++)
            {
                if(number1[which_row_1][j]==number2[which_row_2][k])
                {
                    same_number++;
                    answer = number1[which_row_1][j];
                }
                if(same_number>1)
                {
                    break;
                }
            }
        }

        if(same_number==0)
        {
            fout << "Case #" << i << ": Volunteer cheated!" << "\n";
        }
        else if(same_number==1)
        {
            fout << "Case #" << i << ": "<< answer << "\n";
        }
        else
        {
            fout << "Case #" << i << ": Bad magician!" << "\n";
        }

    }

    return 0;
}
