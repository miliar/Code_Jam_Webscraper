#include <cstdio>
#include <string>

using namespace std;

FILE* infile;
FILE* outfile;

int T, x;
char a, b;

int main(){
    infile = fopen("pancakesin.txt", "r");
    outfile = fopen("pancakesout.txt", "w");

    fscanf(infile, "%d ", &T);

    printf("%d", T);

    for(int i = 0; i<T; i++){
        x = 0;
        a = 'a';
        b = 'b';
        while(true){
            a = b;
            fscanf(infile, "%c", &b);
            if(b!='+'&&b!='-'){
                if(a=='+'){
                    x-=1;
                }
                break;
            }else{
                if(b!=a){
                    x+=1;
                }
            }
        }
        fprintf(outfile, "Case #%d: %d\n", i+1,x);
    }
}
