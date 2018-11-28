#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int C = 1; C <= T; C++){
        //cout << C << endl;
        string res;
        int partiesCount;
        cin >> partiesCount;

        vector<pair<int, char>> members;
        for(int i = 0; i < partiesCount; i++){
            int temp;
            cin >> temp;
            members.emplace_back(temp,'A'+i);
        }

        make_heap(members.begin(), members.end());
        while(members.size() > 2 || members[0].first != members[1].first) {
            //cout << "size: " << members.size() << endl;
            //cout << ", second: " << members[1].second << " " << members[1].first << endl;
            //cout << "first: " << members[0].second << " " << members[0].first;
            pop_heap(members.begin(), members.end());
            res += members.back().second;
            res += ' ';
            if (--(members.back().first) == 0)
                members.pop_back();
            else
                push_heap(members.begin(), members.end());
        }
        string remain;
        remain += members[0].second;
        remain += members[1].second;
        remain += " ";
        for(int i = 0; i < members[0].first; i++){
            res += remain;
        }

        res.resize(res.size()-1);

        cout << "Case #" << C << ": " << res << endl;
    }
    return 0;
}
