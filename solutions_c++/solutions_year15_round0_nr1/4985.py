#include <cstdio>
#include <iostream>

int main(){

    int t,s,q,n,need;
    scanf("%d",&t);
    char ss[1010];

    for(int i = 0; i < t; i++){
        scanf("%d ",&s);
        std::cin.getline(ss,1010);
        q = 0;
        n = 0;
        need = 0;

        for(int j = 0; j <= s; j++){
            if(j == 0) q += ss[j] - 48;
            else if(q >= j) q += ss[j] - 48;
            else{
                if(need == 0) need += j - q;
                else if(j > (q+need+n)) need += j - (q+need+n);
                n += ss[j] - 48;
            }
        }


        printf("Case #%d: %d\n",(i+1),need);
    }
}
