#include<stdio.h>
#include<stdlib.h>
int main()
{
    int t , n , sum , k , i , j , output;
    char output2[10];
    char s[11];
    char p[11];
    char ch[11];
    FILE *fp , *fp2;
    if((fp = fopen("A-small-attempt5.in" , "r")) == NULL)
    {
        exit(1);

    }
    fgets(ch,5,fp);
    t = atoi(ch);

    if((fp2 = fopen("out.txt" , "w")) == NULL)
    {
        exit(1);

    }
    for(i = 0 ; i < t ; i++)
    {
        fgets(ch,2,fp);

        n = atoi(ch);

            fgets(s , 11 , fp);


        sum = 0;
        output = 0;
        for(j = 1 ; j <= n+1 ; j++)
        {
            k = (int) s[j];
            k = k-48;

            if(k > 0)
            {
                if(j <= (sum + 1))
                    sum += k;
                else
                {
                    output += (j - sum - 1) ;
                    sum += (output + k);
                }

            }


        }

        itoa(output , output2 , 10);
        itoa(i+1 , p , 10);
        fputs("Case #",fp2);
        fputs(p,fp2);
        fputs(": ",fp2);;
        fputs(output2,fp2);
        fputs("\n",fp2);
    }
    fclose(fp);
    fclose(fp2);
    return 0;
}
