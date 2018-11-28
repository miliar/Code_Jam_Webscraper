//
//  main.cpp
//  Getting the Digits
//
//  Created by Hong Eunpyeong on 2016. 5. 1..
//  Copyright © 2016년  Hong Eunpyeong. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    int tc;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin >> tc;
    for(int i = 0; i < tc; i++){
        string s;
        fin >> s;
        
        int ch[30] = {0, };
        int res[10] = {0, };
        int stack[] = {6, 7, 8, 4, 5, 9, 0, 2, 3, 1};
        
        for(int j = 0; j < s.size(); j++){
            ch[s[j]-'A']++;
        }
        
        for(int j = 0; j < 10; j++){
            switch(stack[j]){
                case 7:
                    while(ch[4]>1 && ch[18]>0 && ch[21]>0 && ch[13]>0){
                        ch[4]--;
                        ch[4]--;
                        ch[18]--;
                        ch[21]--;
                        ch[13]--;
                        res[7]++;
                    }
                    break;
                case 8:
                    while(ch[4]>0 && ch[8]>0 && ch[6]>0 && ch[7]>0 &&ch[19]>0){
                        ch[4]--;
                        ch[8]--;
                        ch[6]--;
                        ch[7]--;
                        ch[19]--;
                        res[8]++;
                    }
                    break;
                case 0:
                    while(ch[25]>0 && ch[4]>0 && ch[17]>0 && ch[14]>0){
                        ch[25]--;
                        ch[4]--;
                        ch[17]--;
                        ch[14]--;
                        res[0]++;
                    }
                    break;
                
                case 2:
                    while(ch[19]>0 && ch[22]>0 && ch[14]>0){
                        ch[19]--;
                        ch[22]--;
                        ch[14]--;
                        res[2]++;
                    }
                    break;
                case 3:
                    while(ch[19]>0 && ch[7]>0 && ch[17]>0 && ch[4] > 1){
                        ch[19]--;
                        ch[7]--;
                        ch[17]--;
                        ch[4]--;
                        ch[4]--;
                        res[3]++;
                    }
                    break;
                case 4:
                    while(ch[5]>0 && ch[14]>0 && ch[20]>0 && ch[17]>0){
                        ch[5]--;
                        ch[14]--;
                        ch[20]--;
                        ch[17]--;
                        res[4]++;
                    }
                    break;
                case 5:
                    while(ch[5]>0 && ch[8]>0 && ch[21]>0 && ch[4]>0){
                        ch[5]--;
                        ch[8]--;
                        ch[21]--;
                        ch[4]--;
                        res[5]++;
                    }
                    break;
                case 6:
                    while(ch[18]>0 && ch[8]>0 && ch[23]>0){
                        ch[18]--;
                        ch[8]--;
                        ch[23]--;
                        res[6]++;
                    }
                    break;
                
               
                
                case 1:
                    while(ch[14]>0 && ch[13]>0 && ch[4]>0){
                        ch[14]--;
                        ch[13]--;
                        ch[4]--;
                        res[1]++;
                    }
                    break;
                case 9:
                    while(ch[13]>1 && ch[8]>0 && ch[4]>0){
                        ch[13]--;
                        ch[13]--;
                        ch[8]--;
                        ch[4]--;
                        res[9]++;
                    }
                    break;
            }
        }
        
        fout << "Case #" << i+1 << ": ";
        for(int j = 0; j < 10; j++){
            while(res[j] > 0){
                fout << j;
                res[j]--;
            }
        }
        fout << endl;
    }
    return 0;
}
