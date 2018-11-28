#include <bits/stdc++.h>
#define MAX 100005
#define mp make_pair
#define pb push_back
#define rep(a) for(i=0;i<a;i++)
#define loop(a,b) for(i=a;i<b;i++)
#define ll long long int
#define MOD 1000000007

using namespace std;

/*int input () {
    int ip = getchar_unlocked(), ret = 0, flag = 1;
    for ( ; ip < '0' || ip > '9'; ip = getchar_unlocked())
        if (ip == '-') {
            flag = -1;
            ip = getchar_unlocked();
            break;
        }
    for ( ; ip >= '0' && ip <= '9'; ip = getchar_unlocked())
        ret = ret * 10 + ip - '0';
    return flag * ret;
}

void print (int n) {
    if (n < 0) {
        n = -n;
        putchar_unlocked('-');
    }
    int i = 10;
    char output_buffer[10];
    do {
        output_buffer[--i] = (n % 10) + '0';
        n /= 10;
    } while (n);
    do {
        putchar_unlocked(output_buffer[i]);
    } while (++i < 10);
}
*/

int main() {
    freopen("B-large.in","r", stdin);
    freopen("output.txt", "w", stdout);
    int t, tt, i, cnt;
    string s;
    scanf("%d\n", &t);
    tt = t;
    while (t--) {
    	cnt = 0;
        cin>>s;
        int l = s.size();
        //cout<<l<<endl;
        for (int i = 1; i < l; i++) {
        	if (s[i] != s[i-1]) {
        		cnt++;
        	}
        }
        if (s[l-1] == '-') {
        	printf("Case #%d: %d\n", tt-t, cnt+1);
        }
        else {
        	printf("Case #%d: %d\n", tt-t, cnt);
        }
    }
    return 0;
}
