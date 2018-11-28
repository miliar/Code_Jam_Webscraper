#include<stdio.h>
#include<math.h>
bool isPal(int n)
{
    int rev=0,num=n;
    while(num!=0)
    {
        rev=rev*10+num%10;
        num/=10;
    }
    if(n==rev) return true;
    else return false;
}
bool isSquareOfPal(int n)
{
     int h = n & 0xF;
    if (h > 9)
        return false;
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        int t = (int) floor( sqrt((double) n) + 0.5 );
        if(t*t==n)
            return isPal(t);
            else return false;
    }
    return false;
}
int main()
{
    int n,i,j,k;
    long a,b;
    char c;
    int count;
    FILE *fin=fopen("D:/Downloads/C-small-attempt0.in","r");
    fscanf(fin,"%d",&n);
    FILE *fout=fopen("C:/Users/Priyank/Desktop/output.txt","w");
    for(i=0;i<n;i++)
    {
        c=fgetc(fin);
        count=0;
        fscanf(fin,"%ld",&a);
        fscanf(fin,"%ld",&b);
        for(j=a;j<=b;j++)
        {
            if(isPal(j))
            {
                if(isSquareOfPal(j))
                    count++;
            }
        }
        fprintf(fout,"\nCase #%d: %d",i+1,count);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}

