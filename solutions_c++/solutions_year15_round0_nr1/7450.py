#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main()
{
    int tc,n,c=1;
    scanf("%d",&tc);
    while(tc--)
    {
        string A;
        scanf("%d",&n);
        cin>>A;
        int cur_stand=0,count=0,i,pos;
        for(i=0;i<=n;i++)
        {
            if(cur_stand<i)
            {
                if(A[i]=='0')
                {
                    continue;
                }
                //cout<<i<<"\t"<<count<<endl;
                count=count+(i-cur_stand);
                cur_stand=cur_stand+(i-cur_stand);
            }
            pos=A[i]-'0';
            cur_stand=cur_stand+pos;
        }
        printf("Case #%d: %d\n",c,count);
        c++;
    }
    return 0;
}
