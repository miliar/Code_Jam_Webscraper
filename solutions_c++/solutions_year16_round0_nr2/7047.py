#include <bits/stdc++.h>
#define ll long long int
#define pii pair <int,int>
#define f first
#define s second
#define pi acos(-1.0)
#define pb push_back
using namespace std;

template < class T > inline T gcd(T a, T b) {while(b) {a %= b; swap(a, b);} return a;}
inline int nxt() {int wow; scanf("%d", &wow); return wow;}
inline ll lxt() {ll wow; scanf("%lld", &wow); return wow;}

int main()
{
  //  freopen("LARGEoutB.txt","w",stdout);
    int t, cse = 0, i, j;
    cin >> t;
    string s;
    while (t--){
        cin >> s;
        string temp = s, temp2;
        int p = 0, k = 0, ans = 0;
        while(1){
            int cnt = 0;
            for(i=0; i < s.length(); i++){
                if (temp[i] == '+') cnt++;
            }
            if (cnt == s.length()) goto mara;
            string notun;
            if (temp[0] == '-'){
                for(i=0; i < temp.length() && temp[i]=='-'; i++){
                    temp2.pb('+');
                }
                for(; i < temp.length(); i++){
                    notun.pb(temp[i]);
                }
                notun += temp2;
          //      cout << notun << endl;
                temp = notun;
                notun.clear();
                temp2.clear();
                ans++;
            }
            else{
                int seg = 0, maxi = -1, left = 0, right = 0, p = 0;
                for(i=0; i < temp.length() && temp[i]=='+'; i++){
                    temp2.pb('-');
                }
                k = i;
                for(; i < temp.length(); i++){
                    if(temp[i] == '-'){
                        seg = 0;
                        for(j=i; j < temp.length(); j++){
                            if (temp[j] == '+'){
                                i = j;
                                break;
                            }
                            else{
                                seg++;
                                if(seg > maxi){
                                    maxi = seg;
                                    p = j;
                                }
                            }
                        }
                    }
                }
            ///    cout << p << endl;
                for(i=k; i<p; i++){
                    notun.pb(temp[i]);
                }
                notun += temp2;
                for(i=p; i<temp.length(); i++){
                    notun.pb(temp[i]);
                }
            //    cout << notun << endl;
                temp = notun;
                notun.clear();
                temp2.clear();
                ans++;
            }
        }
        mara:
            printf("Case #%d: %d\n", ++cse, ans);
    }
	return 0;
}
