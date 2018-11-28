#include <cstdio>
#include <algorithm>
#include <vector>
#define MAX 10000
inline int half(int n)
{
    return (int)(n/2.0+0.5);
}
int main()
{
    freopen("B-small-attempt8.in","r",stdin);
    freopen("B-small-attempt8.out","w",stdout);
    std::vector<int> v;
    int T,n,cnt,max,result,h,h_cnt,h_cnt2,temp,same,max2;

    scanf("%d",&T);
    for(int k=0;k<T;k++)
    {
        cnt=0;
        result=MAX;
        v.clear();
        scanf("%d",&n);
        for(int i=0;i<n;i++){scanf("%d",&temp);v.push_back(temp);}
        while(1){
            std::sort(v.begin(),v.end());
            max=v.back();
            max2=h=half(max);
            same=h_cnt=h_cnt2=0;
            if(cnt==0) result=max;
            if(max==9)
            {
                for(int i=0;i<v.size()-1;i++) if(v[i]>6) h_cnt++;
                if(h_cnt==0)
                {
                    v.pop_back();
                    v.push_back(3);
                    v.push_back(3);
                    v.push_back(3);
                    cnt+=2;
                }
            }
            h_cnt=0;
            for(int i=0;i<v.size();i++) {if(h<v[i]) h_cnt++; if(h+1<v[i]) h_cnt2++; if(max==v[i]) same++; if(max>v[i]&&max2<v[i]) max2=v[i];}
            //for(int i=0;i<v.size();i++) printf("%d ",v[i]);
            //printf("/%d\n",result);

            if( h > h_cnt ){
                for(int i=0;i<h_cnt2;i++)
                {
                    int b=v.back();
                    v.pop_back();
                    v.push_back(b/2);
                    v.push_back(half(b));
                    std::sort(v.begin(),v.end());
                    cnt++;
                }
                std::sort(v.begin(),v.end());
                result=cnt+v.back();
                if(max<h_cnt2+v.back()) printf("==========");
                //printf("[1] : result=%d\n",result);
            }
            else if(cnt+same+max2<result) {
                for(int i=0;i<same;i++)
                {
                    int b=v.back();
                    v.pop_back();
                    v.push_back(b/2);
                    v.push_back(half(b));
                    std::sort(v.begin(),v.end());
                    cnt++;
                }
                std::sort(v.begin(),v.end());
                result=cnt+v.back();
                //printf("[2] : result=%d\n",result);
            }
            else break;
            max=v.back();
            if(max<=3) break;

        }

        printf("Case #%d: %d\n",k+1,result);
    }
    return 0;
}
