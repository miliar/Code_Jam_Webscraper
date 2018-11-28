#include <cstdio>
#include <cmath>

int isPalindrome(int n){
    char arr[100];
    int r = n;
    int i=0;
    while(r>0){
        arr[i] = '0' + r%10;
        r/=10;
        i++;
    }
    arr[i]='\0';
    for(int j=0; j<i/2; j++){
        if(arr[j]!=arr[i-j-1]){
            return 0;
        }
    }
    //printf("%s: palin\n", arr);
    return 1;

}

int main (){
    int t, c=1;
    FILE *output = fopen("Coutput.txt", "w");
    scanf("%d", &t);
    while(c<=t){
        int n1, n2;
        scanf("%d %d", &n1, &n2);
        int count=0;
        for(int i=n1; i<=n2; i++){
            if(isPalindrome((i))){
                double res = sqrt(i);
                int res2 = sqrt(i);
                if(res2==res){
                    if(isPalindrome(res2)){
                        count++;
                    }
                }
            }
        }
        fprintf(output, "Case #%d: %d\n", c, count);
        c++;
    }
    fclose(output);
    return 0;
}
