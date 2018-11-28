#include<iostream>
#include<cstdio>
#include<bitset>

using namespace std;

int n;
long long num;
bitset<10>v;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        int temp;
        scanf("%d",&temp);
        num=(long long)temp;

        if(temp==0)
            printf("Case #%d: INSOMNIA\n",i);
        else
        {
            for(v.reset();v.count()!=10;num+=temp)
            {
                long long temp1=num;
                while(temp1)
                {
                    v.set(temp1%10);
                    temp1/=10;
                }
            }
            num-=temp;
            printf("Case #%d: ",i);
            cout<<num<<endl;
        }
    }
	return 0;
}
/*
5
0
1
2
11
1692
*/
