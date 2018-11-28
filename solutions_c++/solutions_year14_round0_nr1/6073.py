//#define NDEBUG
#include <thread>
#include <pthread.h>
#include <iostream>
#include <atomic>
#include <vector>
#include <array>
#include <functional>
#include <algorithm>
#include <ctime>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <cmath>
#include <stack>
#include <stdexcept>
#include <list>
#include <queue>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <utility>
#include <unordered_map>
#include <unordered_set>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <assert.h>
#include <typeinfo>

using namespace std;

class magician_testcase
{
private:
    int row1;
    int row2;
    vector<vector< int> > grid1;
    vector<vector< int> > grid2;

    friend class magician;
};

class magician
{
    int T;
    vector<magician_testcase> mt;

public:
    magician(string infilename)
    {
        //open file
        ifstream infile(infilename);
        assert(infile.good() == true);

        //store data in T and mt;
        infile>>T;
        for(int i=0;i<T; i++)
        {
            mt.push_back(read_nexttest(infile));
        }
    }

    magician_testcase read_nexttest(ifstream & infile)
    {
        magician_testcase t;
        int temp;

        //read the first grid with row
        infile>>t.row1;
        t.row1--; //change to 0-based indexing
        for(int i=0;i<4; i++)
        {
            t.grid1.push_back(vector<int>());
            for(int j=0;j<4;j++)
            {
                infile>>temp;
                t.grid1[i].push_back(temp);
            }
        }

        //read the second grid with row
        infile>>t.row2;
        t.row2--; //change to 0-based indexing
        for(int i=0;i<4; i++)
        {
            t.grid2.push_back(vector<int>());
            for(int j=0;j<4;j++)
            {
                infile>>temp;
                t.grid2[i].push_back(temp);
            }
        }

        return t;
    }

    void run(const string outfilename)
    {
        ofstream outfile(outfilename);
        assert(outfile.good() == true);

        //for each test case, make the output
        for(int i=0;i<T;i++)
        {
            printout(outfile, mt[i], i+1);
        }
    }

    void printout(ofstream & outfile, const magician_testcase & t, int testindex)
    {
        unordered_set<int> set_grid1;

        //put row1 of grid1 in set_grid
        for(int col = 0;col<4;col++)
            set_grid1.insert(t.grid1[t.row1][col]);

        //check which of the 3 outputs occur: how many times row2 of grid2 occurs in the set {0,1,1+}
        int num=0;
        int comon_num;

        for(int col = 0;col<4;col++)
            if(set_grid1.find(t.grid2[t.row2][col]) != set_grid1.end())
            {
                num++;
                comon_num = t.grid2[t.row2][col];
            }

        switch(num)
        {
        case 0:
            outfile<<"Case #"<<testindex<<": Volunteer cheated!\n";
            break;

        case 1:
            outfile<<"Case #"<<testindex<<": "<<comon_num<<"\n";
            break;

        default:
            outfile<<"Case #"<<testindex<<": Bad magician!\n";
            break;
        }
    }
};



int main(int argc, char * argv[])
{
    magician m("A-small-attempt0.in");
    m.run("A-small-attempt0.out");

	return 0;
}
















