#include<stdio.h>
#include<fstream>
#include<stdlib.h>
#include<iostream>
using namespace std;
void Qsort(double *arr,int n)
{
	for(int i=1;i<=n;i++)
	{
	for(int j=1;j<=n-i;j++)
    {
   if(arr[j]>arr[j+1])
	swap(arr[j+1],arr[j]);
    }
	}
}
int main()
{
ifstream f1;
    ofstream f2;
    f1.open("A.in",ios::in);
     f2.open("B.in",ios::out);
int t,n,i=0,ans1=0,ans2=0,ia=1;
double arr[1003],arr2[1003];
f1>>t;
//scanf("%d",&t);
while(ia<=t)
{
ans1=0;ans2=0;
f1>>n;
//scanf("%d",&n);
i=1;
while(i<=n)
{
f1>>arr[i];
//scanf("%lf",&arr[i]);
i++;
}
i=1;
while(i<=n)
{
f1>>arr2[i];
//scanf("%lf",&arr2[i]);
i++;
}
Qsort(arr,n);//asc winner nenny
Qsort(arr2,n);//asc looser ken

/*for(int i=1;i<=n;i++)
cout<<arr[i]<<"  ";
cout<<"\n";
for(int i=1;i<=n;i++)
cout<<arr2[i]<<"  ";
cout<<"\n";
*/
ans1=0;
for(int i=1,j=1;i<=n && j<=n;)
{
if(arr[i]<arr2[j])
{
i++;j++;
}
else
{
ans1++;
j++;
}
}
ans2=0;
for(int i=1,i1=1,j=n,j1=n;i<=n;)
{
if(arr[i]<arr2[i1])
{j1--;i++;
}
else
{
ans2++;i++;i1++;
}
}
f2<<"Case #"<<ia<<": "<<ans2<<" "<<ans1<<"\n";
//printf("%d %d",ans1,ans2);
ia++;
}
f1.close();
f2.close();
//cin>>t;
}
