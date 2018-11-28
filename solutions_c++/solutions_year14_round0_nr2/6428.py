
/*
 * main.cc
 *
 *  Created on: Dec 12, 2009
 *      Author: Qian Xin
 *      DataStructure Java book 11.2.2
 */


#include <iostream>
#include <vector>
#include <set>
#include <iomanip>
#include <cassert>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <set>
using namespace std;

//#define debug_print(statement) do {std::cerr<<statement;} while(0)
#define debug_print(statement)

class TestCase
{
public:
    double C;
    double F;
    double X;
    double min;
    TestCase()
    {

    }
    //return 0 is success, other value is fail;
    int input(istream& in)
    {
        in>>C; in>>F; in>>X;
        return 0;
    }

    double cal()
    {
        vector<double> t;
        int i = 0;
        double t_sum = 0;
        while(1)
        {
            double speed = 2+ i*F;

            double tnow=C/speed;
            double snow = t_sum + X/speed;
            double snext = t_sum + tnow + X/(2+i*F+F);

            t_sum = t_sum + tnow;
            if (snow < snext)
            {
                min = snow;
                break;
            }
            i++;
            debug_print("i: "<<i<<", snow:"<<snow<<", snext:"<<snext<<endl);
        }

        return min;
    }


    void output(ostream& o) const
    {
        o <<min;
    }

};

inline ostream& operator<<(ostream& out, const TestCase& obj)
{
    obj.output(out);
    return out;
}

int main()
{
    fstream in_file;
    int case_count;
    int failed=0;

    istream& in=cin;

    in>>case_count;
    if (case_count<=0)
    {
        cerr<<"invalid case_count"<<case_count;
        failed=1;
        return 0;
    }

    for (int i = 1; i <= case_count; i++)
    {
        debug_print("case:"<<i<<"======================="<<endl);
        TestCase the_case;
        the_case.input(in);
        the_case.cal();
        printf("Case #%d: %9.8lf \r\n", i , the_case.min);
    }
    return 0;
}

