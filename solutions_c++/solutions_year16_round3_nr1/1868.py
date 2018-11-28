#include<bits/stdc++.h>


using namespace std;

int main()
{
//    freopen("a.txt","r",stdin);
//    freopen("b.txt","w",stdout);
    int T,cased=0,n;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        int sum=0;

        pair<int,int> a[30];

        for(int i=0;i<n;i++)
        {
            int x;
            scanf("%d",&x);
            a[i].first=x;
            a[i].second=i;
            sum+=a[i].first;

        }
//         cout<<"OK"<<endl;
        printf("Case #%d: ",++cased);

        while(sum>0)
        {
            sort(a,a+n);
            if(a[n-1].first==a[n-2].first and sum!=3)
            {
                cout<<char('A'+a[n-1].second)<<char('A'+a[n-2].second)<<" ";
                a[n-1].first--;
                a[n-2].first--;
                sum-=2;
            }

            else
            {
                cout<<char('A'+a[n-1].second)<<" ";
                a[n-1].first--;
                sum--;
            }
        }
        printf("\n");

    }
    return 0;
}
