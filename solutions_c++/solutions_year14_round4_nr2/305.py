#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int a[100010];
int main()
{
    int ti;scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        int n;scanf("%d",&n);
        vector<pair<int,int> >lst;
        for(int i = 0; i <n;i ++)
        {
            int tmp;
            scanf("%d",&tmp);
            lst.push_back(make_pair(tmp,i));
        }
        sort(lst.begin(),lst.end());
        int ans = 0;
        for(int i = 0; i < n; i ++)
        {
            ans += min(lst[i].second, n-i-1-lst[i].second);
            for(int j=i+1; j < n; j ++)
            {
                if(lst[j].second > lst[i].second)
                    lst[j].second --;
            }
        }
        printf("Case #%d: %d\n",ca,ans);
    }
}
