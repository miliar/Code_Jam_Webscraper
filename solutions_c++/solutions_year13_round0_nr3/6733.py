#include<stdio.h>
#include<math.h>

int arr[1010];

int pal(int n){
    int temp=0,count=0;
    int a,b;
    int m=n,l=n;
    while(n>0){
          n=n/10;
          temp++; 
    }
    for(int i=1;i<=temp/2;i++){
        a=l%10;
        int yaa=1;
        for(int j=1;j<=temp-i;j++) yaa*=10;
        b=m/yaa;
        b=b%10;
        //printf("a=%d b=%d\n",a,b);
        if(a!=b){
            count=1;
            break;
        }
        l=l/10;
    }
    return count;
}

int sqr(int n){
    double a,m;
    m=double(n);
    int b=1;
    a=sqrt(m);
    int c=(int)a;
    if(c*c==n){
        if(c>=10){
            b=pal(c);
        }
        else{
            b=0;   
        }
    }
    return b;
}

int main(){
    int t,a,b;
    int temp;
    
    for(int i=1;i<1010;i++){
        arr[i]=0;
        if(i>=10){
            temp=pal(i);
            if(temp==0){
                temp=sqr(i);
                if(temp==0) arr[i]=1;    
            }
        }
        else{
            double x,y;
            y=(double)i;
            x=sqrt(i);
            temp=(int)x;
            if(temp*temp==i) arr[i]=1;   
        }
    }
    
    scanf("%d",&t);
    
    for(int i=1;i<=t;i++){
        scanf("%d %d",&a,&b);
        int count=0;
        for(int j=a;j<=b;j++){
            if(arr[j]==1){
                count++;
                //printf("%d\n",j);
            }   
        }
        printf("Case #%d: %d\n",i,count);
    }
 
 
 while(getchar()!=EOF);
 return 0;   
}
