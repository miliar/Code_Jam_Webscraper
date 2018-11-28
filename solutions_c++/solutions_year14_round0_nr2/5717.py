#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <string>
#include <cctype>
#include <map>
#include <iomanip>
                   
using namespace std;
                   
#define eps 1e-8
#define pi acos(-1.0)
#define inf 1<<30
#define linf 1LL<<60
#define pb push_back
#define lc(x) (x << 1)
#define rc(x) (x << 1 | 1)
#define lowbit(x) (x & (-x))
#define ll long long

struct Node {
    int x,y,ok;
}a[110],ans[110];
int maz[10][10];
int cnt[10];
int n,k;

void find(int fa) {
    for (int i=0; i<=6; i++) {
        if (maz[fa][i]>0) {
            maz[fa][i]--;
            maz[i][fa]--;
            find(i);            
            ans[k].x=fa;
            ans[k].y=i;
            k++;
        }
    }
    return ;
}

int main() {
    while (cin >> n) {
        int x,y;
        memset(maz,0,sizeof(maz));
        memset(cnt,0,sizeof(cnt));
        for (int i=0; i<n; i++) {
            cin >> x >> y;
            maz[x][y]++;
            maz[y][x]++;
            cnt[x]++;
            cnt[y]++;
            a[i].x=x;
            a[i].y=y;
            a[i].ok=0;
        }
        k=0;
        for (int i=0; i<=6; i++) {
            if (cnt[i]%2==1) k++;
        }
        if (k!=0 && k!=2) cout << "No solution" << endl;
        else {
            int st;
            if (k==0) {
                for (int i=0; i<=6; i++) {
                    if (cnt[i]>0) {st=i;break;} 
                }
            }
            if (k==2) {
                for (int i=0; i<=6; i++) {
                    if (cnt[i]%2==1) {st=i;break;}
                }
            }
            k=0;
            find(st);
            if (k<n) cout << "No solution" << endl;
            else {
                for (int i=n-1; i>=0; i--) {
                    for (int j=0; j<n; j++) {
                        if (a[j].ok==0 && a[j].x==ans[i].x && a[j].y==ans[i].y) {
                            cout << j+1 << " +" << endl;
                            a[j].ok=1;
                            break;
                        }
                        if (a[j].ok==0 && a[j].x==ans[i].y && a[j].y==ans[i].x) {
                            cout << j+1 << " -" << endl;
                            a[j].ok=1;
                            break;
                        }
                    }
                }
            }
        }
    }
    return 0;
}
