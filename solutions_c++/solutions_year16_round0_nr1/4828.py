#include <iostream>
#include <vector>
//#include <algorithm>
//#include <string>
//#include <stack>
//#include <unordered_map>
//#include <limits.h>
//#include <time.h>
//#include <queue>
using namespace std;


int process(vector<bool> & record, long num){
    long long i = 10;
    long long temp;
    while(i <= num * 10){
        temp = (num % i) / (i / 10);
        record[temp] = 1;
        i *= 10;
    }
    for(int j = 0; j < record.size(); ++j){
        if(record[j] == 0) return 0;
    }
    return 1;
}

int main(){
    int t; cin >> t;
    for(int z = 0; z < t; ++z){
        long long n;
        cin >> n;
        if(n == 0){
            cout << "Case #" << z + 1 << ": INSOMNIA" << endl;
            continue;
        }
        vector<bool> record(10);
        long long temp = n;
        while(!process(record, temp))
            temp += n;
        cout << "Case #" << z + 1 << ": " << temp << endl;
        //for_each(record.begin(), record.end(), [](const bool & a)->void{ cout << a << " "; });
    }
}