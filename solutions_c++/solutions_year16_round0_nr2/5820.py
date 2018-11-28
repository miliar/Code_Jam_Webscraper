//
//  main.cpp
//  Revenge of the Pancakes
//
//  Created by Yunfei Lu on 4/9/16.
//  Copyright © 2016 googleCodeJam. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(int argc, const char * argv[]) {
    ifstream file("A-small-practice.in");
    int value = 0;
    string order;
    int sum = 0;
    if (file.fail() == false) {
        file >> value;
        for (int i = 0; i < value; i++) {
            file >> order;
            sum = 0;
            bool leftisPlus = false;
            if (order[0] == '+') {
                leftisPlus = true;
                if (order.size() == 1) {
                    cout <<"Case"<< " #"<< i + 1<<":"<<"\t"<< 0 << endl;
                    continue;
                }
            } else if (order[0] == '-') {
                leftisPlus = false;
                if (order.size() == 1) {
                    cout <<"Case"<< " #"<< i + 1<<":"<<"\t" << 1 << endl;
                    continue;
                }
            }
            for (int i = 1; i < order.size(); i++) {
                if (leftisPlus) {
                    if (order[i] =='+' ) {
                        continue;
                    } else if(order[i] == '-') {
                        while (order[i+1] == '-' ) {
                            i++;
                        }
                        sum += 2;
                    }
                } else if(leftisPlus == false) {
                    if (order[i] == '+') {
                        while (order[i+1] == '+') {
                            i++;
                        }
                        sum += 1;
                        leftisPlus = true;
                    } else if(order[i] == '-') {
                        if(i != order.size() - 1 )
                        continue;
                        else {
                            sum += 1;
                        }
                    }
                }
            }
            cout <<"Case"<< " #"<< i + 1<<":" << "\t" << sum << endl;
        }
    }
    
    return 0;
}
