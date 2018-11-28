#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin >> t;
    for(int q=1;q<=t;q++)
    {
        int r,x;
        int a[17];
        for(int i=1;i<=16;i++)  a[i]=0;

        cin >> r;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            cin >> x;
            if(i+1==r) a[x]++;
        }

        cin >> r;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            cin >> x;
            if(i+1==r) a[x]++;
        }

        printf("Case #%d: ",q);

        bool ok=true;
        int s=-1;
        for(int i=1;i<=16;i++)
        if(a[i]==2)
            {
                if(s==-1){s=i;} else {ok=false;}
            }
        if(s==-1){printf("Volunteer cheated!\n");} else
        if(!ok){printf("Bad magician!\n");} else
            printf("%d\n",s);
    }
    return 0;
}
