#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

int calculateNumb(int N);

int main()
{
    string line;
    int N;
    int numbTests = 0, lineNumb = 0, num = 0;
    fstream myFile("A-large.in");
    ofstream outFile("output");

    if(myFile.is_open())
    {
        getline(myFile, line);
        numbTests = atoi(line.c_str());
        for(lineNumb = 1; lineNumb <= numbTests; lineNumb++)
        {
            //parsing the string
            getline(myFile, line);
            N = atoi(line.c_str());
            //Algorithm
            if(N == 0)
                outFile << "Case #" << lineNumb << ": " << "INSOMNIA" << endl;
            else
            {
                num = calculateNumb(N);
                //Write the output
                outFile << "Case #" << lineNumb << ": " << num << endl;
            }
        }
    }

    //close files
    outFile.close();
    myFile.close();

    return 0;
}

int calculateNumb(int N)
{
    long long num = 0, new_num=0,requiredNum=0;
    int i = 1, totalnum=0;
    int digit=0;
    bool a[10];

    for( i=0;i<=9;i++)
        a[i]=false;

    num = N;
    for(i = 1; totalnum < 10 ; i++ )
    {
        new_num = num*i;
        requiredNum=new_num;
       // new_num=num;
        while(new_num > 0)
        {
            digit = new_num%10;
            if (a[digit] == false)
            {
                a[digit]=true;
                totalnum++;
            }
            if(totalnum==10)
                break;

            new_num = new_num/10;

        }
    }

    return requiredNum;
}
