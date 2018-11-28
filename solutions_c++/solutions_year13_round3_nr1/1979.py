#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<cstring>
using namespace std;
int vow[256];
int main()
{
    vow['a'] = 1,vow['e'] = 1,vow['i'] = 1,vow['o'] = 1,vow['u'] = 1;
    int i,t,n,j,k;
    char str[101];
    scanf("%d",&t);
    for( i = 1; i <= t; i++)
    {
        printf("Case #%d: ",i);
        scanf("%s%d",str,&n);
        int ans = 0, l =strlen(str),c=0,last = -1;
        for( j = 0; str[j+n-1]; j++)
        {
            int flag = 0;
            for( k = j; k <= j+n-1; k++)
            {
                if( vow[str[k]])
                {
                    flag = 1;
                    break;
                }
            }
            if(flag == 0)
            {
                //printf("ans+= %d*%d\n",k+2,l-j);
                if(last!=-1)
                    ans += (j-last+1)*(l-(j+n-1));
                else
                    ans += l-(j+n-1);
                //printf("ans+= %d*%d\n",k+2,l-j);
                //cout<<"ans= "<<ans<<endl;
                last  = -1;
            }
            else
            if(last == -1)
            {
                last = j;
            }

        }
        printf("%d\n",ans);
    }
}
