#include<stdio.h>
int main(){
    int t ,x,r,c,p=1 ;
    scanf("%d",&t) ;
    while(t--){
        scanf("%d",&x) ;
        scanf("%d",&r) ;
        scanf("%d",&c) ;
        if(x==1){
            printf("Case #%d: Gabriel\n",p);
            
        }
        else if(x==2){
            if(r%2==0||c%2==0){
                printf("Case #%d: Gabriel\n",p);
            }
            else
            printf("Case #%d: Richard\n",p);
        }
        else if (x==3){
            if(r>=2&&c>=2&&(r*c)%3==0)
            printf("Case #%d: Gabriel\n",p);
            else
            printf("Case #%d: Richard\n",p);
        }
        else if(x==4)
        if(r>=3&&c>=3&&(r*c)%4==0)
        printf("Case #%d: Gabriel\n",p);
        else
        printf("Case #%d: Richard\n",p);
        else if(x==5)
        if(r*c>=20&&(r*c)%5==0)
        printf("Case #%d: Gabriel\n",p);
        else
        printf("Case #%d: Richard\n",p);
        else if(x==6)
        if((r*c)>=30&&(r*c)%6==0)
        printf("Case #%d: Gabriel\n",p);
        else
        printf("Case #%d: Richard\n",p);
        else
        {
            printf("Case #%d: Richard\n",p);
            
        }
        p++;
        
    }
    return 0;
}
