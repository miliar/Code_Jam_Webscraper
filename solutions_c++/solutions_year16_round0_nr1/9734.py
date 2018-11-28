#include <iostream>

void reverse(char str[], int length){
    int start = 0;
    int end = length -1;
    while (start < end){
        std::swap(*(str+start), *(str+end));
        start++;
        end--;
    }
}

// No negatives in input domain + always in base 10
char* itoa(int num, char* str){
    int i = 0;
 
    if (num == 0){
        str[i++] = '0';
        str[i] = '\0';
        return str;
    }
    
    while (num != 0){
        int rem = num % 10;
        str[i++] = (rem > 9)? (rem-10) + 'a' : rem + '0';
        num = num/10;
    }
 
    str[i] = '\0';
 
    reverse(str, i);
    return str;
}

struct Digits_Seen{
    bool zero;
    bool one;
    bool two;
    bool three;
    bool four;
    bool five;
    bool six;
    bool seven;
    bool eight;
    bool nine;
};

void initialize(struct Digits_Seen* d){
    d->zero = false;
    d->one = false;
    d->two = false;
    d->three = false;
    d->four = false;
    d->five = false;
    d->six = false;
    d->seven = false;
    d->eight = false;
    d->nine = false;
}
void update(struct Digits_Seen* d, char n){
    if(n == '0') d->zero = true;
    else if(n == '1') d->one = true;
    else if(n == '2') d->two = true;
    else if(n == '3') d->three = true;
    else if(n == '4') d->four = true;
    else if(n == '5') d->five = true;
    else if(n == '6') d->six = true;
    else if(n == '7') d->seven = true;
    else if(n == '8') d->eight = true;
    else if(n == '9') d->nine = true;
    else if(n == '-');
    else std::cerr << "NOT A DIGIT" << std::endl;
}
bool check(struct Digits_Seen* d){
    if(d->zero == true && d->one == true && d->two == true && d->three == true
    && d->four == true && d->five == true && d->six == true && d->seven == true
    && d->eight == true && d->nine == true) return true;
    else return false;
}

void try_to_sleep(int n){
    bool finished = false;
    char buffer[(sizeof(int) * 8) + 1];
    Digits_Seen* d = new Digits_Seen;
    initialize(d);
    int i = 1, j = 0;
    // special case for 0
    if(n == 0){
        std::cout << "INSOMNIA" << std::endl;
    }
    else{
        while(!finished){
            itoa(i * n, buffer);
            while(buffer[j] != '\0'){
                update(d, buffer[j]);
                j++;
            }
            j = 0;
            if(check(d)){
                std::cout << i * n << std::endl;
                finished = true;
            }
            i++;
        }
    }
    delete d;
}

int main(){
    int t, n;
    std::cin >> t;
    for(int i = 0; i < t; i++){
        std::cin >> n;
        std::cout << "Case #" << i + 1 << ": ";
        try_to_sleep(n);
    }
    return 0;
}