//
//  main.cpp
//  ASmall

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin;
ofstream fout;


void process(string s) {
    
    int sizeSpecial = 10;
    int sizeFirst = 5;
    int digits[10] = {0, 2, 4, 6, 8, 3, 7, 5, 1, 9};
    char special[10] = {'Z','W', 'U', 'X', 'G', 'H', 'S', 'F', 'O', 'I'};
    int count[10] = {0};
    vector<int> numbers;
    
  //  count[9] - count[4] - count[3] - count[7]
    

    for (int i = 0; i < s.length(); i++) {
        
        for (int j = 0; j < sizeSpecial; j++) {
            
            if (s[i] == special[j]) {
            
                count[j]++;
                break;
            }
        }
    }
    
    
    for (int i = 0; i < sizeFirst; i++) {
    
        for (int j = 0; j < count[i]; j++) {
        
            numbers.push_back(digits[i]);
        }
    }
    
    // THREE
    
    // 3 - 8
    
    for (int i = 0; i < count[5] - count[4]; i++) {
        
        
        numbers.push_back(digits[5]);
    }
    
   // 7 - 6
    
    // SEVEN
    for (int i = 0; i < count[6] - count[3]; i++) {
    
    
        numbers.push_back(digits[6]);
    }
    
    // 5 - 4
    
    //FIVE
    
    for (int i = 0; i < count[7] - count[2]; i++) {
    
        numbers.push_back(digits[7]);
    }

    //ONE
    
    // 1 - 0 - 2 - 4
    
    for (int i = 0; i < count[8] - count[0] - count[1] - count[2]; i++) {
    
        numbers.push_back(digits[8]);
    }
    
    // NINE
    
    // 9 - 8 - 6 - 5
    
    for (int i = 0; i < count[9] - count[4] - count[3] - (count[7] - count[2]) ; i++) {
    
        numbers.push_back(digits[9]);
    }
    
    sort(numbers.begin(), numbers.end());
    
    for (int i = 0; i < numbers.size(); i++) {
    
        fout<<numbers[i];
    }
    
    
}




int main(int argc, const char * argv[]) {
    
    int nr_cases;
    
    fin.open("in.txt");
    fout.open("out.txt");
    
    if (fin.is_open()) {
        
        fin >> nr_cases;
        string s;
        getline(fin, s);
        
        for (int i = 1; i <= nr_cases; i++) {
        
            fout <<"Case #"<<i<<": ";
            getline(fin, s);
            process(s);
            fout <<endl;
        }
        
        
    } else {
    
        cout <<"Fisierul este NULL"<<endl;
    }
    
    fin.close();
    fout.close();
    
    cout <<"DONE"<<endl;
    
    return 0;
}
