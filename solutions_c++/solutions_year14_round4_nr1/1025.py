#include <iostream>  
#include <cstdio>  
#include <fstream> 
#include <map> 
#include <cstring>
using namespace std;  


int main()  
{  
    //ifstream cin("D:\\A-large.in");  
    //freopen("D:\\A-large.out","w",stdout); 

    int k;  
    cin >> k;   
    for(int times = 1; times <= k; times++)  
    {  
        int n, x;
        int s[10005];
        printf("Case #%d: ", times);
        cin >> n >> x;
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }
        sort(s, s + n);
        bool used[10005];
        memset(used, false, sizeof(used));
        int ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (used[i] == false) {
                used[i] = true;
                ans++;
                for (int j = i - 1; j >= 0; j--) {
                    if (used[j] == false && s[j] <= x - s[i]) {
                        used[j] = true;
                        break;
                    }
                }
            }
        }
        printf("%d\n", ans);
    }  
}  
