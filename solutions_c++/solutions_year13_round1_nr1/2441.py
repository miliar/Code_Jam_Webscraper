#include <iostream>

using namespace std;

int main()
{
    int n,ri=1;
    scanf("%d",&n);
    while (n--)
    {
        long long r,t;
        scanf("%I64d %I64d",&r,&t);
        long long begin = 1,end = t,mid = (begin+end)/2;
        while (begin <= end)
        {
            mid = (begin+end)/2;
            if ((2*r+2*mid-1)*mid-t<0) begin = mid+1;
            else if ((2*r+2*mid-1)*mid-t>0) end = mid-1;
            else break;
        }
        if ((2*r+2*mid-1)*mid-t>0) mid--;
        printf("Case #%d: %I64d\n",ri++,mid);
    }
    return 0;
}
