#include<iostream>

#include<algorithm>

using namespace std;

int main()

{

int t,n,count,p,i,j,k;

double a[1000],b[1000];

scanf("%d",&t);

for(p=1;p<=t;p++)

{

count=0;

scanf("%d",&n);

for(i=0;i<n;i++)

scanf("%lf ",&a[i]);

for(i=0;i<n;i++)

scanf("%lf ",&b[i]);

sort(a,a+n);

sort(b,b+n);

k=0;

for(i=0;i<n;i++)

{

for(j=k;j<n;j++)

if(b[j]>a[i])

{

count++;

j++;

break;

}

k=j;

}

i=j=k=0;

for(;i<n&&j<n;)

if(a[i]>b[j])

{

i++;

j++;

k++;

}

else

i++;

printf("Case #%d: %d %d\n",p,k,n-count);

}

return 0;

}