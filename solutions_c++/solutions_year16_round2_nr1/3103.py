#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <unordered_map>

#define INF 1000000000;
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
#define EPS                         1e-9
#define all(a)                      a.begin(), a.end()

using namespace std;
typedef long long LL;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

int alphabets[27];
vector<int> ans;

int main(){
    // freopen("A-large.in","r",stdin);
    int tc,tcount=1;
    scanf("%d\n",&tc);
    string cur;
    for(;tcount<=tc;tcount++){
        getline(cin,cur);
        ans.clear();
        memset(alphabets,0,sizeof alphabets);
        for(int i=0;i<cur.length();i++){
            alphabets[cur[i]-'A']++;
        }
        while(alphabets[25]>0){
            ans.push_back(0);
            alphabets[25]--;
            alphabets[4]--;
            alphabets[17]--;
            alphabets[14]--;
        }
        while(alphabets[6]>0){
            ans.push_back(8);
            alphabets[4]--;
            alphabets[8]--;
            alphabets[6]--;
            alphabets[7]--;
            alphabets[19]--;
        }
        while(alphabets[18]>0 && alphabets[8]>0 && alphabets[23]>0){
            ans.push_back(6);
            alphabets[8]--;
            alphabets[18]--;
            alphabets[23]--;
        }
        while(alphabets[18]>0 && alphabets[4]>1 && alphabets[21]>0 && alphabets[13]>0){
            ans.push_back(7);
            alphabets[4]-=2;
            alphabets[18]--;
            alphabets[21]--;
            alphabets[13]--;
        }
        while(alphabets[19]>0 && alphabets[22]>0 && alphabets[14]>0){
            ans.push_back(2);
            alphabets[19]--;
            alphabets[22]--;
            alphabets[14]--;
        }
        while(alphabets[19]>0 && alphabets[7]>0 && alphabets[17]>0 && alphabets[4]>1){
            ans.push_back(3);
            alphabets[4]-=2;
            alphabets[19]--;
            alphabets[7]--;
            alphabets[17]--;
        }
        while(alphabets[5]>0 && alphabets[14]>0 && alphabets[20]>0 && alphabets[17]>0){
            ans.push_back(4);
            alphabets[5]--;
            alphabets[14]--;
            alphabets[20]--;
            alphabets[17]--;
        }
        while(alphabets[5]>0 && alphabets[8]>0 && alphabets[21]>0 && alphabets[4]>0){
            ans.push_back(5);
            alphabets[5]--;
            alphabets[8]--;
            alphabets[21]--;
            alphabets[4]--;
        }
        while(alphabets[13]>1 && alphabets[8]>0 && alphabets[4]>0){
            ans.push_back(9);
            alphabets[13]-=2;
            alphabets[8]--;
            alphabets[4]--;
        }
        while(alphabets[14]>0 && alphabets[13]>0 && alphabets[4]>0){
            ans.push_back(1);
            alphabets[14]--;
            alphabets[13]--;
            alphabets[4]--;
        }
        sort(all(ans));
        printf("Case #%d: ",tcount);
        for(int i=0;i<ans.size();i++){
            printf("%d",ans[i]);
        }
        printf("\n");
    }
}