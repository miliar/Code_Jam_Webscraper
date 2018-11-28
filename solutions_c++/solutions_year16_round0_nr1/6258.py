#include <cstdio>
#include <iostream> 
#include <algorithm>
#include <map>
using namespace std;
char digit[10];
int main()
{
    int t;
    int kase;
    long long d,n;
    long long r;
    int cnt, prev;
    int i;
    cin >> t;
    for(kase = 1; kase <= t;kase++) {
        memset(digit,0,sizeof digit);
        map<long long, int> dic;
        cnt = 0;
        char str[10];
        cin >> n;
        d = 1;
        do {
            r = d * n;
            if (dic[r] == 1)
                break;
            sprintf(str,"%lld", r);
            int len = strlen(str);
            for(i=0;i<len;i++) {
                if (digit[str[i] - '0'] == 0) {
                    digit[str[i]-'0'] = 1;
                    cnt++;
                }
            }
            dic[r] = 1;
            d++;
        }while(cnt != 10);
        cout << "Case #" << kase <<": ";
        if (cnt != 10) cout << "INSOMNIA" <<endl;
        else cout << r << endl;
    }
    return 0;
}
