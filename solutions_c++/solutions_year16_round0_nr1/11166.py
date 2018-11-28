#include <iostream>
#include <fstream>
using namespace std;
bool check(int digits[]){
    for(int i=0;i<10;i++){
        if (digits[i] != 11){
            return false;
        }
    }
    return true;
}

int getRid(int digits[], int digit){
    for(int i=0;i<10;i++){
        if(digits[i] == digit){
            digits[i] = 11;
        }
    }
}

int strip(int digits[], int number){
    int temp = number;
    int temp2 = 0;
    int temp3 = 0;
    while(temp != 0){
        temp2 = temp/10;
        temp3 = (temp-(temp2*10));
        getRid(digits, temp3);
        temp /= 10;
    }
}

int testNumber(int getal){
    bool done = false;
    int digits[10] = {0,1,2,3,4,5,6,7,8,9};
    int multiplier = 1;
    while(!done){
        strip(digits, getal*multiplier);
        if(check(digits) == true){
            return getal*multiplier;
        }
        multiplier ++;
        if(multiplier > 200){
            return 0;
            break;
        }
    }
}


int main(){
    int Tests = 10;
    int uitkomst = 0;
    int getallen[3] = {0,1,2};
    int hulpGetal = 0;
    int Teller = 1;
    char kar = 'a';
    ifstream invoer;
    ofstream uitvoer;
    invoer.open("countingSheep.txt");
    uitvoer.open("countingSheepOutput.txt");
    while(!invoer.eof()){
        while(kar != '\n'){
            kar = invoer.get();
            if(kar != '\n'){
                hulpGetal = hulpGetal*10 + (kar - '0');
            }
        }
        int uitkomst = testNumber(hulpGetal);
        if(uitkomst == 0){
            uitvoer << "Case #" << Teller << ": INSOMNIA";
        }
        else
            uitvoer << "Case #" << Teller << ": " << uitkomst;
        uitvoer << endl;
        Teller ++;
        hulpGetal = 0;
        kar = 'a';
        if(Teller == 101)
            break;
    }
    return 0;
}
