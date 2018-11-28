#include <iostream>
#include <stdint.h>

using namespace std;

int flags[10];

int getnodigits(int64_t n) {
    unsigned int number_of_digits = 0;
    do {
        ++number_of_digits;
    n /= 10;
    }
    while (n);

    return number_of_digits;
}

void init_flags() {
    int i;
    for (i = 0; i < 10 ; i++)
        flags[i] = 0;
}

void set_flag(int x) {
    flags[x] = 1;
}

int check_status() {
    int local_flag = 0, i=0;

    for (i = 0; i<10; i++)
        if(flags[i] == 1)
            local_flag++;

    if(local_flag < 10)
        return 0;
    else
        return 1;
}

int main() {
    init_flags();
    int number_of_cases = 0;
    int current_iteration = 0;
    int64_t array[200];

    cin>>number_of_cases;

    for (int i= 0 ; i< number_of_cases;i++)
        cin >> array[i];

    while(current_iteration< number_of_cases) {
        init_flags();
        int64_t arrayitem = array[current_iteration];
        int count = 1;

        if(arrayitem == 0) {
            cout << "CASE #" << current_iteration + 1 << ": " << "INSOMNIA" << endl;
            current_iteration++;
            continue;
        }

        while(check_status() == 0) {
            int64_t actualnumber = arrayitem * count;
            int numberofdigits = getnodigits(actualnumber);
            int64_t actualnumbercopy = actualnumber;

            while (numberofdigits > 0) {
                set_flag(actualnumbercopy % 10);
                actualnumbercopy = actualnumbercopy / 10;
                numberofdigits--;
            }

            if (check_status() == 1) {
                cout<<"CASE #"<<current_iteration+1<<": "<<actualnumber<<endl;
                break;
            }
            count++;
        }
        current_iteration++;
    }
    return 0;
}
