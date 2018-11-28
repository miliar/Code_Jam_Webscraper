#include <iostream>
#include <fstream>

using namespace std;

int Magic(int * num1, int * num2)
{
    int answer, answers = 0;
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if(num1[i]==num2[j])
            {
                answer = num2[j];
                answers++;
                if(answers>1) { break; break; }
            }
        }
    }
    if(answers==1) return answer;
    else if(answers==0) return answers;
    else return -1;
}

int main(int argc, char *argv[])
{
    ifstream file_input("A-small-attempt0.in", ios::in);
    ofstream file_output("A-small-attempt0(answer).in", ios::trunc | ios::out);
    if(file_input && file_output)
    {
        int games, test=1, row1, row2, i, num1[4], num2[4];
        file_input >> games;
        while(test<=games)
        {
            file_input >> row1;

            for(i=0; i<4; i++)
                if(row1-1==i) file_input >> num1[0] >> num1[1] >> num1[2] >> num1[3];
                else file_input >> row2 >> row2 >> row2 >> row2;

            file_input >> row2;

            for(i=0; i<4; i++)
                if(row2-1==i) file_input >> num2[0] >> num2[1] >> num2[2] >> num2[3];
                else file_input >> row1 >> row1 >> row1 >> row1;

            file_output << "Case #" << test << ": ";

            if(Magic(num1,num2)<0)
            {
                file_output << "Bad magician!";
            }
            else if(Magic(num1,num2)==0)
            {
                file_output << "Volunteer cheated!";
            }
            else
            {
                file_output << Magic(num1,num2);
            }

            file_output << "\n";
            test++;
        }
        file_input.close();
        file_output.close();
    }
    else
        cerr << "Error : Cannot open the file !" << endl;
    return 0;
}
