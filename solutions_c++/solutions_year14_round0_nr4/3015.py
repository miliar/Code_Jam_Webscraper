#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int testCase = 0;
    int N = 0;
    double W;
    vector<double>::iterator itUp;

/*
freopen("D.in","r",stdin);
freopen("D.out","w",stdout);
*/
    scanf("%d", &testCase);
    for(int T = 1; T <= testCase; T++)
    {
        scanf("%d", &N);

        vector<double> naomi;
        vector<double> ken;
        for(int I = 0; I < N; I++)
        {
            scanf("%lf", &W);
            naomi.push_back(W);
        }
        for(int I = 0; I < N; I++)
        {
            scanf("%lf", &W);
            ken.push_back(W);
        }

        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        /*
        for(int I = 0; I < naomi.size(); I++)
            printf(" %.3lf", naomi[I]);
        printf("\n");
        for(int I = 0; I < ken.size(); I++)
            printf(" %.3lf", ken[I]);
        printf("\n");
        */
        int J = 0;
        for(int I = 0; I < N; I++)
            if(ken[I] > naomi[J])
                J++;
        int warResult = N - J;

        int deceitedResult = 0;
        for(int I = ken.size() - 1; I >= 0; I--)
        {
            itUp = upper_bound (naomi.begin(), naomi.end(), ken[I]);
            if(itUp != naomi.end())
            {
                deceitedResult++;
                naomi.erase(itUp);
            }
            else
            {
                naomi.erase(naomi.begin());
            }
        }

        printf("Case #%d: %d %d\n", T, deceitedResult, warResult);
    }
    return 0;
}
