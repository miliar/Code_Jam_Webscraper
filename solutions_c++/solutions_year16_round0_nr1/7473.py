//
//  main.cpp
//  Counting_Sheep
//
//  Created by 이재현 on 2016. 4. 9..
//  Copyright © 2016년 haru. All rights reserved.
//

#include <iostream>
#include <unistd.h>

using namespace std;

int main(int argc, const char * argv[]) {
    int N;
    cin >> N;
    for(int i=1;i<=N;i++) {
        long long num;
        int check[10];
        cin >> num;
        if(num==0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
        else {
            for(int j=0;j<10;j++) {
                check[j]=0;
            }
            for(int j=1;;j++) {
                long long tempNum = num*j;
//                cout << "tempNum: " << tempNum << endl;
//                usleep(500000);
                while(tempNum!=0) {
                    check[tempNum%10] = 1;
                    tempNum/=10;
                }
                int count;
                for(count=0;count<10;count++) {
//                    cout << count << ": " << check[count] << endl;
                    if(check[count]==0) break;
                }
                if(count==10) {
                    cout << "Case #" << i << ": " << num*j << endl;
                    break;
                }
            }
        }
    }
}
