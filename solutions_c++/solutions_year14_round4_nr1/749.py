#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int files[10100];

int main()
{
    int kase,T;
    scanf("%d",&T);
    int N,X,i,cnt,begin,end;
    for(kase=1;kase<=T;kase++)
    {
        printf("Case #%d: ",kase);
        scanf("%d%d",&N,&X);
        for(i=0;i<N;i++)
            scanf("%d",&files[i]);
        sort(files,files+N);
        begin = 0;
        end = N-1;
        cnt = 0;
        for(i=N-1;i>=begin;i--)
        {
            if(i!=begin && files[i]+files[begin]<=X)
            {
                begin++;
            }
            cnt++;
        }
        printf("%d\n",cnt);
    }
    return 0;
}
