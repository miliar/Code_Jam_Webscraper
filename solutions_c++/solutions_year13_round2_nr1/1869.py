#include<cstdio>
#include<algorithm>

using namespace std;

int mote[1000005];

int main()
{
    int t;
    int a,n;
    int r,i , j ,k;
    int last;
    scanf("%d",&t);
    for(r = 0 ; r < t ; r++)
    {
        scanf("%d %d",&a,&n);
        for(i = 0 ; i < n ; i++)
        {
            scanf("%d",&mote[i]);
        }

        last = a;
        sort(mote,mote+n);
        int sum = a;
        int oper = 0;
        int last = -1;
        int oper1;
        int oper2;

        if(a == 1)
        {
            printf("Case #%d: %d\n",r+1,n);
            continue;
        }
        for(i = 0 ; i < n ;i++)
        {
            if(mote[i] >= sum)
            {
                if(sum < mote[i])
                {
                    oper1 = n-i;
                    oper2 = 0;
                    while(sum <= mote[i])
                    {
                        sum+=sum-1;
                        oper2++;
                    }

                    if(oper1 <= oper2)
                    {
                        oper += oper1;
                        break;
                    }
                    else
                    {
                        oper += oper2;
                        if(oper > n)
                        {
                            oper = n;
                            break;
                        }
                        sum += mote[i];
                    }
                }
                else if(sum == mote[i])
                {
                    sum += sum-1 + mote[i];
                    oper++;
                }
            }
            else if(mote[i] < sum)
            {
                sum += mote[i];
            }
        }

            printf("Case #%d: %d\n",r+1,oper);
    }


    return 0;
}
