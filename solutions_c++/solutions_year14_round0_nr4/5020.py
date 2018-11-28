#include<iostream.h>
#include<conio.h>
#include<fstream.h>


ifstream fin("a.txt");
ofstream fout("ans.txt");

float nauman[12],ken[12];
int input,war=0,deceit_war=0;


void merge(int beg,int mid,int end,float * arr)
{
 float left[20];
 float right[20];
 for(int i=beg;i<=mid;i++)
  left[i]=arr[i];
 for(i=mid+1;i<=end;i++)
  right[i]=arr[i];
 i=beg;
 int j=mid+1;
 int l=beg;
 while(i<=mid&&j<=end)
 {
  if(left[i]<right[j])
  {
   arr[l]=left[i];
   i++;
  }
  else
  {
   arr[l]=right[j];
   j++;
  }
  l++;
 }
 while(i<=mid)
 {
  arr[l]=left[i];
  i++;
  l++;
 }
 while(j<=end)
 {
  arr[l]=right[j];
  j++;
  l++;
 }
}


void merge_sort(int beg,int end,float * arr)
{
 int mid=(beg+end)/2;
 if(beg<end)
 {
  merge_sort(beg,mid,arr);
  merge_sort(mid+1,end,arr);
  merge(beg,mid,end,arr);
 }
}

void cal_cases(int cse)
{
 war=0;
 deceit_war=0;
 int temp=input-1;
 merge_sort(0,input-1,nauman);
 merge_sort(0,input-1,ken);
 for(int i=input-1;i>=0;i--)
 {
  if(nauman[i]>ken[temp])
  {
   war++;
  }
  else if(nauman[i]<ken[temp])
  {
   temp=temp-1;
  }
 }
 temp=0;
 for(i=0;i<=input-1;i++)
 {
  if(nauman[i]>ken[temp])
  {
   deceit_war++;
   temp++;
  }
 }
 fout<<"Case #"<<cse+1<<": "<<deceit_war<<" "<<war<<"\n";
}



void main()
{
 clrscr();
 int total;
 fin>>total;
 for(int i=0;i<total;i++)
 {
  fin>>	input;
  for(int k=0;k<input;k++)
   fin>>nauman[k];
  for(k=0;k<input;k++)
   fin>>ken[k];
  cal_cases(i);
 }
 getch();
}
