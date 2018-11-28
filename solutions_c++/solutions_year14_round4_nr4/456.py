#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <stack>

using namespace std;
int mas[1000];

void solve(int T) {
    int M,N;
    cin>>M>>N;
    vector<string> v(M);
    for (int i=0;i<M;i++)
        cin>>v[i];
    int total = pow(N+0.,M);
    int ways=0, maxi=-1;
    for (int i=0;i<total;i++) {
        vector<int> num(M);
        int k=i;
        for (int j=0;j<M;j++) {
            num[j]=k%N;
            k/=N;
        }
        vector<set<string> > vs(N);
        for (int j=0;j<M;j++) {
            int index=num[j];
            string cur="";
            vs[index].insert(cur);
            for (int tt=0;tt<v[j].size();tt++) {
                cur+=v[j][tt];
                vs[index].insert(cur);
            }
        }
        int curcol=0;
        for (int j=0;j<N;j++) {
            curcol += vs[j].size();
        }
        if (curcol>maxi) {
            maxi=curcol;
            ways=1;
        } else if (curcol==maxi)
            ways++;
    }
    printf("Case #%d: %d %d\n",T,maxi,ways);
}

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int T;
    cin>>T;
    for (int i=0;i<T;i++)
        solve(i+1);
    return 0;
}