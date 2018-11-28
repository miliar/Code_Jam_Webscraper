#include <iostream>
#include <cstdio>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>


using namespace std;

typedef vector<std::string> StringVector;


int main()
{
        long testCase,curTestCase;
    //cin >> testCase;
    std::string line;
    std::istringstream iss;

    ifstream myfile;
    myfile.open("input.txt",ios::in);

    ofstream outfile;
    outfile.open("out.txt");

    if (std::getline(myfile, line)) {
    iss.str(line);
    iss >> testCase;
    }

    //fscanf(fpt,"%ld\n",&testCase);
   // cout << testCase;
    for(curTestCase=0;curTestCase<testCase;curTestCase++)
    {
        long x,r,c;
        //cin >> cursize;

        std::istringstream iss2;

        if (std::getline(myfile, line))
            {
        //        cout << line;
            iss2.str(line);
            iss2 >> x;
            iss2 >> r;
            iss2 >> c;
            }
        std::string result;
        if(r == 1 && c == 1)
        {
            if(x == 1)
                result = "GABRIEL";
            else
                result = "RICHARD";
        }

        else if((r == 1 && c == 2) || (r == 2 && c == 1))
        {
            if(x == 1 || x == 2)
                result = "GABRIEL";
            else
                result = "RICHARD";
        }

        else if((r == 1 && c == 3) || (r == 3 && c == 1))
        {
            if(x == 1)
                result = "GABRIEL";
            else
                result = "RICHARD";
        }

        else if((r == 1 && c == 4) || (r == 4 && c == 1))
        {
            if(x == 1 || x == 2)
                result = "GABRIEL";
            else
                result = "RICHARD";
        }

        else if(r == 2 && c == 2)
        {
            if(x == 1 || x == 2)
                result = "GABRIEL";
            else
                result = "RICHARD";
        }

        else if((r == 2 && c == 3) || (r == 3 && c == 2))
        {
            if(x == 1 || x == 2 || x == 3)
                result = "GABRIEL";
            else
                result = "RICHARD";
        }

        else if((r == 2 && c == 4) || (r == 4 && c == 2))
        {
            if(x == 1 || x == 2)
                result = "GABRIEL";
            else
                result = "RICHARD";
        }

        else if(r == 3 && c == 3)
        {
            if(x == 1 || x == 3)
                result = "GABRIEL";
            else
                result = "RICHARD";
        }

        else if((r == 3 && c == 4) || (r == 4 && c == 3))
        {
            result = "GABRIEL";
        }

        else if(r == 4 && c == 4)
        {
            if(x == 1 || x == 2 || x == 4)
                result = "GABRIEL";
            else
                result = "RICHARD";
        }
//        cout << result << endl;
        outfile << "Case #"<<curTestCase+1<<": "<<result<<endl;
    }

    return 0;
}

