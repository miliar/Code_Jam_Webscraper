#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<iomanip>
#include<fstream>
using namespace std;
#define getchar_unlocked getchar
#define ll long long int
inline long long int in()
{
   long long int n=0;
   long long int ch=getchar_unlocked();
   long long int sign=1;
   while( ch < '0' || ch > '9' )
   {
   	if(ch=='-')sign=-1; ch=getchar_unlocked();
	   }
 
   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getchar_unlocked();
   return n*sign;
}
double b1[1002];
void merge(double a[],long long int low,long long int mid ,long long int high);

void mergesort(double a[],long long int i1,long long int j)
{
   long long int mid;
   if(i1<j)
   {
      mid=(i1+j)/2;
      mergesort(a,i1,mid);
      mergesort(a,mid+1,j);
      merge(a,i1,mid,j);
   }
}
void merge(double a[],long long int low,long long int mid ,long long int high)
{
   long long int h,i,j,k;
   h=low;
   i=low;
    j=mid+1;
   while(h<=mid && j<=high)
   {
      if(a[h]<=a[j])
	 b1[i]=a[h++];
      else
	 b1[i]=a[j++];
      i++;
   }
 
   if( h > mid)
      for(k=j;k<=high;k++)
	b1[i++]=a[k];
   else
      for(k=h;k<=mid;k++)
	 b1[i++]=a[k];
 
   //printf("sorted array:\n");
  for(k=low;k<=high;k++)
   {  a[k]=b1[k];
  //    printf("%lld  ",a[k]);
   }
   //printf("\n");*/
}


int main()
{
	freopen("D-large.in","r",stdin);
	freopen("Problem_d_large_output.txt","w",stdout);
	ll n;
	double ar1[1001],ar2[1001];
	double ar1dup[1001],ar2dup[1001];
	cin>>n;
	for(int t=1;t<=n;t++)
	{
		ll num,ct=0;
		double maxm;
		num=in();
		for(int i=0;i<num;i++)
		cin>>ar1[i],ar1dup[i]=ar1[i];
		for(int i=0;i<num;i++)
		cin>>ar2[i],ar2dup[i]=ar2[i];;
		mergesort(ar1,0,num-1);
		mergesort(ar2,0,num-1);
		mergesort(ar1dup,0,num-1);
		mergesort(ar2dup,0,num-1);
	//	for(int i=0;i<num;i++)
	//	cout<<ar1[i]<<"\n";
	//	for(int i=0;i<num;i++)
	//	cout<<ar2[i]<<"\n";		
	
		ll flag,ans1=0,ans2=0;
	
		//normal war
		for(int i=0;i<num;i++)
		{
			flag=0;
			for(int j=0;j<num;j++)
			{
				if(ar1[i]<ar2dup[j]&&ar2dup[j]!=-1)
				{
					ar2dup[j]=-1;
					flag=1;
					break;	
				}
			}
			if(flag==0)
			ans1++;
			
		}
		
		//deceitful war
		for(int i=0;i<num;i++)
		{
			flag=0;
			for(int j=0;j<num;j++)
			{
				if(ar2[i]<ar1dup[j]&&ar1dup[j]!=-1)
				{
					ar1dup[j]=-1;
					flag=1;
					break;	
				}
			}
			if(flag==1)
			ans2++;
			
		}

		cout<<"Case #"<<t<<": "<<ans2<<" "<<ans1<<"\n";
	}
}
