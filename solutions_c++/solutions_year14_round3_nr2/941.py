
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
using namespace std;
typedef long long ll;
const int maxn = 110;
const ll mod = 1000000007;
const int numlen = 27;
ll ans;
int mark[maxn];
int all[numlen];
int isl[numlen],isr[numlen];
int l[maxn],r[maxn];
int in[numlen];
int n;
ll dd[maxn];
int main(){
        int t,nc = 0,num;
        char str[maxn],str2[maxn];
        cin >> t;
        while(t--){
            ii = 1;
            printf("Case #%d: ",++nc);
            memset(mark,0,sizeof mark);
            memset(l,0,sizeof l);
            memset(r,0,sizeof r);
            memset(all,0,sizeof all);
            memset(in,0,sizeof in);
            scanf("%d",&n);
            num = 0;
            ok = 1;
            for(int i = 1; i <= n; i++){
                scanf("%s",str);
                int len = strlen(str);
                int c = 1;
                str2[0] = str[0];
                for(j = 1; j < len; j++){
                    if(str[j] != str[j-1]) str[c++] = str[j];
                }
                str2[c] = '\0';
                if(c == 1){
                    if(in[str[0] - 'a']) ok = 0;
                    all[str[0]-'a'] ++;
                }
                else{
                    int left = str[0] - 'a', right = str2[c-1] - 'a';
                    if(isl[left] || isr[right] || in[left] || in[right]) ok = 0;
                    isl[left] = ii; isr[right] = ii;
                    l[ii] = left; r[ii] = right;
                    ii++;
                    if(c != 2){
                        for(int j = 1; j < c-1 ; j++){
                            int now = str[j] - 'a';
                            if(in[now] || isl[now] || isr[now]) ok = 0;
                            in[now] ++;
                        }
                    }
                }
            }
            if(!ok) printf("0\n");
            else{
                for(int i = 0; i < ii ;i++){
                    dd[i] = 1;
                }
                for(int i = 0; i < 26; i ++){
                    if(is[i] && a)
                }
            }
        }
}
