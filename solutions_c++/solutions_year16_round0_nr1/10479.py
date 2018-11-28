#include <cstdio>
#include <math.h>

bool digits[10]={0};
int sum() {
    int sum=0;
    for(int i=0; i<10; i++)
        sum+=digits[i];
    return sum;
}


int T, k,coef;
long nb, nb0;


int main() {
        FILE *output,*input; 
    input = fopen("./input.txt", "r");
    output = fopen("./output.txt", "w"); 
    if((input == NULL)||(output == NULL))
    {
        printf("error reading file");
        return 0;
    }
        printf("start\n");
        fscanf(input,"%d", &T);
        for (int r = 1; r <= T; ++r) {
                fscanf(input,"%d", &nb0);
                fprintf(output,"Case #%d:", r);
                printf("case %d \n",r);
                coef = 1;
                for(int j=0; j<10;j++)
                        digits[j]=0;
                do {
                        nb=nb0*coef;
                        k=0;
                        do{
                                digits[(nb/(int)pow(10,k))%10]=1;
                                k++;
                        }while(nb/(int)pow(10,k) != 0);
                        coef++;
                } while ((sum() < 10)&&(coef<100));
                if(sum() == 10)
                        fprintf(output," %d\n",nb);
                else
                        fprintf(output," INSOMNIA\n");
        }
        return 0;
}