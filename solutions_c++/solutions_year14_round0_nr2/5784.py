#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main(int argc, const char * argv[])
{
    
    fstream infile;
    infile.open("B-large.in");
    ofstream outfile;
    outfile.open("A-small.out");
    int num;
    infile>>num;
    outfile.precision(7);
    outfile.setf(ios::fixed, ios::floatfield);
    for(int i = 0;i < num;i++) {
        double c,f,x;
        infile>>c>>f>>x;
        vector<double> time;
        double curr = 2.0;
        while(x/curr > (c/curr + x/(curr+f))) {
            time.push_back(c/curr);
            curr = curr + f;
        }
        time.push_back(x/curr);
        double res = 0.0;
        for(int j = 0;j < time.size();j++) {
            res += time[j];
        }
        outfile<<"Case #"<<i+1<<": "<<res<<endl;
    }
    outfile.close();
    infile.close();
    return 0;
}