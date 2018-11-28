#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector <int> digits(10);

void genDigits(int number){

    string numb = to_string(number);

    for(unsigned int i=0;i<numb.length();i++){
        switch ( numb[i] ){
            case '0':
                digits[0]=1;
                break;
            case '1':
                digits[1]=1;
                break;
            case '2':
                digits[2]=1;
                break;
            case '3':
                digits[3]=1;
                break;
            case '4':
                digits[4]=1;
                break;
            case '5':
                digits[5]=1;
                break;
            case '6':
                digits[6]=1;
                break;
            case '7':
                digits[7]=1;
                break;
            case '8':
                digits[8]=1;
                break;
            case '9':
                digits[9]=1;
                break;
        }
    }
}

int genCases(int number){
    bool countAuxx=false;
    int N=1;

    while(!countAuxx){
        if(number*N){
            int countAux=0;

            genDigits(number*N);

            for(unsigned int i=0;i<digits.size();i++){
                if(digits[i]==1){
                    countAux++;
                }
            }
            if(countAux==10){
                countAuxx=true;
            }
            N++;
        }else{
            countAuxx=true;
        }
    }

    return number*(N-1);
}

int main(){

    int T;
    int N;

    cin >> T;

    for(int i=0;i<T;i++){
        cin >> N;
        fill(digits.begin(), digits.end(), 0);
        int modes = genCases(N);

        if(modes){
            cout << "Case #" << i+1 << ": " << modes <<endl;
        }else{
            cout << "Case #" << i+1 << ": " << "INSOMNIA" <<endl;
        }
    }

    return 0;
}
