
/*
 * main.cc
 *
 *  Created on: Dec 12, 2009
 *      Author: Qian Xin
 *      DataStructure Java book 11.2.2
 */

#include "xinqian.h"

int debug_level = 0;

int main()
{
    fstream in_file;
    int case_count;
    int failed=0;

    //in_file.open ("C-large.in", fstream::in);

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
        cout<<"Case #"<<i<<": ";
        if (the_case.result > 0)
            cout<<the_case.result;
        else if (the_case.result == -1)
            cout<<"Volunteer cheated!";
        else if (the_case.result == -2)
            cout<<"Bad magician!";
        cout<<endl;
    }
    return 0;
}

