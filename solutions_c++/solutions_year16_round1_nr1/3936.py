#include<stdio.h>
#include<string.h>
#include<deque>
using namespace std;
char A[1005];
deque <char> B;
main()
{
    freopen("A-large.in","a+",stdin);
    freopen("output.txt","w+",stdout);
    int t;
    scanf("%d",&t);
    for(int l=1;l<=t;l++)
    {
        scanf("%s",A);
        int Alen = strlen(A);
        for(int i=0;i<Alen;i++)
        {
            if(A[i]<B.front())
                B.push_back(A[i]);
            else
                B.push_front(A[i]);
        }
        printf("Case #%d: ",l);
        while(!B.empty())
        {
            printf("%c",B.front());
            B.pop_front();
        }
        printf("\n");
    }
}
