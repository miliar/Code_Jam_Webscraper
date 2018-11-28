#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

char s[20000];
int a[200];
vector <string> v[20];

void clear(void)
{
    int i;
    
    for (i = 0; i < 200; i++) a[i] = 0;
    for (i = 0; i < 20; i++) v[i].clear();
}

void add(int x)
{
    int n = strlen(s) - 1, i, j;
    
    for (i = 0; i < n; i++) {
        string t = "";
        
        if (s[i] == ' ') continue;
        
        for (j = i; j < n; j++) {
            if (s[j] == ' ') break;
            
            t += s[j];
        }
        
        v[x].push_back(t);
        i = j;
    }
    
    sort(v[x].begin(), v[x].end());
    v[x].erase(unique(v[x].begin(), v[x].end()), v[x].end());
}

int main()
{
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, c = 0, sum = 0, ans = 1e9, j, k;
        map <string, int> mp;
        map <string, int> mp2;
        map <string, int>::iterator it;
        
        clear();
        
        scanf("%d%*c", &n);
        
        for (j = 0; j < n; j++) {
            fgets(s, 20000, stdin);
            
            add(j);
            
            for (k = 0; k < v[j].size(); k++) mp[v[j][k]]++;
        }
        
        for (j = 0; j < v[0].size(); j++) {
            for (k = 0; k < v[1].size(); k++) {
                if (v[0][j] == v[1][k]) {
                    sum++;
                    mp[v[0][j]] = 0;
                    
                    break;
                }
            }
        }
        
        for (it = mp.begin(); it != mp.end(); it++) {
            if (it->second >= 2) mp2[it->first] = c++;
        }
        
        for (j = 0; j < n; j++) {
            for (k = 0; k < v[j].size(); k++) {
                if (mp2.count(v[j][k])) a[mp2[v[j][k]]] |= (1 << j);
            }
        }
        
        for (j = 0; j < (1 << (n - 2)); j++) {
            int x = (j << 2) | 1, y = ((1 << n) - 1) ^ x, p = 0;
            
            for (k = 0; k < c; k++) {
                if ((a[k] & x) && (a[k] & y)) p++;
            }
            
            ans = min(ans, p);
        }
        
        printf("Case #%d: %d\n", i + 1, ans + sum);
    }
    
    return 0;
}
