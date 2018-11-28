#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

/****************************************************/
class Problem{
    public:
        void getInput();
        void putOutput();
        void solve();
        /* Global Variables Here */
        int a, b;
        vector<vector<int> > va;
        vector<vector<int> > vb;
        vector<int> common;
};

/************************/
/* Get Input            */
/************************/
void Problem::getInput()
{
    cin>>a;
    for(int i=0;i<4;i++) {
        vector<int> tv;
        int t;
        for(int j=0;j<4;j++) {
            cin>>t;
            tv.push_back(t);
        }
        va.push_back(tv);
    }
    cin>>b;
    for(int i=0;i<4;i++) {
        vector<int> tv;
        int t;
        for(int j=0;j<4;j++) {
            cin>>t;
            tv.push_back(t);
        }
        vb.push_back(tv);
    }
}

/************************/
/* Print Output         */
/************************/
void Problem::putOutput()
{
    string result = "";
    switch (common.size()) {
        case 0:
            result = "Volunteer cheated!";
            break;
        case 1:
            break;
        default:
            result = "Bad magician!";
            break;
    }
    if(common.size()==1)
        cout<<common[0]<<endl;
    else
        cout<<result<<endl;
}
 
/************************/
/* Solve                */
/************************/
void Problem::solve()
{
    vector<int> cc(8);
    common = cc;
    vector<int> r1;
    vector<int> r2;
    r1 = va[a-1];
    r2 = vb[b-1];
    sort(r1.begin(), r1.end());
    sort(r2.begin(), r2.end());
    vector<int>::iterator iter;
    iter = set_intersection(r1.begin(), r1.end(), r2.begin(), r2.end(), common.begin());
    common.resize(iter-common.begin());
}

/****************************************************/

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        Problem p;
        p.getInput();
        p.solve();
        p.putOutput();
    }
    return 0;
}
