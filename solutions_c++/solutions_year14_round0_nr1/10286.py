#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    char ch;
    fstream input, output;
    input.open("A-small-attempt2.in", ios::in);
    output.open("A-small-attempt2.out", ios::out);
    int t, row, i, j, k, flag, temp, rank = 0, ans;
    int c[4];
    input>>t;
    while(t--)
    {
        input>>row;
        for(i = 1; i <= 4; i++)
        {
            if(i == row)
            {
                for(j = 1; j <= 4; j++)
                    input>>c[j - 1];
            }
            else
            {
                for(j = 1; j <= 4; j++)
                    input>>temp;
            }
        }
        flag = 0;
        input>>row;
        for(i = 1; i <= 4; i++)
        {
            if(i == row)
            {
                for(j = 1; j <= 4; j++)
                {
                    input>>temp;
                    for(k = 0; k < 4; k++)
                    {
                        if(temp == c[k])
                        {
                            if(flag == 0)
                            {
                                flag = 1;
                                ans = temp;
                            }
                            else if(flag == 1)
                                flag = 2;
                            break;
                        }
                    }
                }
            }
            else
            {
                for(j = 1; j <= 4; j++)
                    input>>temp;
            }
        }
        if(flag == 0)
            output<<"Case #"<<++rank<<": Volunteer cheated!\n";
        else if(flag == 1)
            output<<"Case #"<<++rank<<": "<<ans<<"\n";
        else
            output<<"Case #"<<++rank<<": Bad magician!\n";
    }
    return 0;
}
