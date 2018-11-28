#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int main(){

int pal[5] = {1,4,9,121,484};
int min = 0;
int max = 0;
int ans = 0;
int t;

scanf("%d\n",&t);
for (int i=0; i<t; i++) {
    scanf("%d %d", &min, &max);
  
ans = 0;
for (int j=0; j<5; j++)
   if (pal[j] >= min && pal[j] <= max) ans++;

printf("Case #%d: %d\n", i+1, ans);

}
  
//system("pause");
return 0;                  
}
