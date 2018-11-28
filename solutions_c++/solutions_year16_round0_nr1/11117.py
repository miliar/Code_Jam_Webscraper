//
//  main.cpp
//  Counting Sheep
//
//  Created by ZHENGLEI on 4/8/16.
//  Copyright © 2016 86. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int static c;
class countingSheep{
private:
    bool* a = new bool[10];
    int orig, lastNum;
public:
    countingSheep():orig(0), lastNum(0){
        for(int i=0;i<10;i++)
            a[i] = false;
    }
    countingSheep(int orig):orig(orig), lastNum(0){
        for(int i=0;i<10;i++)
            a[i] = false;
    }
    bool isAsleep(){
        for(int i = 0; i<10; i++){
            if(a[i] == false)
                return false;
        }
        return true;
    }
    void updateDigit(int num){
        while(num != 0){
            a[num%10] = true;
            num = num/10;
        }
    }
    void counting(int N){
        reset(N);
        int temp = orig;
        lastNum = temp;
        c++;
        if(orig == 0){
            cout << "Case #" << c << ": INSOMNIA" << '\n';
            return;
        }
        else{
            while(!isAsleep()){
            updateDigit(temp);
            lastNum = temp;
            temp = temp + orig;
            }
            cout << "Case #" << c << ": " << lastNum << '\n';

        }
    }
    int getlastNum(){
        return lastNum;
    }
    bool isOrigZero(){
        if(orig == 0)
            return true;
        return false;
    }
    void reset(int N){
        orig = N;
        for(int i=0;i<10;i++)
            a[i] = false;
    }
};
int main() {
    int n,N;
    countingSheep a;
    ifstream f("A-large.in");
    ofstream out;
    out.open("myOutput2.txt");
    f >> n;
    for(int i=0;i<n;i++){
        f >> N;
        a.counting(N);
        if(a.isOrigZero()){
            out << "Case #" << c << ": INSOMNIA" << '\n';
        }else
        out << "Case #" << c << ": " << a.getlastNum() << '\n';
    }
    f.close();
    out.close();
    return 0;
}
