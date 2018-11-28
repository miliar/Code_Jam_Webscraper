#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;

#define pii pair< int , int >
vector<int> v;
bool func(int special,int mid)
{
    //printf("sp and mid are %d %d\n",special,mid);
    vector<int> f;
    for(int i=0; i<v.size(); i++)
    {
        if(v[i]<=mid)
        {
            //ok...all pancakes can be finished within "mid" minutes
        }
        else if(v[i]>mid)
        {
            //To be transferred
            int diff=v[i]-mid;
            f.push_back(diff);
            //printf("pushing %d\n",diff);
        }
    }
    int idx=0;
    while( idx<f.size())
    {
        if(f[idx]>0 && special==0)
        {
            return false;
        }
        if(mid>=f[idx])
        {
            idx++;
            special--;
            //you have done this part
        }
        else
        {
            f[idx]-=mid;
            special--;
        }
    }
    return true;
}
int main()
{
    int t,D,P,c;
    scanf("%d",&t);
    c=0;
    while(t--)
    {
        c++;
        v.clear();
        scanf("%d",&D);
        for(int i=1; i<=D; i++)
        {
            scanf("%d",&P);
            v.push_back(P);
        }
        sort(v.rbegin(),v.rend());
        int ans=1000006;
        for(int special=0; special<=1000; special++)
        {
            int low,up,mid;
            low=1;
            up=1000;
            while(low<up)
            {
                mid=low+(up-low)/2;
                bool fnd;

                //Can mid be my answer ie can we have atmost "mid" non special minutes
                fnd=func(special,mid);
                //printf("special is %d mid is %d and fnd is %d\n",special,mid,fnd);
                if(fnd==false)
                {
                    low=mid+1;
                }
                else
                {
                    up=mid;
                }
            }//EndOfBinarySearch
            //printf("special %d low %d\n",special,low);
            if(special+low<ans)
            {
                ans=special+low;
            }
        }//EndOfSpecialLoop
        printf("Case #%d: %d\n",c,ans);
    }
    return 0;
}
