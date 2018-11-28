#include <iostream>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
using namespace std;
typedef long long int int64;
int64  _mergeSort(int64 arr[], int64 temp[], int64 left, int64 right);
int64 merge(int64 arr[], int64 temp[], int64 left, int64 mid, int64 right);
int64 mergeSort(int64 arr[], int64 array_size)
{
    int64 *temp = (int64 *)malloc(sizeof(int64)*array_size);
    return _mergeSort(arr, temp, 0, array_size - 1);
}
int64 _mergeSort(int64 arr[], int64 temp[], int64 left, int64 right)
{
  int64 mid, inv_count = 0;
  if (right > left)
  {
    mid = (right + left)/2;
    inv_count  = _mergeSort(arr, temp, left, mid);
    inv_count += _mergeSort(arr, temp, mid+1, right);
    inv_count += merge(arr, temp, left, mid+1, right);
  }
  return inv_count;
}
int64 merge(int64 arr[], int64 temp[], int64 left, int64 mid, int64 right)
{
  int64 i, j, k;
  int64 inv_count = 0;
  
  i = left; 
  j = mid;  
  k = left; 
  while ((i <= mid - 1) && (j <= right))
  {
    if (arr[i] <= arr[j])
    {
      temp[k++] = arr[i++];
    }
    else
    {
      temp[k++] = arr[j++];
      inv_count = inv_count + (mid - i);
    }
  }
  while (i <= mid - 1)
    temp[k++] = arr[i++];
  while (j <= right)
    temp[k++] = arr[j++];
  for (i=left; i <= right; i++)
    arr[i] = temp[i];
  
  return inv_count;
}
int64 findinversion(int64 a[],int64 n)
{
 int64 i,j,count=0;
 
 for(i=0;i<n;i++)
 {
  for(j=i+1;j<n;j++)
       {
   if(a[i]>a[j])
   count++;
    }
 }
 return count;
}
int main(){
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int64 i,j,k,n,t,cnt=1,ans,x,a[100001],vl,mxi,mx,ar1[100001],ar2[100001],ne1,ne2;
  cin>>t;
  while(t--){
    scanf("%lld",&n);ans=1000000000;mx=-1;
    for(i=0;i<n;i++)scanf("%lld",&a[i]);
    //for(i=0;i<n;i++)if(a[i]>mx){mx=a[i];mxi=i;} 
    if(n<=2){ printf("Case #%lld: 0\n",cnt);cnt++;continue;}
    vl=0;
    for(i=0;i<n;i++){
      ne1=ne2=0;
      for(j=0;j<i;j++)if(a[j]>a[i])ne1++;
      for(j=i+1;j<n;j++)if(a[j]>a[i])ne2++;      
      vl+=min(ne1,ne2); 
    }  
    printf("Case #%lld: %lld\n",cnt,vl);
    cnt++;
  }
  return 0;
}

