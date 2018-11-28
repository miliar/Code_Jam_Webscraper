#include <iostream>
#include <string>
using namespace std;

int main() {

    unsigned short elementCount;
    cin >> elementCount;


    string elements[elementCount];
    unsigned short start, end, current, temp;
    short direction;
    char pass;
    unsigned int flipCount;

    for (int i = 0; i < elementCount; ++i) {
        cin >> elements[i];
    }


    for (int i = 0; i < elementCount; ++i) {
        //for each line of input
        current = end = elements[i].length() -1; // we start searching from end;

        direction = -1;                     // and go backwards
        start = 0;
        flipCount = 0;
        pass = '+';

        while(true){
            if(elements[i].at(current) == pass){
                if(direction > 0)
                    start = current;
                else
                    end = current;
                    current = current + direction;
            } else {
                if(direction > 0) {
                    if(elements[i].at(end) != elements[i].at(current)) {
                        //this means after flip, the latest element is still -, so we need to flip it first
                        //while flipping it, we should flip all of the consequtive ones,
                        temp = end;
                        while(elements[i].at(temp) != elements[i].at(current)){
                            elements[i].at(temp) = elements[i].at(current);
                            temp--;
                        }
                        flipCount++;
                    }
                    start = current;
                    current = end;
                } else {
                    if(elements[i].at(start) != elements[i].at(current)) {
                        //this means after flip, the latest element is still -, so we need to flip it first
                        temp = start;
                        while(elements[i].at(temp) != elements[i].at(current)){
                            elements[i].at(temp) = elements[i].at(current);
                            temp++;
                        }
                        flipCount++;
                    }
                    end = current;
                    current = start;
                }

                if(pass == '+')
                    pass = '-';
                else
                    pass = '+';


                direction = direction * -1;

                flipCount++;
            }
            if(end == start)
                break;
        }
        cout << "Case #" << i+1 << ": " << flipCount << endl;
    }

    return 0;
}