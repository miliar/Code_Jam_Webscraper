#include<iostream>
#include<fstream>

void solve (std::ifstream& , int&);

int main()
{
    int interation = 1;
    std::ifstream fin;
    fin.open("A-large.in");
    int loopCount;
    fin >> loopCount;
    for(int i=0;i<loopCount;i++)
    {
        solve(fin, interation);
    }

    return 0;

}

void solve(std::ifstream& fin , int& interation)
{
    long int peopleCount , answer=0;
    fin >> peopleCount;
    char arr[peopleCount]; //we have peopleCount +1 people
    for(int i=0 ; i <= peopleCount ; i++)
    {
        fin >> arr[i];
    }
    std::ofstream fout;
    fout.open("output", std::ios::out | std::ios::app);
    // need to check when a zero occurs if so do the previous values add up to the next position value
        // if yes continue checking the rest of the input
        // if no increment peopleNeeded by defecit check continue as if yes
        for(int i=0; i<=peopleCount ; i++)
        {
            if(arr[i]=='0')
            {
                long int addition=0;
                int numbers[i];
                for(int j=0; j<i ; j++)
                {
                    numbers[j]=arr[j]-'0'; //made an array with all the numbers ,probably not necessary but I want it
                    addition = numbers[j]+addition;

                }
                addition+=answer;
                if (addition <= i)
                {
                    // need to add to the answer
                    answer+=1;
                }
                else
                {
                 // do nothing
                }
            }
        }
        fout << "Case #" << interation << ": " << answer << std::endl;
        interation++;
    fout.close();

}
