#include <stdio.h>
#include <vector>
#include <stdlib.h>
#include <string.h>
#include <string>
using namespace std;

vector<int> aud;

int main(){
    int test_case;
    FILE *file = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");
    fscanf(file,"%d", &test_case);
    for(int z=1;z<=test_case;z++){
        char tmp;
        int sMax, cnt=0, total=0;
        fscanf(file, "%d", &sMax);
        while((tmp = fgetc(file))==' ' || tmp >45){
            if(tmp == ' ')
                continue;
            aud.push_back(tmp-48);
        }
        for(int i=0;i<aud.size();i++){
            while(total < i)
                total++, cnt++;
            total += aud[i];
        }
        fprintf(fout, "Case #%d: %d\n", z, cnt);
        aud.resize(0);
    }

    fclose(file);
    fclose(fout);
    return 0;
}
