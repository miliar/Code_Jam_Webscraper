#include "cstdio"
#include "vector"
#include "algorithm"
#include "utility"

using namespace std;

int main(void)
{
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        vector<pair<int,int> > nums;
        
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            int buff;
            scanf("%d",&buff);
            nums.push_back(make_pair(buff,i));
        }
        
        int ans = -1;
        sort(nums.begin(), nums.end());
        
        do
        {
            int now = 1;
            for(;now<n;now++)
            {
                if(nums[now].first<nums[now-1].first)
                    break;
            }
            
            bool ok = true;
            for(;now<n;now++)
            {
                if(nums[now].first>nums[now-1].first)
                {
                    ok = false;
                    break;
                }
            }
            
            if(!ok)
                continue;
            
            int val = 0;
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<i;j++)
                    val += nums[i].second<nums[j].second;
            }
            
            if(ans==-1 || ans>val)
                ans = val;
        }
        while(next_permutation(nums.begin(), nums.end()));
            
        printf("Case #%d: %d\n",test,ans);
    }
    return 0;
}
