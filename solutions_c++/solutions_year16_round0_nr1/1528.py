#include <iostream>
#include <string>

using namespace std;

/* MACROS */
#define NOTFOUND_MSG     "INSOMNIA"

/* Function prototypes */
int countSheep(int begin);

int main(){

    int numOfTest = 0;
    int count = 0;
    string line;

    if(getline(cin, line)){
        numOfTest = stoi(line);
    }
    else{
        cout << "No testcase is specified.\n";
        return 1;
    }

    while(getline(cin, line)) {
        // cout << line << endl;

        int test = stoi(line);
        int result = countSheep(test);

        cout << "Case #" << ++count << ": ";
        if(result == -1)
            cout << NOTFOUND_MSG << endl;
        else
            cout << result << endl;
    }

    return 0;
}

int countSheep(int begin){
    int counter[10] = {0,};

    int current = begin;
    int temp = current;
    int notChanged = 1;
    int changed = 0;

    while(changed < 10 && notChanged < 100){
        do{
            int remainder = temp % 10;
            if(counter[remainder] == 0){
                counter[remainder]++;
                notChanged = 0;
                changed++;
            }
            temp /= 10;
        }while(temp);

        notChanged++;
        
        if(changed < 10){
            current += begin;
            temp = current;
        }
    }

    if(changed == 10)
        return current;
    else
        return -1;
}
