#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#define MID(x,y) ((x+y)>>1)
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

const int sup = 0x7fffffff;
const int inf = -0x7fffffff;

vector <long long> res;
bool palindromes(char *s){
    int l = strlen(s);
    for (int i = 0; i < l/2; i ++)
        if (s[i] != s[l-1-i]){
            return false;
        }
    return true;
}
void pretreat(long long n){
    for (long long i = 1; i * i <= n; i ++){
        long long num = i * i;
        char s2[30] = "";
        char s1[30] = "";
        itoa(i, s1, 10);
        itoa(num, s2, 10);
        if (palindromes(s1) && palindromes(s2)){
            res.push_back(num);
        }
    }
}

int main(){
    pretreat(100000000000000);
    FILE *fi = fopen("input.txt", "r+");
    FILE *fp = fopen("output.txt", "w+");
    int t;
    fscanf(fi, "%d", &t);
    for (int cases = 1; cases <= t; cases ++){
        long long low, high;
        fscanf(fi, "%I64d %I64d", &low, &high);
        vector <long long> ::iterator it = lower_bound(res.begin(), res.end(), low);
        long long ans = 0;
        for (; it != res.end(); it ++){
            //cout << *it << " ";
            if (*it > high)
                break;
            ans ++;
        }
        //cout << endl;
        fprintf(fp, "Case #%d: %I64d\n", cases, ans);
    }
	return 0;
}
