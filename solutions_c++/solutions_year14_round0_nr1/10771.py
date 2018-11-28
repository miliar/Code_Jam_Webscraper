#include <iostream>
#include <iterator>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    int t; cin >> t;
    for(int c = 1; c<=t; c++ ){
        string result;
        int f1; cin >> f1;
        vector<set<int>> v1;
        for (int i = 0; i < 4; ++i){
            set<int> f;
            int v;
            
            cin >> v;
            f.insert(v);
            cin >> v;
            f.insert(v);
            cin >> v;
            f.insert(v);
            cin >> v;
            f.insert(v);
            v1.push_back(f);
        }
        

         int f2; cin >> f2;
        vector<set<int>> v2;
        for (int i = 0; i < 4; ++i){
            set<int> f;
            int v;
            
            cin >> v;
            f.insert(v);
            cin >> v;
            f.insert(v);
            cin >> v;
            f.insert(v);
            cin >> v;
            f.insert(v);
            v2.push_back(f);
        }

        set<int> &s1 = v1[f1-1];
        set<int> &s2 = v2[f2-1];

        set<int> A;
        set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),
                          std::inserter(A,A.begin()));

        if (A.size() == 0) result = "Volunteer cheated!";
        if (A.size() == 1) result = to_string(*A.begin());
        if (A.size() > 1) result = "Bad magician!";

        cout << "Case #" << c << ": " << result << endl;
    }



    return 0;
}