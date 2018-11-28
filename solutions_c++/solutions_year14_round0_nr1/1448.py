#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int N,i,j,T,a,b;
pair<int,int> pos[17];

int main()
{
    scanf("%d",&T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d",&a);
        for(i = 0; i < 4; i++)
        for(j = 0; j < 4; j++)
        {
            scanf("%d",&N);
            pos[N].first = i+1;
        }
        scanf("%d",&b);
        for(i = 0; i < 4; i++)
        for(j = 0; j < 4; j++)
        {
            scanf("%d",&N);
            pos[N].second = i+1;
        }
        int num = 0, numv = 0;
        for(i = 1; i <= 16; i++)
        if(pos[i] == mp(a,b))
        {
            num++;
            numv = i;
        }
        if(num == 1)
            printf("Case #%d: %d\n",t,numv);
        else if(num == 0)
            printf("Case #%d: Volunteer cheated!\n",t);
        else
            printf("Case #%d: Bad magician!\n",t);    
    }
    
    return 0;
}

