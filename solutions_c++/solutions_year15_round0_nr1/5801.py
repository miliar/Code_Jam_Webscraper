#include <iostream>
#include <sstream>
#include <fstream>


using namespace std;

int makeint(char x)
{   int integer;
    stringstream ss;
    ss << x;
    ss >> integer;

    return integer;
}

int main()
{
    int i,T,friends,k,standing,people;

    ofstream outputfile;
    ifstream inputfile;
    outputfile.open("ASmall.txt");
    inputfile.open("A-large.in");
    string audience,j;
    inputfile >> T;
    for(i=1;i<=T;i++)
    {   inputfile >> j;
        inputfile >> audience;

        friends = 0;
        standing = 0;
        for(k=0;k<audience.length();k++)
        {
            people = makeint(audience.at(k));
            if (standing >= k) standing = standing + people;
            else{
                    friends = friends+(k-standing);
                    standing = standing + (k-standing) + people;
                }
        }
        outputfile << "Case #" << i << ": " << friends << endl;
    }

    return 0;
}
