#include <iostream>
#include <cstdio>
#include <climits>

using namespace std;

int T;
int n,a[1010];

bool verify(int plant,int cake) {
    int amount = 0;
    for(int i=0;i<n;++i)
        amount += (a[i]-1)/cake;
    return (amount+n)<=plant ;
}
int binary(int left,int plant,int right) {
    if(left == right) return left;
    int middle = (left+right)>>1;
    if(verify(plant,middle))
        return binary(left,plant,middle);
    else
        return binary(middle+1,plant,right);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin >> T;
    for(int i=0;i<T;++i) {
        cin >> n;
        int answer = INT_MAX;
        for(int j=0;j<n;++j)
            cin >> a[j];
        for(int j=n;j<=2000;++j)
            answer = min(answer,j-n+binary(1,j,1000));
        printf("Case #%d: %d\n",i+1,answer);
    }
    return 0;
}
