#include <stdio.h>

int main()
{
    int T;
    bool digits[10];
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        long long int n;    
        scanf("%lli",&n);
        long long int count = 0,digitsCounted = 0;
        int flag=0;
        long long int newNo;
        for(int i=0;i<10;i++)
            digits[i] = 0; //initially no digits counted
        while(digitsCounted != 10)
        {
            count++;
            if(count > 10 && digitsCounted <= 3) //TODO: other cases of insomnia
            {
                printf("Case #%d: INSOMNIA\n",t);
                flag=1;
                break;
            }
            newNo = (count) * n;
            long long int temp = newNo;
            while(temp != 0)
            {
                long long int last = temp % 10;
                if(digits[last] != 1)
                {
                    digits[last] = 1;
                    digitsCounted++;
                }
                temp /= 10;
            } 
        }
        if(flag != 1)
            printf("Case #%d: %lli\n",t,newNo);    
    }//end of for loop(test cases)
}