#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

string find_card(int row1[4],int row2[4])
{
    vector<int> common;

    for(int i =0;i<4;++i)
    {
        for(int j=0;j<4;++j)
        {
            if(row1[i] == row2[j])
            {
                common.push_back(row1[i]);
                break;
            }
        }
    }

    ostringstream str;

    switch(common.size())
    {
        case 0:
            return "Volunteer cheated!";

        case 1:
            str << common[0];
            return str.str();

        default:
            return "Bad magician!";
    }
}

int main()
{
    int n_test;
    int choice1,choice2;
    int arrange1[4][4],arrange2[4][4];

    ifstream in("A-small-attempt2.in");
    ofstream out("results.txt");

    in >> n_test;

    for(int i=0;i<n_test;++i)
    {
        in >> choice1;

        for(int j=0;j<4;++j)
            for(int k=0;k<4;++k)
                in >> arrange1[j][k];

        in >> choice2;

        for(int j=0;j<4;++j)
            for(int k=0;k<4;++k)
                in >> arrange2[j][k];

        out << "Case #"<<i+1<<": "<<find_card(arrange1[choice1-1],arrange2[choice2-1])<<endl;

    }

}
