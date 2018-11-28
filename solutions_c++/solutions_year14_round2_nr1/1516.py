#include<algorithm>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
#include<sstream>
#include<stdio.h>
#include<ctype.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<map>
#include<set>

using namespace std;

int n1,n2,fegla;
pair<int,int> last[105];
char arr[105][105];

int get_last(int row,char now,int i)
{
    int len=strlen(arr[row]);
    for(int c=i;c<len;c++)
    {
        if(arr[row][c]!=now)
            return c-1;
    }
    return len-1;
}

void clear(int n)
{
    for(int i=0;i<n;i++)
    {
        last[i].first=-1;
        last[i].second=-1;
    }

}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tt,n,result_out,result_in,batee5a,k,i,j,len_el_kebeer,len1,flag,z,l;
    char now;
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++)
    {
        scanf("%d",&n);
        clear(n);
        for(i=0;i<n;i++)
        {
            scanf("%s",arr[i]);
        }
        now = arr[0][0];
        result_out=0;
        flag=0;
        z=1;
        while(z)
        {
            z=0;
            now=arr[0][last[0].second+1];
            for(l=0;l<n;l++)
            {
                if(arr[l][last[l].second+1]!=now)
                {
                    flag=1;
                    break;
                }
                last[l].first=last[l].second;
                last[l].second=get_last(l,now,last[l].first+1);
            }
            if(flag)break;
            result_in=10000000;
            for(j=0;j<n;j++)
            {
                batee5a=0;
                len_el_kebeer=last[j].second-last[j].first;
                for(k=0;k<n;k++)
                {
                    if(k==j)continue;
                    len1=last[k].second-last[k].first;
                    batee5a+=abs(len_el_kebeer-len1);
                }
                result_in=min(result_in,batee5a);
            }
            result_out+=result_in;
            for(i=0;i<n;i++)
            {
                if(last[i].second!=strlen(arr[i])-1)
                    z=1;
            }
        }
        printf("Case #%d: ",tt);
        if(!flag)
            printf("%d\n",result_out);
        else
            fegla:printf("Fegla Won\n");
    }
	return 0;
}
