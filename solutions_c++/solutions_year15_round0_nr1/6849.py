/* 
 * File:   main.cpp
 * Author: YuhaoZhu
 *
 * Created on April 10, 2015, 5:01 PM
 */

#include <cstdlib>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int index=1;
    int n;
    cin>>n;
    while (n--){
        int result=0;
        int standed=0;
        int size;
        cin>>size;
        string aud;
        cin>>aud;
        int audience[size];
        for (int i=0;i<aud.length();i++){
            audience[i]=(int)(aud[i]-'0');
        }
        for (int i=0;i<=size;i++){
            if (standed>=i){
                standed+=audience[i];
            }else{
                result+=i-standed;
                standed=i+audience[i];
            }
        }
        cout<<"Case #"<<index++<<": "<<result<<endl;
    }
    return 0;
}

