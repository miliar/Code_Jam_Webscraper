#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;

long long get_high(long long A, long long value, long long &tempcount){
    long long arbit = A;
    long long count = 0;
    if(A == 1){
        tempcount = 1000000;
        return A - 1;
    }
    else{
    while(arbit <= value){
        arbit = 2 * arbit - 1;
        count++;
    }
    }
    tempcount = count;
    return arbit;

}

int main(){
    long long t;
    cin>>t;
    for(long long te = 0; te < t; te++){
        long long A;
        cin>>A;
        long long n;
        cin>>n;
        vector<long long> values(n, 0);
        for(int i=0; i < n;i++)
            cin>>values[i];

        sort(values.begin(), values.end());
        long long count = 0;
        for(int i=0; i < n;i++){
            if(A > values[i])
                A += values[i];
            else{
                long long tempcount = 0;
                long long temp = get_high(A, values[i], tempcount);
                if(tempcount <  n - i){
                    count += tempcount;
                    A = temp + values[i];
                }
                else{
                    count += n - i;
                    break;
                }

            }
        }
        cout<<"Case #"<<te+1<<": "<<count<<endl;



    }
}

