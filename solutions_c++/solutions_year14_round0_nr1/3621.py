#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main()
{
    ifstream input;
    input.open("small.txt");
    ofstream output;
    output.open("smallo.txt");
    int t;
    input>>t;
    for (int cse=1;cse<=t;cse++)
    {
        int row;
        input>>row;
        vector <int> group;
        vector <int> group1;
        for (int i=1;i<=16;i++)
        {
            if(i<4*row-3||i>4*row)
            {
            int z;
            input>>z;
            }
            else{
                    int z;
            input>>z;
                group.push_back(z);
            }
        }

        input>>row;

        for (int i=1;i<=16;i++)
        {
            if(i<4*row-3||i>4*row)
            {
            int z;
            input>>z;
            }
            else{
                    int z;
            input>>z;
                group1.push_back(z);
            }
        }
        sort(group1.begin(),group1.end());
        sort(group.begin(),group.end());

        vector<int>::iterator it;
        vector <int> emp(8);
        it=set_intersection (group.begin(),group.end(),group1.begin(),group1.end(), emp.begin());
        emp.resize(it-emp.begin());
        output<<"Case #"<<cse<<": ";
        if(emp.size()==0)
        {
            output<<"Volunteer cheated!"<<endl;
        }
        if(emp.size()==1)
        {
            output<<emp[0]<<endl;
        }
        if(emp.size()>1)
        {
            output<<"Bad magician!"<<endl;
        }




    }

    return 0;

}
