#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;


void readrows(set<int>& res)
{
    int index;
    cin >> index;
    int tmp;
    for(int j=0; j<4; ++j)
    {
        for(int k=0; k<4; ++k)
        {
            cin >> tmp;
            if ( index == (j+1) )
            {
                res.insert(tmp);
            }
        }
    }
    return;
}

int main()
{
    int ncases;
    cin >> ncases;
    for(int i=0; i<ncases; ++i)
    {
        set<int> frow;
        set<int> srow;
        
        readrows(frow); 
        readrows(srow); 

        std::vector<int> intersect(10);
        std::vector<int>::iterator it;

        it = set_intersection (frow.begin(), frow.end(), srow.begin(), srow.end(), intersect.begin());
        intersect.resize(it-intersect.begin());

        cout << "Case #" << i+1 << ": ";
        if (intersect.size() == 1)
        {
            cout << *intersect.begin() << endl;
        }
        else if (intersect.empty())
        {
            cout << "Volunteer cheated!" << endl;
        }
        else if (intersect.size() > 1)
        {
            cout << "Bad magician!" << endl;
        }
    }

    return 0;
}
