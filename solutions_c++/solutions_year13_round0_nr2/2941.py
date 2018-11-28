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

typedef long long LL;
const int sup = 0x7fffffff;
const int inf = -0x7fffffff;
int ch[103][103];
int n, m;

bool judge(int x, int y){
    bool res = true;
    for (int j = 0; j < m; j ++)
        if (ch[x][j] > ch[x][y]){
            res = false;
            break;
        }
    if (res)
        return true;
    res = true;
    for (int i = 0; i < n; i ++)
        if (ch[i][y] > ch[x][y]){
            res = false;
            break;
        }
    if (res)
        return true;
    return false;
}
int main(){
    FILE *fi = fopen("input.txt", "r+");
    FILE *fp = fopen("output.txt", "w+");
    int t;
    fscanf(fi, "%d", &t);
    for (int cases = 1; cases <= t; cases ++){
        fscanf(fi, "%d %d", &n, &m);
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                fscanf(fi, "%d", &ch[i][j]);
        bool res = true;
        for (int i = 0; i < n; i ++){
            if (!res)   break;
            for (int j = 0; j < m; j ++){
                if (!judge(i, j)){
                    res = false;
                    break;
                }
            }
        }
        if (res){
            fprintf(fp, "Case #%d: YES\n",cases);
        }
        else{
            fprintf(fp, "Case #%d: NO\n",cases);
        }
    }
	return 0;
}
