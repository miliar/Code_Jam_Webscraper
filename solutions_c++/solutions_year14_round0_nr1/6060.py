#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int main()
{
    freopen("A-small-attempt1 (1).in", "r", stdin);
    freopen("out1.out", "w", stdout);
    int i, j, n, t, cas = 1, r1, r2, val, count;
    int a[20];
    int b[5][5], c[5][5];
    cin>>t;
    while(t--)
    {
        cin>>r1;
        memset(a, 0, sizeof(a));
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++){
                cin>>b[i][j];
                if(i == r1)a[ b[i][j] ] = 1;
            }
        cin>>r2;
        count = 0;
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++){
                cin>>c[i][j];
                if(i == r2 && a[ c[i][j] ]){
                    val = c[i][j];
                    //printf("val = %d\n", val);
                    count++;
                }
            }
        printf("Case #%d: ", cas++);
        if(count == 1)printf("%d\n", val);
        else if(count > 1)printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
    return 0;
}
