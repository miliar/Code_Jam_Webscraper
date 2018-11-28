#include <iostream>
#include <stdio.h>
using namespace std;


int ovation(int caseNo){
    int maxshyness;
    cin >> maxshyness;
    int friends = 0;
    int clapping = 0;
    char num;
    cin.get();

    for (int shyness = 0; shyness <= maxshyness; shyness++){
        num = cin.get() - '0';
        if ( clapping + friends >= shyness){
            clapping += num;
        } else {
            friends++;
            clapping += num;
        }
    }
    cin.get();
    printf("Case #%d: %d\n", caseNo, friends);
}

int main(int argc, char* argv[]){
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++){
        ovation(i);
    }
}
