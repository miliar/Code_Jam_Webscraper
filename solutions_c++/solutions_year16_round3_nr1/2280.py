#include <iostream>
#include<stdio.h>
#include<limits.h>
#include<algorithm>
#include<vector>
using namespace std;
vector<pair<int, int> > p;
int main()
{
    freopen("input3.in","r",stdin);
    freopen("output3.txt","w",stdout);
    int t,n,c=1,minn,x;
    scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",c);
        c++;
        scanf("%d",&n);
        minn=INT_MAX;
        for(int i=65; i<65+n; i++)
        {
            scanf("%d",&x);
            if(x<minn) minn=x;
            p.push_back(make_pair(x,i));
        }
        sort(p.begin(),p.end());
        int i,xx;
        for(i=p.size()-1; i>0; i--)
        {
            ab:
            xx=0;
            for(int j=i; j<p.size(); j++)
            {
                //while(p[j].first>p[i-1].first)
                //{
                    if(p[j].first>p[i-1].first)
                    {
                        printf("%c ",char(p[j].second));
                        p[j].first--;
                        xx=-1;
                    }
                //}
            }
            if(xx==-1) goto ab;
            /*while(p[i].first>p[i-1].first)
            {
                printf("%c ",char(p[i].second));
                p[i].first--;
            }*/
        }

        //for
        /*for(int i=65; i<65+n; i++)
        {
            while(p[i]>minn)
            {
                printf("%c ",char(i));
                p[i]--;
            }
        }*/
        for(int i=0; i<p.size()-2; i++)
        {
            while(p[i].first>0)
            {
                printf("%c ",char(p[i].second));
                p[i].first--;
            }
        }
/*        for(int i=65; i<65+n-2; i++)
        {
            while(p[i]>0)
            {
                printf("%c ",char(i));
                p[i]--;
            }
        }*/
        int a=p.size()-1, b=p.size()-2;
        for(int i=0; i<minn; i++)
        {
            printf("%c%c ",char(p[a].second),char(p[b].second));
        }
        printf("\n");
        p.clear();
        //for(int i=0; i<=26; i++) p[i]=0
    }
    return 0;
}
