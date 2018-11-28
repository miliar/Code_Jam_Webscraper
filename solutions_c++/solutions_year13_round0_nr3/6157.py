#include <cstdlib>
#include <iostream>
#include <cmath>
#include <math.h>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("3.in", "rt", stdin);
    freopen("C.out","wt",stdout);
    int cnt,c,n,a,b;
    float i; 
    cin>>n;
    for(c=1;c<=n;c++){
        cin>>a>>b;
        cnt=0;
        for(i=a;i<=b;i++){
            if(i>=1&&i<=9){
                if(sqrt(i)==(int)(sqrt(i)))
                    cnt++;
            }
            else if(i>=10&&i<=99){
               if((int)i%11==0){
                   if(sqrt(i)==(int)(sqrt(i)))
                      cnt++;   
               }
            }
            if(i>99&&i!=1000){
                int num=(int)i%10;
                int num2=((int)i/100)%10;
                    if(num==num2){
                        if(sqrt(i)==(int)(sqrt(i))){
                            if(i!=676)
                                cnt++;
                        }
                    }
            }
        }
        printf("Case #%d: %d\n",c,cnt);
    }
    //system("PAUSE");
    return 0;//EXIT_SUCCESS;
}
