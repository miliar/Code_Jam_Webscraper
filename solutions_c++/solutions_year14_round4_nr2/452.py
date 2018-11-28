#include <iostream>
#include<stdio.h>
#include<map>
#include<fstream>
using namespace std;
struct hh
{
    int ru;
    int chu;
    int s;
}qq[100003];
map<int,int>map_a;
int main()
{
    //freopen("in.txt","r",stdin);
    int from,to;
    int t=0;
    while(scanf("%d%d",&from,&to))
    {

        map_a.clear();
        t++;
        int i;
        if(from==-1&&to==-1)break;
        if(from==0&&to==0)
        {
           printf("Case %d is a tree.\n",t);
           continue;
        }
        int k=0;
        map_a[from]=k;
        qq[k].chu=1;
        qq[k].ru=0;
        k++;
         if(map_a.count(to))
            {
                qq[map_a[to]].ru++;
            }
            else
            {
                map_a[to]=k;
                qq[k].chu=0;
                qq[k].ru=1;
                qq[k].s=to;
                k++;
            }
        while(scanf("%d%d",&from,&to))
        {
            if(from==0&&to==0)
                break;
            if(map_a.count(from))
            {
                qq[map_a[from]].chu++;
            }
            else
            {
                map_a[from]=k;
                qq[k].chu=1;
                qq[k].ru=0;
                qq[k].s=from;
                k++;
            }
            if(map_a.count(to))
            {
                qq[map_a[to]].ru++;
            }
            else
            {
                map_a[to]=k;
                qq[k].chu=0;
                qq[k].ru=1;
                qq[k].s=to;
                k++;
            }
        }

        int flag=0;
        int wrong=0;
        int s=0;
        for(i=0;i<k;++i)
        {
            if(qq[i].ru==0)flag++;
            if(qq[i].ru>1)
            {
                wrong=1;
                break;
            }
            s+=qq[i].chu;
        }
        //cout<<flag<<' '<<wrong;
        if(wrong==1){printf("Case %d is not a tree.\n",t);continue;}
        if(flag!=1){printf("Case %d is not a tree.\n",t);continue;}
        if(s!=k-1){printf("Case %d is not a tree.\n",t);continue;}
        printf("Case %d is a tree.\n",t);
    }
    return 0;
}