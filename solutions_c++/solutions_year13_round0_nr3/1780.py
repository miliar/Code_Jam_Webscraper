#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <cmath>

int t;
long long a,b;

bool pal(long long n)
{
 char buff[20];
 sprintf(buff, "%I64d", n);
 int l = strlen(buff);
 for(int i=0,j=l-1;i<j;i++,j--)
  if(buff[i]!=buff[j]) return false;
 return true;
}

long long v[39];

int main()
{
 v[0]=1;
 v[1]=4;
 v[2]=9;
 v[3]=121;
 v[4]=484;
 v[5]=10201;
 v[6]=12321;
 v[7]=14641;
 v[8]=40804;
 v[9]=44944;
 v[10]=1002001;
 v[11]=1234321;
 v[12]=4008004;
 v[13]=100020001;
 v[14]=102030201;
 v[15]=104060401;
 v[16]=121242121;
 v[17]=123454321;
 v[18]=125686521;
 v[19]=400080004;
 v[20]=404090404;
 v[21]=10000200001;
 v[22]=10221412201;
 v[23]=12102420121;
 v[24]=12345654321;
 v[25]=40000800004;
 v[26]=1000002000001;
 v[27]=1002003002001;
 v[28]=1004006004001;
 v[29]=1020304030201;
 v[30]=1022325232201;
 v[31]=1024348434201;
 v[32]=1210024200121;
 v[33]=1212225222121;
 v[34]=1214428244121;
 v[35]=1232346432321;
 v[36]=1234567654321;
 v[37]=4000008000004;
 v[38]=4004009004004;

 /*
 freopen("gcj2013_c_aux.cpp","w",stdout);
 int c=0;
 for(long long i=1l;i<=10000000l;i++)
 {
  if(pal(i))
  {
   long long candidato = i*i;
   if(pal(candidato)){ printf(" v[%d]=%I64d;\n",c,candidato);c++;}
  }
 }
 return 666;
 * */
 
 //freopen("C-large-1.in", "r", stdin);
 //freopen("C-large-1.out", "w", stdout);
 scanf("%d", &t);
 for(int i=1;i<=t;i++)
 {
  scanf("%I64d %I64d", &a, &b);
  printf("Case #%d: ", i);
  int c = 0;
  if(a>b) std::swap(a,b);
  for(int j=0;j<39;j++)
  {
   if(v[j]>=a && v[j]<=b) c++;
  }
  printf("%d\n", c);
 }
}
