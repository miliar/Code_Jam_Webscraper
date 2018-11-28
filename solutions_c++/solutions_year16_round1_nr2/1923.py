#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair <int,int> ii;
vector <int> vec[300];
void Solve(int);
int main()
{
    freopen("C:\\Users\\dell\\Downloads\\inputb.txt","r",stdin);
    freopen("C:\\Users\\dell\\Downloads\\outputb.txt","w",stdout);
    int tc,t;
    scanf("%d",&tc);
    for(t = 1 ; t<=tc ; t++) Solve(t);
    return 0;
}
void Solve(int TestCase)
{
    int n;
    scanf("%d",&n);
    for(int i = 1 ; i<=2*n-1 ; i++)
    {
        vec[i].clear();
        for(int j = 0 ; j<n ; j++)
        {
            int x;
            scanf("%d",&x);
            vec[i].push_back(x);

        }
    }
    sort(vec+1,vec+2*n);
    // if(TestCase == 27)
    // {
    //  printf("%d\n",n);
    // for(int i = 1 ; i<=2*n-1 ; i++)
    // {
    //     vec[i].clear();
    //     for(int j = 0 ; j<n ; j++)
    //     {
    //         int x;
    //         printf("%d ",vec[i][j]);
    //         //vec[i].push_back(x);

    //     }
    //     printf("\n");
    // }   
    // }

    vector <int> ans;
    int mark[300] = {0};
    int cnt = 0,a = 0,b = 0,i = 0;
    for(i = 0 ; i<=n-1 ; i++)
    {
        int mn = 25000;
        cnt = 0;
        a = 0;
        b = 0;
        for(int j = 1 ; j<=2*n-1 ; j++)
        {
            if(mark[j] == 1) continue;
            if(vec[j][i] < mn)
            {
                mn = vec[j][i];
                cnt = 1;
                a = j;
            }
            else
            {
                if(vec[j][i] == mn)
                {
                    cnt = 2;
                    b = j;
                }
            }
        }
        mark[a] = 1;
        mark[b] = 1;
        //printf("%d %d %d %d %d\n",i,mn,cnt,a,b);
        if(cnt == 1) break;
    }
    //printf("%d %d %d %d\n",i,cnt,a,b);
    vector <int> cand;
    cand.push_back(vec[a][i]);
    for(int j = 1 ; j<=2*n - 1 ; j++)
    {
        cand.push_back(vec[j][i]);
    }
    sort(cand.begin(),cand.end());
    int j = 0;
    for(int k = 0 ; k<2*n ; k++)
    {
        if(j < n && cand[k] == vec[a][j]) j++;
        else ans.push_back(cand[k]);
    }
    printf("Case #%d:",TestCase);
    for(int i = 0 ; i<n ; i++) printf(" %d", ans[i]);
    printf("\n");
}
/*
1
10
2 3 4 5 6 7 8 9 10 11
4 5 6 7 8 9 10 11 12 13
1 2 3 4 5 6 7 8 9 10
7 8 9 10 11 12 13 14 15 16
4 5 6 7 8 9 10 11 12 13
3 4 5 6 7 8 9 10 11 12
9 10 11 12 13 14 15 16 17 18
8 9 10 11 12 13 14 15 16 17
9 10 11 12 13 14 15 16 17 18
3 4 5 6 7 8 9 10 11 12
6 7 8 9 10 11 12 13 14 15
5 6 7 8 9 10 11 12 13 14
8 9 10 11 12 13 14 15 16 17
6 7 8 9 10 11 12 13 14 15
2 3 4 5 6 7 8 9 10 11
10 11 12 13 14 15 16 17 18 19
10 11 12 13 14 15 16 17 18 19
1 2 3 4 5 6 7 8 9 10
5 6 7 8 9 10 11 12 13 14


*/