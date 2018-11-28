#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <iomanip>
using namespace std;

typedef long long LL;

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

string n;
set<string>pos;
vector<string>num;

string square(string a) {
    char retV[999] = {0}, s[999] = {0};
    int n = a.size(), ri = 0, rn = 0;
    for (int i = 0; i < n; i++) s[i] = a[i] - '0';
    for (int i = n - 1; i >= 0; i--) {
        int cur = s[i], x = 0;
        char temp[999] = {0};
        int it = 0;
        for (int j = n - 1; j >= 0; j--) {
            x += cur * s[j];
            temp[it++] = x % 10;
            x /= 10;
        }
        while (x > 0) { temp[it++] = x % 10; x/= 10; }
        for (int j = 0; j < it; j++) {
            x += retV[ri + j] + temp[j];
            retV[ri + j] = x % 10;
            x /= 10;
        }
        while (x > 0) { x = retV[ri + it] + x; retV[ri + it] = x %10; x/=10; it++; }
        rn = ri + it;
        ri++;
    }
    string r;
    for (int i = rn - 1; i >= 0; i--) r += retV[i] + '0';
    return r;
}


bool ispal(string a) {
    string b = a;
    reverse(b.begin(), b.end());
    if (a == b) return true;
    return false;
}

void addPos(string a, int s=0, int c1=0) {
    if (!ispal(square(a))) return;
    if (a.size() % 2 == 0) {
        if (s > a.size()/2) {
            pos.insert(a);
            return;
        }
        addPos(a, s+1);
        a[s + 1] = '1';
        a[a.size() - 1 - s - 1] = '1';
        addPos(a, s+1);
    } else {
        if (s > a.size()/2) {
            pos.insert(a);
            if (c1 <= 1) {
                int m = a.size()/2;
                a[m] = '1';
                pos.insert(a);
                a[m] = '2';
                pos.insert(a);
            }
            return;
        }
        addPos(a, s+1, c1);
        a[s + 1] = '1';
        a[a.size() - 1 - s - 1] = '1';
        addPos(a, s+1, c1+1);
    }
}

#define D 55

void gen() {
    pos.insert("1");
    pos.insert("2");
    pos.insert("3");
    for (int i = 2; i <= D; i++) {
        string a = "";
        a += '1';
        for (int j = 1; j < i-1; j++) a += '0';
        a += '1';
        addPos(a);
    }
    for (int i = 2; i <= D; i++) {
        if (i % 2 == 0) {
            string a = "";
            a += '2';
            for (int j = 1; j < i-1; j++) a += '0';
            a += '2';
            pos.insert(a);
        } else {
            string a = "";
            a += '2';
            for (int j = 1; j < i-1; j++) a += '0';
            a += '2';
            pos.insert(a);
            int m = a.size()/2;
            a[m] = '1';
            pos.insert(a);
        }
    }
}

bool cmp(string a, string b) {
    if (a.size() < b.size()) {
        return true;
    }
    else if (a.size() > b.size()) {
        return false;
    }
    else {
        for (int i = 0; i < a.size(); i++)
            if (a[i] < b[i]) return true;
            else if (a[i] > b[i]) return false;
    }
    return false;
}

void store() {
    for (set<string>::iterator it = pos.begin(); it != pos.end(); it++) {
        string a = *it;
        string b = square(a);
        if (ispal(b)) {
            num.push_back(b);
        }
    }
    sort(num.begin(), num.end(), cmp);
    //for (int i = 0; i < num.size(); i++) cout<<num[i]<<"\n";
    //cout<<num.size()<<"\n";
}

int count(string a) {
    int cnt = lower_bound(num.begin(), num.end(), a, cmp) - num.begin();
    //cout<<cnt<<" "<< num[cnt]<<"\n";
    return cnt;
}

int main() {
    int t;
    scanf("%d", &t);
    gen();
    store();
    for(int tt = 1; tt <= t; tt++) {
        string a, b;
        cin>>a>>b;
        int i = count(b);
        int j = count(a);
        if (num[i] == b) i++;
        printf("Case #%d: %d\n",tt, i - j);
    }
	return 0;
}
