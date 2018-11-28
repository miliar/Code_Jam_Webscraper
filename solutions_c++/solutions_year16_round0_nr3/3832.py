//
//  main.cpp
//  Coin Jam
//
//  Created by dengjc on 16/4/9.
//  Copyright © 2016年 dengjc. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <bitset>
#include <vector>

using namespace std;

long long toInt(string s,int base);
bool isPrime(long long num);

int main(int argc, const char * argv[]) {
    ofstream ofs;
    ifstream ifs;
    ofs.open("/Users/dengjc/Desktop/C-small");
    ifs.open("/Users/dengjc/Desktop/C-small-attempt0.in");
    if (!ofs.is_open()||!ifs.is_open()) {
        cout<<"打开文件出错"<<endl;
        return 1;
    }
    
    int T;
    ifs>>T;
    
    for (int i=1; i<=T; i++) {
        int N,J;
        ifs>>N>>J;
        string jamStr = "1000000000000001";
        
        bitset<16> bset(jamStr);
        
        unsigned long minJam = bset.to_ulong();
        int cnt = 0;
        
        ofs<<"Case #"<<i<<":"<<endl;
        
        while (cnt!=J) {
            vector<long long> vec;
            string result = "";
            bool isJamCoin = true;
            for (int base = 2; base<=10; base++) {
                long long baseNum = toInt(jamStr, base);
                //cout<<"baseNum = "<<baseNum<<endl;
                vec.push_back(baseNum);
                if(isPrime(baseNum))
                {
                    isJamCoin = false;
                    vec.clear();
                    break;
                }
            }
            
            if (isJamCoin) {
                cnt++;
//                cout<<jamStr<<endl;
                result = result + jamStr + " ";
                for(long long num:vec)
                {
                    for (int j=2; j<num; j++) {
                        if (num%j==0) {
                            result = result + to_string(j) + " ";
                            break;
                        }
                    }
                }
                ofs<<result<<endl;
            }
            minJam += 2;
            bitset<16> bset(minJam);
            jamStr = bset.to_string();
        }
        
//        ofs<<"Case #"<<i<<": "<<result<<endl;
    }
    return 0;
}

long long toInt(string s,int base)
{
    long long res = 0;
    size_t len = s.length();
    for (int i=0; i<len; i++) {
        res += (s[i] - '0')*pow(base, len-i-1);
    }
    return res;
}


bool isPrime(long long n)
{
    if(n<2)
        return false;
    if(n==2)
        return true;
    for(int i=3;i<sqrt(n);i+=2)
        if(n%i==0)
            return false;
    return true;
}