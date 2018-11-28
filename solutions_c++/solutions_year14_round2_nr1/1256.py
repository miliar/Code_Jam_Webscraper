#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector <string> v;
int ind[105];
int n;

int f (vector <int> r) {
    int ret = 0;
    int m = r.size() / 2;
    int num = r[m];
    for (int i=0; i<r.size(); i++) {
        int diff = abs(r[i] - num);
        ret += diff;
    }
    return ret;
}

int start () {
    int ret = 0;
    vector <int> num;
    while (ind[0] != v[0].size()) {
        num.clear();
        char ini = v[0][ind[0]];
        for (int i=0; i<n; i++) {
            if (ind[i] == v[i].size() || v[i][ind[i]] != ini) return -1;
            int cnt = 0;
            while (ind[i] < v[i].size() && v[i][ind[i]] == ini) {
                ind[i] ++;
                cnt ++;
            }
            num.push_back(cnt);
        }
        sort (num.begin() , num.end());
        ret += f (num);
    }
    for (int i=0; i<n; i++) {
        if (ind[i] != v[i].size()) {
            return -1;
        }
    }
    return ret;
}

int main () {
    FILE *in = fopen("A.in","r");
    FILE *out = fopen("A.out","w");
    int t,k = 1;
    fscanf (in,"%d",&t);
    while (t --) {
        v.clear();
        memset (ind,0,sizeof(ind));
        fprintf (out, "Case #%d: ",k++);
        fscanf (in,"%d",&n);
        for (int i=0; i<n; i++) {
            char c[105];
            fscanf (in,"%s",c);
            v.push_back(c);
        }
        int ret = start();
        if (ret == -1) fprintf (out,"Fegla Won\n");
        else fprintf (out,"%d\n",ret);
    }
}
