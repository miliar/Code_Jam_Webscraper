#include <bits/stdc++.h>
using namespace std;
int plate[1005],d;

void merge (int *a,int start,int mid,int end)
{
     int k,n1=mid-start+1,n2=end-mid,i=0,j=0;
     int l[mid-start+1],r[end-mid];
     for(k=0;k<n1;k++) l[k] = a[start+k];
     for(k=0;k<n2;k++)  r[k] = a[mid+k+1];
     for(k=start;k<=end;k++)
     {
            if(n1 && n2)
            {
                   if(l[i]<=r[j])
                   {
                         a[k] = l[i];
                         i++;
                         n1--;
                   }
                   else if(l[i]>r[j])
                   {
                        a[k] = r[j];
                         j++;
                         n2--;
                   }
            }
            else if(!n1)
            {
                 while(n2>0)
                 {
                         a[k] = r[j];
                         j++;
                         n2--;
                         k++;
                 }
            }
            else if(!n2)
            {
                 while(n1>0)
                 {
                         a[k] = l[i];
                         i++;
                         n1--;
                         k++;
                 }
            }
     }
     return ;
}
void merge_sort(int * a,int start,int end)
{
     if(end<=start)
     return ;
     int mid;
     mid=(start+end)/2;
     merge_sort(a,start,mid);
     merge_sort(a,(mid+1),end);
     merge(a,start,mid,end);
     return ;
}
int f(int val)
{
	   if(plate[d-1]<=val)return 1;
	   int flag = 0;
	   int i,j;
	   int ex,tmp;
	   int highest;
	   double l;
	   for(i=1;i<val;i++)
	   {
	   	     ex = 0;
	   	     highest = val-i;
	   	     for(j=d-1;j>=0;j--)
	   	     {
	   	     	    l = (double)plate[j]/(double)highest;
	   	     	    tmp = (int)ceil(l);
	   	     	    ex +=tmp-1;
	   	     	    if(ex>i)
	   	     	    break;
	   	     }
	   	     if(ex<=i)
	   	     {
	   	     	  flag = 1;
	   	     	  break;
	   	     }
	   }
	   return flag;
}
int bin_search()
{
	   merge_sort(plate,0,d-1);
	   int hi = plate[d-1];
	   int lo = 1;
	   int mid ;
	   while(lo+1<hi)
	   {
	   	     mid = (lo+hi)/2;
	   	     if(f(mid))
	   	     hi = mid;
	   	     else
	   	     lo = mid+1;
	   }
	   if(f(lo))return lo;
	   else return hi;
}
int main()
{

	 int t,i,j,ans;
	 freopen("in.txt","r+",stdin);
	 freopen("out.txt","w+",stdout);
	 cin>>t;
	 for(i=1;i<=t;i++)
	 {
	 	   cin>>d;
	 	   for(j=0;j<d;j++)cin>>plate[j];
	 	   ans = bin_search();
	 	   printf("Case #%d: %d\n",i,ans);
	 }
	 return 0;
}
