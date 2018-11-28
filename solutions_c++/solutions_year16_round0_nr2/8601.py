#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<numeric>
#include<fstream>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 long long
#define u64 unsigned i64

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.ans","w",stdout);
    int t, cs = 1;
    string s;
    cin>>t;
    while(t--){
        cin>>s;
        int n = s.length();
        int last = n - 1, cnt = 0, j;
        while(last>=0){
            while(last>=0 && s[last]=='+') last --;
            if(last<0) break;
            int i =0;
            while(i<=last && s[i]=='+'){
                s[i++]='-';
            }
            if(i) cnt++;
            for(i = 0, j = last;i<j;i++,j--){
                swap(s[i],s[j]);
            }
            for(i = 0;i<=last;i++){
                if(s[i]=='+') s[i] = '-';
                else s[i] = '+';
            }
            cnt++;
        }
        printf("Case #%d: %d\n",cs++,cnt);
    }
	return 0;
}
