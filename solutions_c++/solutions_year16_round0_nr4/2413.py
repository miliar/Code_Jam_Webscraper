#include <bits/stdc++.h>
using namespace std;
void Solve(int TestCase)
{
    int k,c,s;
    scanf("%d %d %d",&k,&c,&s);
    printf("Case #%d:",TestCase);
    for(int i = 1 ; i<=k ; i++) printf(" %d",i);
    printf("\n");
}
int main()
{
    freopen("C:\\Users\\dell\\Downloads\\inputd.txt","r",stdin);
    freopen("C:\\Users\\dell\\Downloads\\outputd.txt","w",stdout);
    int tc,t;
    scanf("%d",&tc);
    for(t = 1 ; t<=tc ; t++) Solve(t);
    return 0;
}
