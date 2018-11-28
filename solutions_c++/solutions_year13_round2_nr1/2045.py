#include<iostream.h>
#include<conio.h>
void main()
{
int ntc;
cin>>ntc;
for(int c=1;c<=ntc;c++)
{
int ms,nm,arr[1000],msa,op=0,msl;
cin>>ms>>nm;msl=nm;
for(int q=1;q<=nm;q++) cin>>arr[q];int temp;
for(int a=nm-1;a>0;a--)
for(int b=1;b<=a;b++)
{    if(arr[b]>arr[b+1]) {   temp=arr[b];arr[b]=arr[b+1];arr[b+1]=temp;               }            }


for(int q=1;q<=nm;q++)
{ if(ms<2) { op=nm-q+1+op; break;}
if(ms>arr[q]){   ms=ms+arr[q];continue;      }
if(ms<=arr[q]) {   if(msl>(nm-q+1+op)) msl =nm-q+1+op; while(ms<=arr[q]){   ms=2*ms-1;  op++;       }   }
if(op>msl) { op=msl; break;} else {   ms=ms+arr[q];          }



}

cout<<"Case #"<<c<<": "<<op<<endl;
}}