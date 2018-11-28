#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

bool visited[10];
int cnt;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("y.out","w",stdout);
    int t, ca= 0;
    cin>> t;
    while(t--)
    {
        cnt = 0;
        memset(visited,0,sizeof(visited));
        int n;
        scanf("%d",&n);
        printf("Case #%d: ",++ca);
        if(n == 0){
            printf("INSOMNIA\n");
            continue;
        }
        int r = 1,temp, res;
        for(int i = 1; r ; ++i)
        {
             temp = i*n;
             while(temp)
             {
                 int k = temp%10;
                 if(!visited[k]) { cnt++; visited[k] = 1; }
                 temp/=10;
             }
             if(cnt == 10) { r = 0; res = i*n; };
        }
        printf("%d\n",res);
    }
    return 0;
}
