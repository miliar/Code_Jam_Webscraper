//
//  main.cpp
//  codejam
//
//  Created by 원재 정 on 2016. 4. 9..
//  Copyright © 2016년 Anthony Jung. All rights reserved.
//

#include <fstream>

bool check_done(int flag) {
    return ((flag ^ 0x03FF) == 0);
}

int check_digits(int num) {
    int flag = 0;
    while (num > 0) {
        flag |= 0x01 << (num % 10);
        num /= 10;
    }
    return flag;
}

int count_sheep(int n) {
    if (n == 0) return -1;
    int flag = 0, i = 1;
    int number;
    
    do {
        number = i++ * n;
        flag |= check_digits(number);
    } while(!check_done(flag));
    
    return number;
}

int main(int argc, const char * argv[]) {
    int t;
    std::ifstream fin("A-large.in");
    std::ofstream fout("A-large.out");
    fin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        fin >> n;
        auto result = count_sheep(n);
        fout << "Case #" << i + 1 << ": ";
        if (result < 0)
            fout << "INSOMNIA" << std::endl;
        else
            fout << result << std::endl;
    }
    fin.close();
    fout.close();
    
    return 0;
}
