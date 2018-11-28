#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

int calculateOptim(string str);

int main()
{
    string line;
    int numbTests = 0, lineNumb = 0, num = 0;
    fstream myFile("B-large.in");
    ofstream outFile("output");

    if(myFile.is_open())
    {
        getline(myFile, line);
        numbTests = atoi(line.c_str());
        for(lineNumb = 1; lineNumb <= numbTests; lineNumb++)
        {
            //parsing the string
            getline(myFile, line);
            //Algorithm
            num = calculateOptim(line);
            //Write the output
            outFile << "Case #" << lineNumb << ": " << num << endl;
        }
    }

    //close files
    outFile.close();
    myFile.close();

    return 0;
}

int calculateOptim(string str)
{
    int index = 0, num = 0, negIndex = 0, posIndex = 0, strLength = 0;
    bool negEnd = true, posEnd = true;
    char g1;

    strLength = str.length();
    int allpos = 0, allneg = 0;
    int strEnd = strLength-1;
    int pairSigns = 0;
    int s;
    while(index <=strEnd)
    {
       if(str[index] == '+' && index <= strEnd)
       {
           index++;
           while(str[index] == '+' && index <= strEnd)
           {
                index++;
                allpos++;
           }

           if(index > strEnd)
                break;

           while(str[index] == '-' && index <= strEnd)
                index++;

           num = num+2;

       }

       if(str[index] == '-' && index <= strEnd)
       {
           index++;
           while(str[index] == '-' && index <= strEnd )
           {
               index++;
               allneg++;
           }
           num++;
       }

    }
    if(allpos == strLength)
        num = 0;
    if(allneg == strLength)
        num = 1;

    return num;
}
