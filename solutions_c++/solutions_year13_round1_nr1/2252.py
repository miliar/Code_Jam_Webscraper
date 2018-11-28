#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int main(){

int n;
int r;
int t;
int ml;
int a[1000] = {0};
int ring = 0;

scanf("%d",&n);
for (int i=0; i<n; i++){
    scanf("%d %d",&r,&t);
//    printf(" - - %d %d\n",r,t);
    
int d=0;    
for(int p=0; p<1000; p++){
        a[p] = (r+d+1)*(r+d+1)-(r+d)*(r+d);         
//        printf("%d %d %d\n",p,r+d+1,a[p]);
        d+=2;
}

ring = 0;
int j=0;

while (t - a[j] >= 0){
       t = t - a[j];
       j++;
       ring++;
}
printf("Case #%d: %d\n", i+1, ring);
}
//if (ans == 1) printf("Case #%d: X won\n", i+1);
//if (ans == 2) printf("Case #%d: O won\n", i+1);
//if (ans == 3) printf("Case #%d: Draw\n", i+1);
//if (ans == 4) printf("Case #%d: Game has not completed\n", i+1);
//scanf("%c",&p);

  
//system("pause");
return 0;                  
}
