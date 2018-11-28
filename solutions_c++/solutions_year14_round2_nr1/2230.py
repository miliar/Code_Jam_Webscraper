#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

struct sequence {
    char chr;
    int db;
};

using namespace std;

void print(const vector<sequence>& v) {
    for(auto i : v) {
        cout << i.db << i.chr << " ";
    }
    cout << endl;
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for(int i=1;i<=t;++i) {
        int n;
        in >> n;
        vector<vector<sequence> > strings(n);
        for(int j=0;j<n;++j) {
            string tmp;
            in >> tmp;
            sequence seq;
            seq.chr = tmp[0];
            seq.db = 1;
            int pt=1;
            while(pt < tmp.length()) {
                if(tmp[pt] == seq.chr) {
                    ++pt;
                    ++seq.db;
                }
                else {
                    strings[j].push_back(seq);
                    seq.chr = tmp[pt];
                    seq.db = 1;
                    ++pt;
                }
            }
            strings[j].push_back(seq);
        }

        bool possible = true;
        for(int j=1;j<n && possible;++j) {
            if(strings[j].size() != strings[0].size()) {
                possible = false;
            }
        }
        for(int j=1;j<n && possible;++j) {
            for(int k=0;k<strings[0].size() && possible;++k) {
                if(strings[j][k].chr != strings[0][k].chr) {
                    possible = false;
                }
            }
        }
/*
for(int j=0;j<n;++j) {
    print(strings[j]);
}
*/
        out << "Case #" << i << ": ";
        if(possible) {
            int minAct = 0;
            for(int j=0;j<strings[0].size();++j) {
                vector<int> nums(n);
                int sum = 0;
                for(int k=0;k<n;++k) {
                    nums[k] = strings[k][j].db;
                    sum += nums[k];
                }
                sort(nums.begin(),nums.end());
                int pt = 0;
                int partSum = nums[0];
                while(partSum < sum/2) {
                    pt++;
                    partSum+=nums[pt];
                }
                for(int k=0;k<n;++k) {
                    minAct += abs(nums[pt] - strings[k][j].db);
                }
            }
            out << minAct << endl;
        }
        else {
            out << "Fegla Won" << endl;
        }
    }
    in.close();
    out.close();
    return 0;
}
