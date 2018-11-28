#include <bits/stdc++.h>

using namespace std;

#define mem0(arr) memset(arr , 0 , sizeof arr)
#define memf(arr) memset(arr , false , sizeof arr)
#define memdp(arr) memset(arr , -1 , sizeof arr)
#define rep(i , n) for(int i = 1; i <= n; i++)
#define loop(i , n) for(int i = 0; i < n; i++)
#define pb push_back
#define fi first
#define se second
#define cs(y) cout << "Case " << y << ": "
#define cs2(y) cout << "Case " << y << ":" << "\n"

typedef long long ll;

int main()
{
    //ios::sync_with_stdio(false);cin.tie(0);

    freopen ("B-large.in", "r", stdin);
    freopen ("submit.txt","w",stdout);

    int n , m  , k , d , t , tem1 , tem2 , tem3 , tem4 , y = 1, sum = 0 , ans = 0;
    string s , c;


    scanf("%d", &t);

    while(t--){

        cin >> s;
        int n = s.size();
        printf("Case #%d: ", y++);
        ans = 0;

        for(int i = n - 1; i >= 1; i--){

            if(s[i] == '-'){

                ans++;
                int j;

                if(s[0] == '+'){

                    ans++;
                    j = 0;
                    while(s[j] == '+') s[j++] = '-';
                }

                j = 0;
                int k = i;

                while(j < k){

                    char temp;

                    if(s[k] == '+'){

                        temp = s[j];
                        s[j] = '-';

                        if(temp == '+') s[k] = '-';
                        else            s[k] = '+';

                    } else {

                        temp = s[j];
                        s[j] = '+';

                        if(temp == '+') s[k] = '-';
                        else            s[k] = '+';
                    }

                    k--;
                    j++;
                }

                if(j == k){

                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }

        if(s[0] == '-') ans++;
        printf("%d\n", ans);
    }

    return 0;
}
