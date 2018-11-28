#include <iostream>
#include <cstdio>
#include <vector>
#include <bitset>
using namespace std;

long long check(int base, int v){
    long long pow = 1;
    long long res = 0;
    for(int i = 0; i < 16; i++){
        res += ((v & (1 << i)) >> i)*pow;
        pow *= base;
    }
    for(long long i = 2; i*i <= res; i++){
        if(res%i == 0){
            return i;
        }
    }
    return -1;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //freopen("input.txt", "w", stdout);

    cin.tie(NULL);
    ios::sync_with_stdio(false);
    cout << "Case #1:" << endl;
    for(int i = 0; i < 500; i++){
        string s, tmp;
        cin >> s;
        cout << s << s<< " ";
        for(int i = 0; i < 9; i++){
            cin >> tmp;
            cout << tmp << " ";
        }
        cout << endl;
    }

    /*int tot = 0;
    for(int i = (1 << 15) + 1; (i < (1 << 16)) && tot < 600; i+= 2){
        long long tmp = 1;
        vector<long long> res;
        for(int j = 2; (j <= 10) && (tmp > 0); j++){
            tmp = check(j, i);
            res.push_back(tmp);
        }
        if(tmp > 0){
            cout << bitset<16>(i) << " ";
            for(int j = 0; j < res.size(); j++){
                cout << res[j] << " ";
            }
            cout << endl;
            tot ++;
        }
    }*/

    return 0;
}
