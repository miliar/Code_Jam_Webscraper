/* AUTHOR: TARASHA KHURANA
** PROBLEM: CC/STROPR
*/

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
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, tt, n, num;
    int arr[100005];
    scanf("%d\n", &t);
    tt=t;
    while (t--) {
        memset(arr, 0, sizeof arr);
        scanf("%d\n", &n);
        for (int i = 0; i < (2*n)-1; i++) {
        	for (int j = 0; j < n; j++) {
        		scanf("%d\n", &num);
        		arr[num]++;
        	}
        }
        cout<<"Case #"<<(tt-t)<<": ";
        for (int i = 0; i < 100005; i++) {
        	if (arr[i]%2 == 1) {
        		printf("%d ", i);
        	}
        }
        printf("\n");
    }
    return 0;
}
