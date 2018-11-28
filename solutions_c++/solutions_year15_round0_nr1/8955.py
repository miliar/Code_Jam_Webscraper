#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("A-large.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1; i <= t; i++) {
        int n, count = 0, standing;
        scanf("%d",&n);
        char shyness[n+1];
        scanf("%s",&shyness);

        standing = shyness[0] - '0';
        for(int j = 1; j <= n; j++) {
            if(j > standing) {
                count += (j - standing);
                standing += (j - standing);
            }
            standing += shyness[j] - '0';
        }

        printf("Case #%d: %d\n",i,count);
    }
}
