// Fair and Square problem for the Google Code Jam
// Solution by 64Mega

#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

struct range
{
    long int a;
    long int b;
};

vector<range> cases;

void readfile(string fname)
{
    ifstream in(fname);
    if(!in.is_open())
    {
        cout << "ERROR OPENING FILE" << endl;
        abort();
    }

    // Read number of test cases
    int num = 0;
    in >> num;
    cout << "Number of test cases: " << num;

    for(int i = 0; i < num; i++)
    {
        range t;
        in >> t.a >> t.b;
        cout << t.a << " " << t.b << endl;
        cases.push_back(t);
    }

    in.close();
}

int main(int argc, char** argv)
{
    readfile("input.txt");

    vector<int> count;

    // Start processing
    for(int i = 0; i < cases.size(); i++)
    {

        //s.clear();
        long n = 0;

        for(long int a = cases[i].a; a <= cases[i].b; a++)
        {
            stringstream s;
            s << (int)a;
            string cs = s.str();

            if(cs[0] != cs.back())continue;
            //else cout << "PALINDROME: " << cs << endl;

            double sq = sqrt(a);
            double it = 0;
            if(modf(sq,&it)!= 0.0F)continue;
            stringstream q;
            q << sq;
            cs = q.str();

            if(cs[0] != cs.back())continue;

            cout << "PALINDROME (SQUARE): " << cs << endl;
            n++;
        }

        count.push_back(n);
    }

    ofstream out("c_output.txt");
    for(int i = 0; i < count.size(); i++)
    {
        out << "Case #" << i+1 << ": ";
        out << count[i] << endl;
    }
    out.close();
}
