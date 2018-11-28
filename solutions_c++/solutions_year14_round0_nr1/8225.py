#include <cstdio>
#include <algorithm>
using namespace std;
int arr[4][4];
int arr1[4][4];
int readint()  {
    int ret=0,a=getchar_unlocked();
    for(;a<'0' || a>'9';)   a=getchar_unlocked();
    for(;a>='0' && a<='9';){
        ret=ret*10+a-'0';
        a=getchar_unlocked();
    }
    return ret;
}
int main(void)
{
   int ab,T;T=readint();
   for(ab=1;ab<=T;ab++){
       int r1=0,r2=0,count=0,temp=0;
       //For inputting first input matrix
       r1=readint();
       for(int i=1;i<=4;i++){
           for(int j=1;j<=4;j++)    arr[i][j]=readint();
       }
       //for inputing 2nd input matrix
       r2=readint();
       for(int i=1;i<=4;i++){
           for(int j=1;j<=4;j++)    arr1[i][j]=readint();
       }
       //for calculation of common number
       for(int i=1;i<=4;i++){
           for(int j=1;j<=4;j++){
                if(arr[r1][i]==arr1[r2][j]){++count;if(count==1) temp=arr[r1][i];}    
           }
       }
       if(count==1) printf("Case #%d: %d\n",ab,temp);
       else if(count>1) printf("Case #%d: Bad magician!\n",ab);
       else printf("Case #%d: Volunteer cheated!\n",ab);
   }
   return 0;
}

