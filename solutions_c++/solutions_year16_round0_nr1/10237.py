#include <iostream>
#include <string>
#include <fstream>


int main() {
    
    std::ifstream inFile;
    std::ofstream outFile;
    inFile.open("A-large.in");
    outFile.open("A-large.out");
    int cases = 0;
    long N = 0;
    long count = 0;
    long product = 0;
    long *array;
    struct AllFound {
        bool one = false, two = false, three = false,
        four = false, five = false, six = false, seven = false,
        eight = false, nine = false, zero = false;
        
        bool allTrue() {
            if (one && two && three && four && five  && six
                 && seven  && eight && nine  && zero) {
                return true;
            } else {
                return false;
            }
        }
        void setFalse(){
            one = false;
            two = false;
            three = false;
            four = false;
            five = false;
            six = false;
            seven = false;
            eight = false;
            nine = false;
            zero = false;
        }
    };
    
    std::string hold;
    
    inFile >> cases;
    std::string::size_type found;
    array = new long[cases];
    AllFound search;
    
    for (int i = 0; i < cases; i++) {
        count = 1;
        product = 0;
        inFile >> N;
        while (!search.allTrue()) {
            product = N * count;
            hold = std::to_string(product);
            if (N == 0) {
                array[i] = 0;
                break;
            }
            found = hold.find("1");
            if (found != std::string::npos) {
                search.one = true;
            }
            found = hold.find("2");
            if (found!= std::string::npos) {
                search.two = true;
            }
            found = hold.find("3");
            if (found != std::string::npos) {
                search.three = true;
            }
            found = hold.find("4");
            if (found != std::string::npos) {
                search.four = true;
            }
            found = hold.find("5");
            if (found != std::string::npos) {
                search.five = true;
            }
            found = hold.find("6");
            if (found != std::string::npos) {
                search.six = true;
            }
            found = hold.find("7");
            if (found != std::string::npos) {
                search.seven = true;
            }
            found = hold.find("8");
            if (found != std::string::npos) {
                search.eight = true;
            }
            found = hold.find("9");
            if (found != std::string::npos) {
                search.nine = true;
            }
            found = hold.find("0");
            if (found != std::string::npos) {
                search.zero = true;
            }
            count++;
        }
        search.setFalse();
        array[i] = product;
    }
    
    for (int i = 0; i < cases; i++) {
        if (array[i] == 0) {
            outFile << "Case #" << i+1 << ": INSOMNIA" << std::endl;
        } else {
            outFile << "Case #" << i+1 << ": " << array[i] << std::endl;
        }
    }
    return 0;
}