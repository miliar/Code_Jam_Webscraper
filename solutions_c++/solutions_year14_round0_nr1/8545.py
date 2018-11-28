#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>


using namespace std;


int main()
{
    int T;
    int n,x;
    ifstream in("A-small-attempt0.in");
    ofstream out("out.txt");
    vector<int> row1;
    vector<int> row2;
    vector<int> intersection(8);
    vector<int>::iterator it;

    in>>T;
    for(int j=1;j<=T;j++)
    {
        in>>n;
        for(int i=0;i<(n-1)*4;i++)
            in>>x;

        for(int i=0;i<4;i++)
        {
            in>>x;
            row1.push_back(x);
        }

        for(int i = n*4; i<16;i++)
            in>>x;

        in>>n;
        for(int i=0;i<(n-1)*4;i++)
            in>>x;

        for(int i=0;i<4;i++)
        {
            in>>x;
            row2.push_back(x);
        }
        for(int i = n*4; i<16;i++)
            in>>x;


        sort(row1.begin(),row1.end());
        sort(row2.begin(),row2.end());
        it = set_intersection(row1.begin(),row1.end(),row2.begin(),row2.end(),intersection.begin());
        intersection.resize(it - intersection.begin());

        
        switch(intersection.size())
        {
        case 0:
            out<<"Case #"<<j<<": "<<"Volunteer cheated!\n";
            break;
        case 1:
            out<<"Case #"<<j<<": "<<intersection[0]<<"\n";
            break;
        default:
            out<<"Case #"<<j<<": "<<"Bad magician!\n";
            break;
        }
        intersection.clear();
        intersection.resize(8);
        row1.clear();
        row2.clear();

            
    }
}

