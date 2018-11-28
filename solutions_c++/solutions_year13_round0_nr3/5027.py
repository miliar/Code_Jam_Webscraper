#include<cstdio>
using namespace std;
FILE *fr, *fw;
unsigned long long a[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
void getResult(long long s, long long e, int j)
{
    int count=0, p=0;
    while(s > a[p++]);  p--;
    for(int i=p; a[i]<=e; i++)
    {
        count++;
    }
    fprintf(fw, "Case #%d: %d\n",j,count);
}
int main()
{
    int tcase, j=1;
    long long start, end;
    fr = fopen ("C-small-attempt0.in", "rt");
    fw = fopen ("Large_op1.txt", "w+");
    fscanf(fr, "%d", &tcase);
    while(tcase--)
    {
        fscanf(fr, "%lld %lld", &start, &end);
        getResult(start, end, j);
        j++;
    }
}
