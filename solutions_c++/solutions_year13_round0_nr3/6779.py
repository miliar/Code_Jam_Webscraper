#include<cstdio>
#include<cmath>
using namespace std;

int ispalin(int num)
{
   int n = num, rev=0, dig;
   while(num>0)
   {
       dig = num % 10;
       rev = rev * 10 + dig;
       num = num / 10;
   }
   if (n == rev) return 1;
   else return 0;
}

void getResult(int s, int e, int j)
{
   double start = sqrt(double(s));
   int end = sqrt(double(e));
   int count=0;
   for(int i=ceil(start); i<=end; i++)
   {
       if(ispalin(i) && ispalin(i*i))   count++;
   }
   printf("Case #%d: %d\n",j,count);
}
int main()
{
   int tcase, start, end, j=1;
   scanf("%d", &tcase);
   while(tcase--)
   {
       scanf("%d %d", &start, &end);
       getResult(start, end, j);
       j++;
   }
}