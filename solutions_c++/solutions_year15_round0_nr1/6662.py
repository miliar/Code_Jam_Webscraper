#include "j.h"

int ovation(int maxShyness, string &s) {
    int sum = 0;
    int added = 0;
    for(int i = 0; i < s.size(); i++) {
        if(s[i]-48 == 0)
            continue;
        int diff = sum - i;
        //printf("At index %d, num available is %d, num needed is %d\n", i, sum, i);
        if(diff >= 0) {
            sum += s[i]-48;
            continue;
        }
        else {
            //printf("Added %d at i = %d\n", i-sum, i);
            added += i-sum;
            sum += added + s[i]-48;
        }
    }
    return added;
}


int main() {
    int c = readSingleFromCin<int>();
    FE(ic, 1, c) {
        int ans = 0;
        int maxShyness;
        string s;
        cin >> maxShyness;
        cin >> s;
        //cout << "Max is: " << maxShyness << " and array is " << s << endl;
        //vector<float> v = readNumbersFromCin<float>();
        printf("Case #%d: %d\n", ic, ovation(maxShyness, s));
    }
}
