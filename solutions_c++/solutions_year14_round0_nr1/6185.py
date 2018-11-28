

#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

void
readCards(ifstream& f, std::set<int>& s)
{   
    int r = 0;
    f >> r;
    for (int i = 1; i <= 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            int a = 0;
            f >> a;
            if (i == r) {
               s.insert(a);
            }
        }
    }
}

int main()
{
    ifstream infile("file.in");
    ofstream outfile("file.out");
    
    int nCase = 0;
    infile >> nCase;
    
    for (int c = 1; c <= nCase; ++c) {
        
        std::set<int> set1;
        readCards(infile, set1);
        
        std::set<int> set2;
        readCards(infile, set2);
        
        std::vector<int> res(std::max(set1.size(), set2.size()));
        std::vector<int>::const_iterator it = set_intersection(set1.begin(), 
                                    set1.end(), set2.begin(), set2.end(),
                                    res.begin());
        int size = it - res.begin();
        
        outfile << "Case #" << c << ": ";
        if (size == 1) {
           outfile << res.front() << endl;
        }
        else if (size == 0) {
           outfile << "Volunteer cheated!" << endl;
        }
        else {
           outfile << "Bad magician!" << endl;
        }
    }
    
    infile.close();
    outfile.close();
}
