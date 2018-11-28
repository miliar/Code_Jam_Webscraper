#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <numeric>
using namespace std;
bool keep[10];
bool keepAll(){
    for(int i = 0; i < 10; ++i)
        if(!keep[i])
            return false;
    return true;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T, N;
    cin >> T;
    for(int i = 1; i <= T; ++i){
        for(int i = 0; i < 10; ++i)
            keep[i] = false;
        cin >> N;
        if(N == 0)
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        int tmp1 = N;
        int tmp = N;
        for(int j = 0; j < 200; ++j){
            tmp = (j + 1)*tmp1;
            while(tmp > 0){
                keep[tmp % 10] = true;
                tmp/=10;
            }
            if(keepAll())
            {
                cout<<"Case #"<<i<<": "<<(j+1)*tmp1<<endl;
                break;
            }
        }
    }
    return 0;
}
