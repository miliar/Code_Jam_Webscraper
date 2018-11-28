#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
void squareNumber();
bool is_palindrome(long val);
long limit=50,sn[50];
int main(){
    freopen("C.in","r",stdin);
    freopen("output.out","w",stdout);
    long n,i,b,j,a,count,sqa,sqb,num;
    squareNumber();
    while(scanf("%ld",&n)==1){
        for(i=1;i<=n;i++){
            scanf("%ld %ld",&a,&b);
            sqa = long(ceil(sqrt(a)));
            sqb = long(floor(sqrt(b)));
            count=0;
            for(j=sqa;j<=sqb;j++){
                if(is_palindrome(sn[j])){
                    num = long(sqrt(sn[j]));
                    if(is_palindrome(num))
                        count++;
                }
            }
            printf("Case #%ld: %ld\n",i,count);
        }
    }
    fclose(stdout);
    fclose(stdin);

return 0;
}
void squareNumber(){
    for(int index=1;index<=limit;index++){
        sn[index] = index*index;
    }
}
bool is_palindrome(long val){
    char str[100],str1[100];
    sprintf(str,"%ld",val);
    strcpy(str1,str);
    //printf("%s %s",str,str1);
    if(strcmp(str,strrev(str1))==0){
        //printf("%s %s\n",str,str1);
        return true;
       }
    return false;
}
