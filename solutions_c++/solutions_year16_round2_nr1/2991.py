/*
** AUTHOR: TARASHA KHURANA
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
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, tt, ctr, len;
    int num[10], arr[26];
    string s;
    scanf("%d\n", &t);
    tt =t;
    while (t--) {
        cin>>s;
        ctr = 0;
        len = 0;
        memset(num, 0, sizeof num);
        memset(arr, 0, sizeof arr);
        for (int i = 0; s[i] !='\0'; i++) {
        	arr[s[i] - 'A']++;
        	len++;
        }

        while (ctr < len) {
        //cout<<ctr;
        if (arr['G' - 'A']) {
        	num[8]++;
        	ctr+=5;
        	arr['E' - 'A']--;
        	arr['I' - 'A']--;
        	arr['G' - 'A']--;
        	arr['H' - 'A']--;
        	arr['T' - 'A']--;
        }
        else if (arr['Z' - 'A']) {
        	num[0]++;
        	ctr+=4;
        	arr['Z' - 'A']--;
        	arr['E' - 'A']--;
        	arr['R' - 'A']--;
        	arr['O' - 'A']--;
        }
        else if (arr['X' - 'A']) {
        	num[6]++;
        	ctr+=3;
        	arr['X' - 'A']--;
        	arr['S' - 'A']--;
        	arr['I' - 'A']--;
        }
        else if (arr['W' - 'A']) {
        	num[2]++;
        	ctr+=3;
        	arr['W' - 'A']--;
        	arr['T' - 'A']--;
        	arr['O' - 'A']--;
        }
        else if (arr['H' - 'A']) {
        	num[3]++;
        	arr['H' - 'A']--;
        	arr['T' - 'A']--;
        	arr['R' - 'A']--;
        	arr['E' - 'A']--;
        	arr['E' - 'A']--;
        	ctr+=5;
        }
        else if (arr['R' - 'A']) {
        	num[4]++;
        	arr['R' - 'A']--;
        	arr['F' - 'A']--;
        	arr['O' - 'A']--;
        	arr['U' - 'A']--;
        	ctr+=4;
        }
        else if (arr['F' - 'A']) {
        	num[5]++;
        	arr['F' - 'A']--;
        	arr['I' - 'A']--;
        	arr['V' - 'A']--;
        	arr['E' - 'A']--;
        	ctr+=4;
        }
        else if (arr['V' - 'A']) {
        	num[7]++;
        	arr['V' - 'A']--;
        	arr['S' - 'A']--;
        	arr['E' - 'A']--;
        	arr['E' - 'A']--;
        	arr['N' - 'A']--;
        	ctr+=5;
        }
        else if (arr['I' - 'A']) {
        	num[9]++;
        	arr['I' - 'A']--;
        	arr['N' - 'A']--;
        	arr['N' - 'A']--;
        	arr['E' - 'A']--;
        	ctr+=4;
        }
        else if (arr['N' - 'A']) {
        	num[1]++;
        	arr['N' - 'A']--;
        	arr['O' - 'A']--;
        	arr['E' - 'A']--;
        	ctr+=3;
        }
        }
        /*for (int i = 0; i < 10; i++) {
            cout<<num[i]<<endl;
        }*/
        cout<<"Case #"<<tt-t<<": ";
        for (int i = 0; i < 10; i++) {
        	while (num[i] != 0) {
        		printf("%d", i);
        		num[i]--;
        	}
        }
        cout<<endl;
    }
    return 0;
}
