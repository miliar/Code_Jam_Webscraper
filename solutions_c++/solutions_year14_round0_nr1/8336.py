#include <bits/stdc++.h>
using namespace std;


int main()
{
    int t,a,b;
    int arr[4][4];
    int i ,j,t1;
    scanf("%d",&t);
    t1=0;
    while(t--)
    {
        t1++;
        map <int,int> mymap;
        scanf("%d",&a);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&arr[i][j]);
                if(i==a-1)
                    mymap[arr[i][j]]++;
            }
        }

        scanf("%d",&b);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&arr[i][j]);
                if(i==b-1)
                    mymap[arr[i][j]]++;
            }
        }

        int sz = mymap.size();
        if(sz==7)
        {
            int ans;
            for (map<int,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
            {
                if(it->second==2)
                {
                    ans=(it->first);
                    break;
                }
            }


            printf("Case #%d: %d\n",t1,ans);

        }
        else if(sz==8)
        {
           printf("Case #%d: Volunteer cheated!\n",t1);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",t1);
        }

    }

    return 0;
}
