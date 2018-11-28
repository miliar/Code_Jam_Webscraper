#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int main()
{

    ifstream infile;
    ofstream outfile;
    infile.open ("A-large.in");
    outfile.open ("A-large.out");

    int n;
    infile>>n;
    for(int i=0; i<n; i++){
        outfile<<"Case #"<<i+1<<": ";
        int t;
        string shy;
        infile>>t>>shy;
        int num_need = 0;
        // Iterate all digits of the string, make sure the one with highest threshold will join standing ovation
        // Initialization
        int people = 0;
        int j = 0;
        while(j<=t)
        {
            int current_threshold = j;
            if(people<current_threshold)
            {
                num_need += (current_threshold - people);
                people = current_threshold;
            }
            people += shy.at(j) - '0';
            j++;
        }
        outfile<<num_need<<endl;
    }
}
