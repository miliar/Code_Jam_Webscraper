#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <deque>
#include <limits.h>
#include <algorithm>
using namespace std;

int main(void){
#ifndef ONLINE_JUDGE
  freopen("d://A-small-attempt0.in", "r", stdin);
#endif
    int T, n, sum, need;
    string people;
    cin >> T;
    for(int i = 0; i < T; i++){
        sum = need = 0;
        cin >> n >> people;
        for(int j = 0; j < people.size(); j++){
            if(sum >= j){
              sum += people[j]-'0';
            }
            else{
              need += j-sum;
              sum = j+people[j]-'0';
            }
        }
        cout << "Case #" << i+1 << ": " << need << endl;
    }
    return 0;
}