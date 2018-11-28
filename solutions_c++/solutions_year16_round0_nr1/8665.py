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
ll num[10], cnt = 0, ctr = 1, i, newnum, tt,t;

void lookinto (ll numb) {
	ll dig;
	while (numb > 0) {
		dig = numb%10;
		//cout<<"dig = "<<dig<<endl;
		numb /= 10;
		if (num[dig] == 0) {
			cnt++;
			num[dig] = 1;
		}
	/*rep(10) {
			cout<<"i = "<<i<<" " <<num[i]<<endl;
		}*/
	}
	if (cnt == 10) {
		printf("Case #%lld: %lld\n", tt-t, newnum);
	}
}

int main() {
	freopen("A-large.in","r", stdin);
    freopen("output.txt", "w", stdout);
    ll number;
    scanf("%lld\n", &t);
    tt = t;
    while (t--) {
        memset(num, 0, sizeof num);
        cin>>number;
        if (number == 0) {
        	printf("Case #%lld: INSOMNIA\n", tt-t);
        }
        else {
      		cnt = 0;
      		ctr = 1;
        	while (cnt < 10) {
        		if (cnt == 10) {
        			break;
        		}
        		newnum = number*ctr;
        		//cout<<"This is newnum = "<<newnum<<endl;
        		lookinto(newnum);
        		ctr++;
        	}
        }
    }
    return 0;
}
