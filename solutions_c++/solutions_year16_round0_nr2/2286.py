//
//  main.cpp
//  code-jam-2
//
//  Created by Ryan on 4/9/16.
//  Copyright © 2016 Ryan. All rights reserved.
//

#include <iostream>
#include <string>



using namespace std;


void convert(string str, int* arr){
    for(int i=0; i<str.length(); i++){
        if(str[i]=='+') arr[i] = 1;
        else if(str[i]=='-') arr[i] = 0;
    }
}

int num(int* arr, size_t length){
    int retval = 0;
    int last = -1;
    int cur;
    for(int i=0; i<length; i++){
        cur = arr[i];
        if(cur==0&&last==-1) retval++;
        else if(cur==0&&last==1) retval+=2;
        last = arr[i];
    }
    return retval;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    cin >> T;
    string str;
    int ans;
    for(int i=0; i<T; i++){
        cin >> str;
        int arr[str.length()];
        convert(str, arr);
        ans = num(arr, str.length());
        printf("Case #%d: %d\n", i+1, ans);
    }
    return 0;
}
