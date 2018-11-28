#include<fstream>
#include<iostream>
using namespace std;

int main(){
    FILE * f;
    FILE * out;
    f = fopen("large.txt", "r");
    out = fopen("large_out.txt", "w");

    int t;
    fscanf(f, "%i", &t);
    for(int i = 0; i < t; i++){
        int high;
        int temp;
        fscanf(f, "%i", &high);
        fscanf(f, "%c", &temp);
        int people = 0;
        int friends = 0;

        for(int j = 0; j <= high; j++){

            fscanf(f, "%c", &temp);
            temp -= 48;
            if(people + friends < j){
                friends += j- (people + friends);
            }
            people += temp;
        }
        cout << endl;
        fscanf(f, "%c", &high );
        fprintf(out, "Case #%i: %i\n", i + 1, friends);

    }

    fclose(f); fclose(out);

}
