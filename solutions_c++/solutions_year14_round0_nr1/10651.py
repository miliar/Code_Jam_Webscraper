#include <cstdio>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <istream>
#include <sstream>
#include <cstdlib>
#define EOF (-1)

using namespace std;

int main()

{

    ofstream out;
    out.open("out.txt");
    ifstream fin;
     fin.open("A-small-attempt5.in");
     stringstream ss;

    int l1[4], l2[4], line1, line2;
    char str[20];
    vector<int> verify;


    int cases;

    int j, k, a, test;
    fin.get(str, 20, '\n');
    cases = atoi(str);



    for(int i = 0 ; i < cases; i++)

    {
        fin.get();
        line1 = fin.get();
        fin.get();



        for( j = 0; j < line1 - '0' - 1; j++)
        {

            fin.get(str, 20, '\n');
            fin.get();
        }


            fin.get(str, 20, '\n');
            ss << str;
            ss >> l1[0] >> l1[1] >> l1[2] >> l1[3];
            ss.clear();
            ss.str("");

        for(j = 0; j < 4 - (line1 - '0'); j++)
        {   fin.get();
            fin.get(str, 20, '\n');




        }





        fin.get();
        line2 = fin.get();
        fin.get();



        for( j = 0; j < line2 - '0' - 1; j++)
        {

            fin.get(str, 20, '\n');
            fin.get();


        }

            fin.get(str, 20, '\n');
            ss << str;
            ss >> l2[0] >> l2[1] >> l2[2] >> l2[3];
            ss.clear();
            ss.str("");

        for(j = 0; j < 4 - (line2 - '0'); j++)
        {   fin.get();
            fin.get(str, 20, '\n');


        }


    for(j = 0; j < 4; j++)
    {
        for(k = 0; k < 4; k++)
        {
            if (l1[j] == l2[k] )
                verify.push_back(l1[j]);
        }
    }
    if (verify.empty() == true)
    {
        out << "Case #" << i + 1 << ": Volunteer cheated!\n";
    }

    else if (verify.size() > 1)
    {
        out << "Case #" << i + 1 << ": Bad magician!\n";
    }

    else if (verify.size() == 1)
     {
        out << "Case #" << i + 1 << ": " << verify[0] << "\n";
    }
    verify.clear();
    }


fin.close();
out.close();
return 0;
}
