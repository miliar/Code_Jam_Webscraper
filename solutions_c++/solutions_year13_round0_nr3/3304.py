#include <cstdlib>
#include <iostream>
#include <math.h>

using namespace std;

bool isSys(int x){
     char buf[101];
     itoa(x, buf, 10);
     int len = strlen(buf);
     
     int ceil_half = (int)ceil(double(len)/2);
     
     for(int i=0;i<ceil_half;i++){
             if(buf[i] != buf[len-1-i])
                       return false;
     }
     return true;
}



int main(int argc, char *argv[])
{
    int num_case;
    int fairNum[100];
    int cnt = 0;
    
    for(int i=1;i<1000;i++){
            if(isSys(i) && isSys(i*i)){
                        fairNum[cnt++] = i*i;            
            }
    }
    
    //for(int i=0;i<cnt;i++)
    //        printf("%d ", fairNum[i]);
    
    
    scanf("%d", &num_case);
    for(int i=0;i<num_case;i++){
        int n,m;
        scanf("%d %d", &n, &m);

        int itemCnt = 0;        
        for(int a=0;a<cnt;a++){
             if( fairNum[a] >=n && fairNum[a] <=m){
                 itemCnt++;
             }
        }
        printf("Case #%d: %d\n", i+1,itemCnt);

                       
    }
}


