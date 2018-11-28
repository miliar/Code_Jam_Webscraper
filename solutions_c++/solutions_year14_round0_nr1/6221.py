#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<string>
#include<map>
#include<vector>
#include<stack>
#include<deque>
#include<list>
#include <algorithm>
#include<iostream>
#include<utility>

using namespace std;
typedef long long LL;




int main()
{

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int t,r;
    int s;
    int a1[10],a2[10];
    scanf("%d",&t);
    int T=1;
    while(T++<=t){
        scanf("%d",&r);
        for(int j=0;j<4;j++){
            if(j!=r-1)
             for(int i=0;i<4;i++)
                scanf("%d",&s);
            else
            for(int i=0;i<4;i++)
               scanf("%d",&a1[i]);
        }

        scanf("%d",&r);
        for(int j=0;j<4;j++){
            if(j!=r-1)
                for(int i=0;i<4;i++)
                    scanf("%d",&s);
            else
            for(int i=0;i<4;i++)
               scanf("%d",&a2[i]);
        }

        sort(a1,a1+4);
        sort(a2,a2+4);
        int i=0,j=0;
        int res=0;
        int va=-1;
        while(i<4&&j<4){
            if(a1[i]==a2[j]){
                va=a1[i];i++;j++;res++;
            }else if(a1[i]<a2[j])
                i++;
            else
                j++;
        }
        if(res==0)
            printf("Case #%d: Volunteer cheated!\n",T-1);
        else if(res>1)
            printf("Case #%d: Bad magician!\n",T-1);
        else
            printf("Case #%d: %d\n",T-1,va);

    }
    return 0;
}
