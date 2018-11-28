#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

int N, T;

int digs[10];

bool alldigs()
{
    bool a = true;
    for (int i = 0; i < 10; i++){
        if (digs[i] == 0){
            a = false;
        }
    }
    return a;
}


int main()
{
    freopen("/Users/yan/Documents/Prep/codeJame/countingSheepLarge.txt", "r", stdin);
    freopen("/Users/yan/Documents/Prep/CodeJame/OUT.txt","w", stdout);

    cin >> T;
    for (int x = 1; x <= T; x++){
        cin >> N;
        string num;
        int current = N;
        int i = 1;

        while (!alldigs())
        {

            current = N*i;

            num = to_string(current);
            for (int j = 0; j < num.size(); j++){
                digs[num[j]-'0']++;
            }

            if (N*(i+1) == N){
                current = -1;
                break;
            }

            i++;
        }

        memset(digs, 0, sizeof(digs));
        if (current > 0) cout << "Case #" << x << ": " << current << endl;
        else cout << "Case #" << x << ": INSOMNIA" << endl;
    }

}
