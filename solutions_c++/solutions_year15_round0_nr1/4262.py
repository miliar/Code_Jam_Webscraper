#include <iostream>
using namespace std;

int main ()
{
int t;
scanf("%d",&t);
for (int t1(1);t1<=t;t1++)
{
int smax;
char a[10000];
scanf("%d%s",&smax,a);int total(0);int untilnow(0);
for (int c(0);c<strlen(a);c++)
{
if (a[c]-'0'>0&&c>untilnow)total+=c-untilnow,untilnow=c;
untilnow+=a[c]-'0';
}
cout <<"Case #" << t1 << ": " <<  total << endl;
}
}
