#include <iostream>  
#include <cstdio>  
#include <fstream> 
#include <map> 
#include <cstring>
using namespace std;  


int a[1024];
int n;

int main()  
{  
    //ifstream cin("D:\\B-large.in");  
    //freopen("D:\\B-large.out","w",stdout); 

    int k;  
    cin >> k;   
    for(int times = 1; times <= k; times++)  
    {  
        int n, x;
        printf("Case #%d: ", times);
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        int ans = 0;
        bool used[1024];
        memset(used, false, sizeof(used));
        for (int i = 0; i < n; i++) {
            int minx = INT_MAX;
            int now;
            for (int j = 0; j < n; j++) {
                if (!used[j] && a[j] < minx) {
                    minx = a[j];
                    now = j;
                }
            }
            used[now] = true;
            int first = 0, second = 0;
            for (int j = 0; j < now; j++) {
                if (!used[j]) first++;
            }
            for (int j = now + 1; j < n; j++) {
                if (!used[j]) second++;
            }
            ans += min(first, second);
        }
        printf("%d\n", ans);
    }  
}  
