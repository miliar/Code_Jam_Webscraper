#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Pancakelarge.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int I = 1 ; I <= t ; I++){
        string s;
        int k;
        cin >> s;
        scanf("%d",&k);
        int ans = 0;
        int n = s.size();
        for(int i = 0 ; i < n-k+1 ; i++){
            if(s[i] == '-'){
                ans ++;
                for(int j = i , l = 0 ;l < k ; l++ , j++){
                    if(s[j] == '-')
                        s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        bool isPoss = true;
        for(int i = 0 ; i < n ; i ++){
            if(s[i] == '-'){
                isPoss = false;
            }
        }
        if(isPoss){
            printf("Case #%d: %d\n",I,ans);
        }else printf("Case #%d: IMPOSSIBLE\n",I);
    }
    return 0;
}
