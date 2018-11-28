#include <iostream>
#include <cstring>
using namespace std;



int main() {
    unsigned short elementCount;
    unsigned int currentNumber;
    unsigned int currentDigit;
    unsigned int currentFactor = 0;

    bool searching = true;
    cin >> elementCount;

    unsigned int elements[elementCount][11];
    std::memset(elements, 0, elementCount*11*sizeof(unsigned int));
    for (int i = 0; i < elementCount; ++i) {
        cin >> elements[i][0];
    }
    for (int i = 0; i < elementCount; ++i) {
        searching=true;
        currentFactor=0;
        if(elements[i][0] == 0) {
            std::cout << "Case #" << i+1 <<": " "INSOMNIA" << std::endl;
        } else {
            while(searching) {
                currentFactor++;
                currentNumber = elements[i][0] * currentFactor;
                //mark digits
                while(true){
                    currentDigit = currentNumber % 10;
                    elements[i][currentDigit+1] = 1;
                    currentNumber = currentNumber / 10;
                    if(currentNumber == 0){
                        break;
                    }
                }
                for (int j = 1; j < 11; ++j) {
                    searching = false;
                    if(elements[i][j] == 0) {
                        searching = true;
                        break;
                    }
                }
            }
            std::cout << "Case #" << i+1 <<": " << elements[i][0] * currentFactor << std::endl;
        }
    }
    return 0;
}