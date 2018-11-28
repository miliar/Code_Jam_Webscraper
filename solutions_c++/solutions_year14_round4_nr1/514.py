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
int mas[10000];

void solve(int T) {
    int N,X;
    cin>>N>>X;
    for (int i=0;i<N;i++)
        cin>>mas[i];
    sort(mas,mas+N);
    int cur=0;
    int left=0;
    for (int right=N-1;;right--) {
        if (left > right)
            break;
        if (left == right) {
            cur++;
            break;
        }
        int rcap=mas[right];
        int lcap=mas[left];
        if (rcap+lcap<=X)
            left++;
        cur++;
    }
    printf("Case #%d: %d\n",T,cur);
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