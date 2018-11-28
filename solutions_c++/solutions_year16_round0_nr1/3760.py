//
//  main.cpp
//  codejam
//
//  Created by 张思浩 on 4/4/16.
//  Copyright © 2016 张思浩. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    int t;
    cin >> t;
    for(int i=0;i<t;++i){
        int n;
        cin >> n;
        if(n==0){
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
            continue;
        }
        int num=n;
        bool digits[10]={false};
        int count = 0;
        while(count<10){
            int temp = num;
            while(temp>0){
                if(!digits[temp%10]){
                    digits[temp%10]=true;
                    count++;
                    if(count==10)break;
                }
                temp=temp/10;
            }
            num+=n;
        }
        cout << "Case #" << i+1 << ": " << num-n << endl;
    }
    return 0;
}
