//
//  main.cpp
//  codejam2
//
//  Created by Raphael Sampaio on 4/9/16.
//  Copyright © 2016 Raphael Sampaio. All rights reserved.
//

#include <iostream>
#include <string>

int pancakes(std::string str) {
    int size = (int)str.size();
    int j = str[size-1] == '+' ? 0 : 1;
    for (int i = 1; i < size; i++) {
        if (str[i-1] != str[i]) {
            j++;
        }
    }
    return j;
}

int main(int argc, const char * argv[]) {
    int max;
    std::string str;
    std::cin >> max;
    for(int i = 0; i < max; ++i)
    {
        std::cin >> str;
        printf("Case #%d: ", i + 1);
        printf("%d\n", pancakes(str));
    }
    return 0;
}