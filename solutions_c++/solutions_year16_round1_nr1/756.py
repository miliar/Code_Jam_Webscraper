#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

int main()
{
    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d: " , test_case);
        int i, j;
        string S;
        cin>>S;
        int N=S.length();
        deque<char> P;
        P.push_back(S[0]);
        for(i=1;i<N;i++)
        {
            if(P.front()> S[i])
            {
                P.push_back(S[i]);
            }
            else
            {
                P.push_front(S[i]);
            }
        }
        for(i=0;i<N;i++)
        {
            char tmp=P.front();
            P.pop_front();
            printf("%c" , tmp);
        }
        printf("\n");



    }

    return 0;
}
