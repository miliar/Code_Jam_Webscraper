#include<stdio.h>
#include<string.h>
int main()
{
    FILE *input_file, *output_file;
    input_file = fopen("a2i.txt","r");
    output_file = fopen("a2o.txt","w");
    int a,b,sum;
    fscanf(input_file,"%d %d",&a,&b);
    sum=a+b;
    fprintf(output_file,"The sum is %d",sum);
    fclose(input_file);
    fclose(output_file);
    return 0;
}
