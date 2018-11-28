#include <iostream>
#include <stdio.h>

using namespace std;

int T;

int n;

int data[1001];

int result1,result2;
int temp_rate;
int temp;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);getchar();
    for(int k=1;k<=T;++k)
    {
        scanf("%d",&n);getchar();
        for(int i=1;i<=n;++i) {scanf("%d",&data[i]);}
        getchar();
        result1=0;result2=0;
        temp_rate=0;
        for(int i=2;i<=n;++i)
        {
            if(data[i]<data[i-1])
            {
                result1+=data[i-1]-data[i];
                if(temp_rate<data[i-1]-data[i])
                {
                    temp_rate=data[i-1]-data[i];
                }
            }
        }
        for(int i=2;i<=n;++i)
        {
            if(data[i-1]>=temp_rate)
            {
                result2+=temp_rate;
            }
            else
            {
                result2+=data[i-1];
            }
        }
        printf("Case #%d: %d %d\n",k,result1,result2);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
