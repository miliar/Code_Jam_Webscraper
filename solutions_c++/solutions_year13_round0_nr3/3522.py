#include <cstdio>

bool is_palindrome(int a)
{
     if(a<10)
             return true;
     else if(a<100)
     {
          int help=(a%10)*10+a/10;
          if(help==a)
                     return true;
     }
     else
     {
         int help=a;
         int x=(a%10)*100;
         help/=10;
         x+=(help%10)*10;
         help/=10;
         x+=help;
         if(x==a)
                 return true;
     }
     return false;
}

int is_square(int a)
{
    for(int i=1;i*i<=a;i++)
    {
            if(i*i==a)
                      return i;
    }
    return 0;
}

int count_results(int a, int b)
{
        int sq;
        int counter=0;
        for(int i=a;i<=b;++i)
        {
                if(is_palindrome(i))
                {
                        sq=is_square(i);
                        if(sq!=0)
                        {
                                 if(is_palindrome(sq))
                                                      counter++;
                        }            
                }
        }
        return counter;
}


int main()
{
    FILE *fread;
    fread=fopen("C-small-attempt0.in","r");
    FILE *fwrite;
    fwrite=fopen("output.txt","w");
    int n;
    fscanf(fread,"%d", &n);
    int a,b;
    for(int i=0;i<n;++i)
    {
            fscanf(fread,"%d", &a);
            fscanf(fread,"%d", &b);
            fprintf(fwrite, "Case #%d: %d\n", i+1, count_results(a,b));
    }
    fclose(fwrite);
    fclose(fread);
    return 0;
}
