#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

#include<stdio.h>

using namespace std;

int  mi(int a ,int b){
    if(a<b)
        return a ;
    return b ;
}
int mini(int arr[])
{
    int i,brr[10],crr[10],drr[10],err[10] ;
    for(i=0;i<=9;i++)
        brr[i]=arr[i] ;
for(i=0;i<=9;i++)
        crr[i]=arr[i] ;
for(i=0;i<=9;i++)
        drr[i]=arr[i] ;
for(i=0;i<=9;i++)
        err[i]=arr[i] ;
    if(arr[9]>=4)
 {

     return 9 ;
 }
 else if(arr[9]==3&&(arr[6]>0||arr[7]>0||arr[8]>0))
    return 9 ;
else if(arr[7]>2&&(arr[9]>1))
    return 9 ;
else if(arr[7]>2&&(arr[8]>0))
    return 8 ;
else if(arr[8]>3&&arr[9]==0)
    return 8 ;
else if(arr[8]>3&&arr[9]>0)
    return 9 ;
    else if(arr[8]>2&&arr[9]>0)
    return 9 ;

    for(i=9;i>=0;i--)
    {
        if(arr[i]>0)
        break;
    }

    if(i<4)
        return i;
    else
        {
            for(int  k=1;k<=9;k++)

            {
                if(arr[k]){

                    if(k>=1)
                    arr[k-1]=arr[k] ;
                    arr[k]=0 ;
                }
            }
        arr[0]=0 ;
        brr[0]=0;
        for(i=9;i>=0;i--){
            if(brr[i]>0)
                break ;
        }
        brr[i]-- ;
	crr[i]--;
	drr[i]--;
	err[i]--;

        if(i==9)
{brr[i/2]++;
brr[i-i/2]++;
crr[i/2-1]++;
crr[i-i/2+1]++;
drr[i/2-2]++;
drr[i-i/2+2]++;
err[i/2-3]++;
err[i-i/2+3]++;
return 1+mi(mi(mini(arr),mini(brr)),mi(mi(mini(crr),mini(drr)),mini(err)));



}
if(i==8)
{brr[i/2]++;
brr[i-i/2]++;
crr[i/2-1]++;
crr[i-i/2+1]++;
drr[i/2-2]++;
drr[i-i/2+2]++;
err[i/2-3]++;
err[i-i/2+3]++;
return 1+mi(mi(mini(arr),mini(brr)),mi(mi(mini(crr),mini(drr)),mini(err)));



}
if(i==7)
{brr[i/2]++;
brr[i-i/2]++;
crr[i/2-1]++;
crr[i-i/2+1]++;
drr[i/2-2]++;
drr[i-i/2+2]++;

return 1+mi(mi(mini(arr),mini(brr)),mi(mini(crr),mini(drr)));



}
if(i==6)
{brr[i/2]++;
brr[i-i/2]++;
crr[i/2-1]++;
crr[i-i/2+1]++;
drr[i/2-2]++;
drr[i-i/2+2]++;

return 1+mi(mi(mini(arr),mini(brr)),mi(mini(crr),mini(drr)));



}
if(i==5)
{brr[i/2]++;
brr[i-i/2]++;
crr[i/2-1]++;
crr[i-i/2+1]++;


return 1+mi(mi(mini(arr),mini(brr)),mini(crr));



}

if(i==4)
{brr[i/2]++;
brr[i-i/2]++;
crr[i/2-1]++;
crr[i-i/2+1]++;


return 1+mi(mi(mini(arr),mini(brr)),mini(crr));



}


return 0 ;

       // return (1+ mi(minii(arr),minii(brr)));
           }

return 0 ;
}

int main(){
    int t ,d,arr[11],k,p=0 ;
    cin>>t ;
    while(t--){
        p++ ;
        for(int i=0;i<11;i++){
            arr[i]=0 ;
        }
        cin>>d ;
        for(int i=0;i<d;i++){
            cin>>k ;
            arr[k]++;

        }
          int c=mini(arr) ;
        printf("Case #%d: %d\n",p,c) ;
    }

return 0;

                  }
