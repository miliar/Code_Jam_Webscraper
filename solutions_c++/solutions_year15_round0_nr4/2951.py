#include <fstream>

using namespace std;

int main(){
    FILE * f;
    FILE * out;
    f = fopen("small.txt", "r");
    out = fopen("small_out.txt", "w");

    int t;
    fscanf(f, "%i", &t);
    for(int i = 0; i < t; i++){
        int x, r, c;
        int richard_wins = false;
        fscanf(f, "%i", &x);
        fscanf(f, "%i", &r);
        fscanf(f, "%i", &c);
        if(x >= 7){
            fprintf(out, "Case #%i: RICHARD\n", i+1);
            continue;
        }
        else if(r*c%x != 0){
            fprintf(out, "Case #%i: RICHARD\n", i+1);
            continue;
        }else if(x == 1 || x == 2){
            fprintf(out,"Case #%i: GABRIEL\n", i+1 );
        }else if(max(r, c) >= x && min(r,c) >= x - 1){
            fprintf(out,"Case #%i: GABRIEL\n", i+1 );
        }else{
            fprintf(out,"Case #%i: RICHARD\n", i+1 );
        }
    }

    return 0;
}
