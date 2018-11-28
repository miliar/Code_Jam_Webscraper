#include<iostream>
#include<map>
#include<utility>
#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include <stdio.h>
#include<vector>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output1-large.out", "w", stdout);
    int t, DP[26];
    cin >> t;
    string s;
    for (int ij = 1;ij<=t;ij++) {
        cout << "Case #" << ij << ": ";
        cin >> s;
        int i, len=s.length(), ans[10], val;
        for (i=0;i<26;i++) {
            DP[i]=0;
        }
        for (i=0;i<10;i++) ans[i]=0;
        for (i=0;i<len;i++) {
            DP[s[i]-'A']++;
        }
        if (DP[25]>0) {
            val = DP[25];
            ans[0]+=val;
            DP[25] = DP[25]-val;
            DP[4] = DP[4]-val;
            DP[17] -= val;
            DP[14] -= val;
        }
        if (DP[22]>0) {
            val = DP[22];
            ans[2]+=val;
            DP[22]-=val;
            DP[19]-=val;
            DP[14]-=val;
        }
        if (DP[20]>0) {
            val = DP[20];
            ans[4]+=val;
            DP[5]-=val;
            DP[14]-=val;
            DP[20]-=val;
            DP[17]-=val;
        }
        if(DP[23]>0) {
            val = DP[23];
            ans[6]+=val;
            DP[18]-=val;
            DP[8]-=val;
            DP[23]-=val;
        }
        if(DP[6]>0) {
            val = DP[6];
            ans[8]+=val;
            DP[4]-=val;
            DP[8]-=val;
            DP[6]-=val;
            DP[7]-=val;
            DP[19]-=val;
        }
        if (DP[14]>0) {
            val = DP[14];
            ans[1]+=val;
            DP[14]-=val;
            DP[13]-=val;
            DP[4]-=val;
        }
        if (DP[17]>0) {
            val = DP[17];
            ans[3]+=val;
            DP[19]-=val;
            DP[7]-=val;
            DP[17]-=val;
            DP[4]-=val;
            DP[4]-=val;
        }
        if (DP[5]>0) {
            val = DP[5];
            ans[5]+=val;
            DP[5]-=val;
            DP[8]-=val;
            DP[21]-=val;
            DP[4]-=val;
        }
        if (DP[18]>0) {
            val = DP[18];
            ans[7]+=val;
            DP[18]-=val;
            DP[4]-=val;
            DP[21]-=val;
            DP[4]-=val;
            DP[13]-=val;
        }
        if (DP[8]>0) {
            val = DP[8];
            ans[9]+=val;
        }
        for (i=0;i<10;i++) {
            while (ans[i]-->0) cout<<i;
        }
        cout << endl;
    }
}
