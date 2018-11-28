#include <fstream>

using namespace std;

const int SMAX = 1<<10;

int a[SMAX], s, T;
char str[SMAX];

int main(){
    ifstream cin("C:\\Users\\user\\Downloads\\A-large.in");
    ofstream cout("C:\\Users\\user\\Downloads\\sv-large.out");
    cin >> T; for(int t = 1; t <= T; t++){
        cin >> s; int ans = 0;
        cin >> str;
        for(int i = 0; i <= s; i++) a[i] = str[i]-'0';
        for(int i = 1; i <= s; i++){
            int sum = 0;
            for(int j = 0; j < i; j++)
                sum += a[j];
            if(sum < i) a[0] += i-sum, ans += i-sum;
        }
        cout << "Case #" << t << ": " << ans << '\n';
    }
    return 0;
}
