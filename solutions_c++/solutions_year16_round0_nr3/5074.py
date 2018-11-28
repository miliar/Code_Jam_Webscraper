#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;


ull div(ull x){
    if(x <= 3) return -1;
    for(ull i = 2; i*i < x; i++){
        if(x%i == 0) return i;
    }
    return -1;
}

ull boy[12];

void pbin(ull x, int N = 10){
    string ans = !x ? "0" : "";
    while(x){
        ans.push_back((x%2)+'0');
        x>>=1;
    }
    while(ans.length() < N) ans.push_back('0');
    reverse(ans.begin(), ans.end());
    printf("%s", ans.c_str()); 
}
bool test(ull mask, int N = 6){
    memset(boy, 0, sizeof boy);

   // printf("trying %d\n", mask);
   // pbin(mask,6); puts("");
    if(mask == 35){
        //pbin(mask,N); cout << endl;
    }
    ull ax = mask;
    for(int j = N-1; j >= 0; j--){ 

        for(int i = 2; i <= 10; i++){
            if(mask == 33){
                //if(i==2) printf("j: %d | i: %d | %d\n", j, i,boy[i]);
            }

            boy[i] = i*boy[i] + ((mask&(1<<j))&&1);                
            if(mask == 33){

               // if(i==2) printf("j: %d | i: %d | %d | bit: %d\n", j, i,boy[i], ((mask&(1<<j))==1));
            }            
        }
     
    }
  //  printf("-->%d\n", boy[2]);
    if(boy[2] == 35){
   //     for(int i = 2; i <=10; i++) cout << boy[i] << endl;

   }
    bool ok =1;
    for(int i = 2; i <=10; i++){
        if(boy[i] <= 0) return 0;
        if(div(boy[i]) == -1) return 0;
    }
    //printf("~ %d ~\n", ax);
    //for(int i = 2; i <=10; i++) cout << boy[i] << endl;

    return 1;
}




int main(int argc, char const *argv[]){
    

    int TT;
    int N,J;
    scanf("%d", &TT);
    for(int T = 1; T <= TT; T++){
        scanf("%d %d", &N,  &J);
        vector<int> v; 
        printf("Case #%d:\n", T);
        for(int i = 1, c = 0; i < (1<<N) && c < J; i++){ // cada mask
            if( (i&1) && (i&(1<<(N-1))) ){
                if(test(i,N)){
                   // printf("hello\n");
                    pbin(i, N);
                    for(int x = 2; x <= 10; x++){

                        //printf(" (%d,%d)", boy[x], div(boy[x]));
                        printf(" %llu", div(boy[x]));
                    }
                    printf("\n");
                    c++;
                }
            }
        }
    }

    return 0;
}