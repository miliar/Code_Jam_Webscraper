#include <iostream>
#include <set>

using namespace std;


pair<int,int> readRow(set<int> & row,int rowsize = 4)
{
    int rep = 0;
    int tmp=0, number=0;

    typedef pair<set<int>::iterator,bool> retval;

    retval retinsert;
    while(rowsize--)
    {
        cin >> tmp;
        retinsert = row.insert(tmp);
        if(!retinsert.second)
        {
            number = tmp;
            ++rep;
        }
    }

    return std::make_pair(rep,number);
}

void skipRow(int times, int rowsize=4)
{
    int tmp,r = rowsize;
    while(times--)
    {
        while(r--)
            cin >> tmp;
        r= rowsize;
    }
}

int main(int argc, char *argv[])
{
    int T=0,casen =1;
    cin >> T;

    int row;

    while(T--)
    {
        set<int> uniqueset;
        cout << "Case #" << (casen++) << ": ";

        //first answer
        cin >> row;

        //square grid: save cards
        skipRow(row-1);
        readRow(uniqueset);
        skipRow(4-row);

        //second answer
        cin >> row;

        //square grid: compare cards
        skipRow(row-1);
        pair<int,int> foundp;
        foundp = readRow(uniqueset);
        skipRow(4-row);

        //elaborate the output
        int found = foundp.first;
        int lastfound = foundp.second;

        if(found == 0)
          cout << "Volunteer cheated!" << endl;
        else if(found == 1)
          cout << lastfound << endl;
        else
          cout << "Bad magician!" << endl;

    }
}
