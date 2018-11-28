#include <stdio.h>

int num[10];

void reset();
int judge();
void check(int input);

int main(void)
{
    int TC, TC_i=1;
    scanf("%d",&TC);

    if (TC > 100)
    {   
        printf("The number of test cases must be under 100\n");
        return 0;
    }   

    while (TC_i <= TC) 
    {   
        reset();
        printf("Case #%d: ", TC_i);

        int input_n;
        scanf("%d",&input_n);
        if (input_n > 1000000)
        {   
            printf("The number of datasets must be under 200\n");
            return 0;
        }   

        if (input_n == 0)
        {   
            printf("INSOMNIA\n");
            TC_i++;
            continue;
        }   

        int i=1;
        while(!judge())
        {   
            check(input_n * i); 
            i++;
        }   
        printf("%d\n",input_n*(i-1));

        TC_i++;
    }   

    return 0;
}

void reset()
{
    int i;
    for(i=0;i<10;i++)
        num[i]=0;
}

int judge()
{
    int flag=1;
    int i;
    for(i=0;i<10;i++)
    {
        if(num[i] == 0)
            flag=0;
    }
    return flag;
}

void check(int input)
{
        int temp = input;
        while(temp >= 10)
        {
            num[temp%10] = 1;
//            printf("%d\n", temp%10);
            temp = temp / 10;
        }
        num[temp] = 1;
//        printf("%d\n", temp);
}
