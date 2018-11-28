#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <set>
#include <cstdio>
#include <cstring>
#include <climits>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define MAXN 1010

int v[MAXN];
int x[MAXN];
int aux[MAXN];

int count_inversion_merge(int first, int last)
{
    int mid = (first+last)/2;
    int ai = first;
    int bi = mid+1;
    int finali=0;
    int inversion = 0, i;

    while (ai <= mid && bi <= last) {
        if (x[ai] <= x[bi]) {
                aux[finali++] = x[ai++];
        } else {
                aux[finali++] = x[bi++];
                inversion += mid - ai + 1;
        }
    }

    while (ai <= mid)
        aux[finali++] = x[ai++];

    while (bi <= last)
        aux[finali++] = x[bi++];

    for (i=0 ; i<last-first+1 ; i++)
        x[i+first] = aux[i];

    return inversion;
}

int count_inversion2(int a, int b){
    int ans = 0;
    for(int i = a ; i <= b ; i++){
        for(int j = i + 1 ; j <= b ; j++)
            if(x[j] < x[i])
                ans++;
    }
    return ans;
}

int count_inversion(int a, int b){
    int x, y, z, mid;
    if (a >= b) return 0;

    mid = (a+b)/2;

    x = count_inversion(a, mid);
    y = count_inversion(mid+1, b);
    z = count_inversion_merge(a, b);

    return x+y+z;
}

int n;
int solve(int ind){
    int sz = 0;
    for(int i = 0 ; i < ind ; i++){
        x[sz++] = v[i];
    }
    int ans = 0;
    ans += count_inversion(0,sz-1);
    sz = 0;
    for(int i = ind ; i < n ; i++){
        x[sz++] = v[i];
    }
    ans += (sz*(sz - 1))/2;
    ans -= count_inversion(0,sz-1);
    return ans;
}

int solve2(int ind){
    int pos = 0;
    for(int i = 0 ; i < n ; i++){
        if(v[i] > v[pos])
            pos = i;
    }
    int ans = abs(pos-ind);
    for(int i = 0 ; i < n ; i++){
        aux[i] = v[i];
    }
    if(pos < ind){
        while(pos < ind){
            swap(aux[pos],aux[pos+1]);
            pos++;
        }
    }
    else if(pos > ind){
        while(pos > ind){
            swap(aux[pos],aux[pos-1]);
            pos--;
        }
    }

    int sz = 0;
    for(int i = 0 ; i < ind ; i++){
        x[sz++] = aux[i];
    }
    int ans1 = count_inversion(0,sz-1);
    sz = 0;
    for(int i = ind + 1 ; i < n ; i++){
        x[sz++] = aux[i];
    }
    int ans2 = ((sz*(sz - 1))/2) -  count_inversion(0,sz-1);
    ans += ans1 + ans2;
    return ans;

}

int main(){
    int nt;
    freopen ("B-small-attempt3.in","r",stdin);
    freopen ("Bac3.out","w",stdout);

    scanf(" %d",&nt);
    int t = 1;
    while(nt--){
        scanf(" %d",&n);
        for(int i = 0 ; i < n ; i++){
            scanf(" %d",&v[i]);
        }

        int ans = INT_MAX;
        for(int i = 0 ; i < n ; i++){
            ans = min(ans,solve2(i));
        }
        printf("Case #%d: %d\n",t++,ans);
    }
    return 0;
}
