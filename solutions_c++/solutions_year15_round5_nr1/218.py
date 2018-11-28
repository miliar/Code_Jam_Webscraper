#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

void readData(int n, vector<int>& v)
{
    int init, a, c, r;
    cin >> init >> a >> c >> r;

    v.resize(n);
    v[0] = init;
    for(int i=1; i<n; ++i)
        v[i] = (v[i-1] * a + c) % r;
}

class Data
{
public:
    int id, salary, manager;
    Data(){
    }
    Data(int id, int salary, int manager){
        this->id = id;
        this->salary = salary;
        this->manager = manager;
    }
    bool operator<(const Data& d) const{
        return salary < d.salary;
    }
};

int solve(int n, int d, const vector<int>& salary, const vector<int>& manager)
{
    vector<Data> v(n);
    for(int i=0; i<n; ++i)
        v[i] = Data(i, salary[i], manager[i]);
    auto v2 = v;
    sort(v2.begin(), v2.end());

    int j = 0;
    vector<bool> used(n, false);
    int ans = 0;
    for(int i=0; i<n; ++i){
        while(j < n && v2[j].salary - v2[i].salary <= d){
            used[v2[j].id] = true;
            ++ j;
        }
        if(used[0]){
            int cnt = 0;
            for(int k=0; k<n; ++k){
                int id = k;
                while(id != 0 && used[id])
                    id = v[id].manager;
                if(id == 0)
                    ++ cnt;
            }
            ans = max(ans, cnt);
        }
        used[v2[i].id] = false;
    }

    return ans;
}

int main()
{
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        int n, d;
        cin >> n >> d;

        vector<int> salary, manager;
        readData(n, salary);
        readData(n, manager);
        for(int i=1; i<n; ++i)
            manager[i] = manager[i] % i;

        cout << "Case #" << t << ": " << solve(n, d, salary, manager) << endl;
    }
}