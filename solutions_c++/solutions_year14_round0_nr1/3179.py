#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int testCase = 0;
    int ans1 = 0;
    int ans2 = 0;
    int cardNo = 0;
    int magicAns = 0;
    int ansNo = 0;
/*
freopen("A.in","r",stdin);
freopen("A.out","w",stdout);
*/
    scanf("%d", &testCase);
    for(int T = 1; T <= testCase; T++)
    {
        scanf("%d", &ans1);
        vector<int> possibles;
        for(int I = 1; I <= 4; I++)
        {
            for(int J = 0; J < 4; J++)
            {
                scanf("%d", &cardNo);
                if(I == ans1)
                    possibles.push_back (cardNo);
            }
        }

        scanf("%d", &ans2);
        magicAns = 0;
        ansNo = 0;
        for(int I = 1; I <= 4; I++)
        {
            for(int J = 0; J < 4; J++)
            {
                scanf("%d", &cardNo);
                if(I == ans2)
                {
                    if(find(possibles.begin(), possibles.end(), cardNo) != possibles.end())
                    {
                        ansNo++;
                        magicAns = cardNo;
                    }
                }
            }
        }

        if(ansNo == 0)
            printf("Case #%d: Volunteer cheated!\n", T);
        else if(ansNo == 1)
            printf("Case #%d: %d\n", T, magicAns);
        else
            printf("Case #%d: Bad magician!\n", T);
    }
    return 0;
}
