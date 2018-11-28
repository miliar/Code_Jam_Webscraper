#include<stdio.h>
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

string num[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int cnt[200];
vector<int> v;

void del(int n){
    int len = num[n].length();
    
    for(int i = 0; i < len; i++)
        cnt[num[n][i]]--;
    
    v.push_back(n);
}

int main(){
    freopen("/Users/WarYi/Desktop/a.in", "r", stdin);
    freopen("/Users/WarYi/Desktop/a.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    getchar();
    for(int t = 1; t <= T; t++){
        for(int i = 0; i < 200; i++)
            cnt[i] = 0;
        
        while(1){
            char in;
            scanf("%c", &in);
            if(in == '\n') break;
            cnt[in]++;
        }
        
        while(cnt['Z']) del(0);
        while(cnt['X']) del(6);
        while(cnt['W']) del(2);
        while(cnt['U']) del(4);
        while(cnt['G']) del(8);
        while(cnt['S']) del(7);
        while(cnt['H']) del(3);
        while(cnt['F']) del(5);
        while(cnt['O']) del(1);
        while(cnt['N']) del(9);
        
        sort(v.begin(), v.end());
        
        int size = v.size();
        printf("Case #%d: ", t);
        for(int i = 0; i < size; i++)
            printf("%d", v[i]);
        printf("\n");
        
        v.clear();
    }
}