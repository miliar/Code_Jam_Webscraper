#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("bin.txt","r",stdin);
    freopen("bout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d: " , test_case);
        string S;
        cin>>S;
        char first=S[0];
        int tot=1;
        char tmp=first;
        for(int i=1;i<S.length();i++)
        {
            if(S[i]!=tmp)
            {
                tot++;
                tmp=S[i];
            }
        }
        if(first=='+')
        {
            printf("%d\n" , tot-(tot&1));
        }
        else
        {
            printf("%d\n" , tot-1+(tot&1));
        }



    }

    return 0;
}
