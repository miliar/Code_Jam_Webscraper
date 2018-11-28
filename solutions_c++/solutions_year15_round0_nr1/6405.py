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

using namespace std;

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    
    string shy;
    int lines;

    int test_case,this_case=0;
    cin>>test_case;
    cin.ignore();
    
    
    while (this_case<test_case) {
        cin>>lines;
        cin>>shy;
        int sum=shy[0]-'0', needed = 0;
        for (int i=1; i<lines+1; i++) {
            if (shy[i]-'0' >0 ) {
//                cout<<"i "<<i<<" shy[i] "<<shy[i]<<" sum "<<sum<<endl;
                if (sum<i) {
                    needed += i-sum;
                    sum = i;
                }
                sum += shy[i]-'0';
            }
        }
        
        cout<<"Case #"<<this_case+1<<": "<<needed<<endl;
        this_case++;
    }
    
    
    
    return 0;
}