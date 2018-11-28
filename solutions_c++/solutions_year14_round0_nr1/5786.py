#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main(int argc, const char * argv[])
{
    
    fstream infile;
    infile.open("A-small-attempt0.in");
    ofstream outfile;
    outfile.open("A-small.out");
    int num;
    infile>>num;
    for(int i = 0;i < num;i++) {
        unordered_set<int> s;
        vector<int> v;
        int row;
        infile>>row;
        for(int j = 0;j < 4;j++) {
            for(int k = 0;k < 4;k++) {
                int n;
                infile>>n;
                if(j == row-1) {
                    s.insert(n);
                }
            }
        }
        infile>>row;
        for(int j = 0;j < 4;j++) {
            for(int k = 0;k < 4;k++) {
                int n;
                infile>>n;
                if(j == row-1) {
                    v.push_back(n);
                }
            }
        }
        int count = 0;
        int res;
        for(int j = 0;j < 4;j++) {
            if(s.find(v[j]) != s.end()) {
                count++;
                res = v[j];
            }
        }
        if(count == 1) {
            outfile<<"Case #"<<i+1<<": "<<res<<endl;
        } else if(count > 1) {
            outfile<<"Case #"<<i+1<<": Bad magician!"<<endl;
        } else {
            outfile<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }
    }
    outfile.close();
    infile.close();
    return 0;
}