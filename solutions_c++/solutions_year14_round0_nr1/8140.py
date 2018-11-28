#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void megold(istream& in, ostream &out)
{
    int cards[4][4];
    int row;
    vector<int> p,q;

    //add
    in>>row;
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            in>>cards[i][j];
        }
    }
    for(int i=0; i<4; i++)
    {
        p.push_back(cards[row-1][i]);
    }

    //remove
    in>>row;
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            in>>cards[i][j];
        }
    }
    for(int i=0; i<4; i++)
    {
        if(find(p.begin(), p.end(), cards[row-1][i])!=p.end())
            q.push_back(cards[row-1][i]);
    }

    if(q.size()==0) out<<"Volunteer cheated!";
    else if(q.size()>1) out<<"Bad magician!";
    else out<<*q.begin();
}

int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("magician.out");
    int n;
    in>>n;
    for(int i=1; i<=n; i++)
    {
        out<<"Case #"<<i<<": ";
        megold(in, out);
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
