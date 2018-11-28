#include <iostream>
#include <cstdio>
#include <vector>
#include <sstream>

using namespace std;


int main() {
    int n;
    cin >> n;
    for(int ii = 1; ii<=n; ++ii) {
        string p;
        cin >> p;
        printf("Case #%d: ",ii);

        int times = 0;
        if(p.size() == 0) {
            cout<<0<<endl;
            break;
        }

        vector<int> nums;
        for(int i = 0; ; ) {
            if(p[i] == '+') {
                nums.push_back(+1);
                while(++i < p.size() && p[i] == '+') { }
            }
            else {
                nums.push_back(-1);
                while(++i < p.size() && p[i] == '-') { }
            }
            if(i == p.size()) break;
        }
        if(nums[nums.size()-1] == +1) nums.pop_back();

        cout<<nums.size()<<endl;
    }
    return 0;
}
