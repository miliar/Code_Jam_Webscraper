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
    int N;
    cin>>N;
    for (int i=0;i<N;i++)
        cin>>mas[i];
    int left=0, right=N-1;
    int swaps=0;
    while (left != right) {
        int mini=2E9, index=-1;
        for (int i=left;i<=right;i++) {
            if (mas[i]<mini) {
                mini=mas[i];
                index=i;
            }
        }
        int toleft=index-left, toright=right-index;
        if (toleft<toright) {
            for (int i=index-1;i>=0;i--)
                mas[i+1]=mas[i];
            swaps+=toleft;
            left++;
        } else {
            for (int i=index+1;i<=right;i++)
                mas[i-1]=mas[i];
            swaps+=toright;
            right--;
        }
    }
    printf("Case #%d: %d\n",T,swaps);
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