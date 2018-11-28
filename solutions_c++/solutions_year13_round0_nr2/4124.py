#include <stdio.h>
//#include<iostream.h>
//#include<conio.h>
using namespace std;
main()
{
//taking 1st square as a[1][1]
int a[101][101], row[101], col[101];
int test, n, m;
//printf("enter the no of test cases:-");
FILE *file, *out;
    file=fopen("inputashu.txt", "r");
    out=fopen("outputashu.txt", "w");
    fscanf(file,"%d", &test);
for(int i=1; i<=100; i++)
{
row[i]=1;
col[i]=1;
}
for(int t=1; t<=test; t++)
{
int flag=0;
//printf("enter N=");
fscanf(file,"%d", &n);
//printf("enter M=");
fscanf(file,"%d", &m);
/*for(int i=1; i<=n; i++)
row[i]=1;
for(int i=1; i<=m; i++)
col[i]=1;
*/

for(int i=1; i<=n; i++ )
{
for(int j=1; j<=m; j++)
{
//printf("a[%d][%d]=", i, j);
fscanf(file,"%d", &a[i][j]);
}
}
int max;
// row ke lie
for(int r=1; r<=n; r++)
{
max=a[r][1];
for(int c=1; c<=m; c++)
{

if(a[r][c]>max)
{
max=a[r][c];
}
}
row[r]=max;
}

// column ke lie
for(int c=1; c<=m; c++)
{
max=a[1][c];
for(int r=1; r<=n; r++)
{
if(a[r][c]>max)
{
max=a[r][c];
}
}
col[c]=max;
}

// now I traverse the array and for each 1 I will check row and column such that this must contain all 1's
for(int r=1; r<=n; r++)
{
for(int c=1; c<=m; c++)
{
if(a[r][c]!= row[r] && a[r][c]!= col[c])
{
fprintf(out,"Case #%d: NO\n", t);
flag=1;
break;

}
}
if(flag==1)
break;
}
if(flag==1)
continue;
fprintf(out,"Case #%d: YES\n", t);
}
//getch();
}
