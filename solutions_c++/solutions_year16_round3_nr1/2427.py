//
//  main.cpp
//  Senate Evacuation
//
//  Created by Jeremy Wong on 8/5/2016.
//  Copyright © 2016 Jeremy Wong. All rights reserved.
//

#include <iostream>
#include <vector>


using namespace std;

void updatePercentage(double *percent, int *num, int numOfParty, int total);
bool notContainMajority(double *percent, int numOfParty);
string convertToString(int ary[]);


int main(int argc, const char * argv[]) {
    
    
    int numOfInput;
    cin >> numOfInput;
    
    for (int i=0; i<numOfInput; i++){
        
        int numOfParty;
        cin >> numOfParty;
        
        int *num = new int[numOfParty];
        double *percent = new double[numOfParty];
        int total = 0;
        for (int j=0; j<numOfParty; j++){
            
            cin >> num[j];
            total += num[j];
            
        }
        //cout << "Total: " << total << endl;
        updatePercentage(percent, num, numOfParty, total);
        
        vector <string> vec;
        
        while (total != 0){
            
            int highest_index = 0;
            int highest_value = 0;
            for (int j=0; j<numOfParty; j++){
                if (num[j]>highest_value){
                    highest_value = num[j];
                    highest_index = j;
                }
            }
            
            
            bool done = false;
            
            
            if (num[highest_index]>1){
                num[highest_index] -= 2;
                updatePercentage(percent, num, numOfParty, total-2);
                if (notContainMajority(percent, numOfParty)){
                    
                    done = true;
                    int *ary = new int[2];
                    ary[0] = highest_index;
                    ary[1] = highest_index;
                    vec.push_back(convertToString(ary));
                    total -=2;
                }else{
                    num[highest_index] += 2;
                }
            }
            
            
            
            if (!done){
                
                int secondHighest_index = 0;
                highest_value = 0;
                for (int j=0; j<numOfParty; j++){
                    
                    if (j != highest_index){
                        
                        if (num[j] > highest_value){
                            highest_value = num[j];
                            secondHighest_index = j;
                        }
                    }
                }
                
                
                num[highest_index] -= 1;
                num[secondHighest_index] -= 1;
                updatePercentage(percent, num, numOfParty, total-2);
                if (notContainMajority(percent, numOfParty)){
                    
                    done = true;
                    int *ary = new int[2];
                    ary[0] = highest_index;
                    ary[1] = secondHighest_index;
                    vec.push_back(convertToString(ary));
                    total -=2;
                }else{
                    num[highest_index] += 1;
                    num[secondHighest_index] += 1;
                }
                
            }
            
            
            
            
            if (!done){
                
                num[highest_index] -=1 ;
                int *ary = new int[2];
                ary[0] = highest_index;
                ary[1] = -1;
                vec.push_back(convertToString(ary));
                total -=1;
                
                
            }
            
        }
        
        
        
        cout << "Case #" << i+1 << ": ";
        vector<string>::iterator iter;
        for (iter=vec.begin(); iter!=vec.end(); iter++){
            cout << (*iter) << " ";
        }
        cout << endl;
    }
    
    return 0;
}

void updatePercentage(double *percent, int *num, int numOfParty, int total){
    
    for (int i=0; i<numOfParty; i++){
        
        percent[i] = (double)num[i]/(double)total;
        //cout << percent[i] << " ";
    }
    //cout << endl;
}

bool notContainMajority(double *percent, int numOfParty){
    
    bool result = true;
    for (int i=0; i<numOfParty; i++){
        
        
        if (percent[i]>0.5){
            result = false;
            break;
        }
        
    }
    
    return result;
    
}


string convertToString(int ary[]){
    
    string str = "";
    
    for (int i=0; i<2; i++){
        
        switch (ary[i]){
                
            case 0:
                str += "A";
                break;
            case 1:
                str += "B";
                break;
            case 2:
                str += "C";
                break;
            case 3:
                str += "D";
                break;
            case 4:
                str += "E";
                break;
            case 5:
                str += "F";
                break;
            case 6:
                str += "G";
                break;
            case 7:
                str += "H";
                break;
            case 8:
                str += "I";
                break;
            case 9:
                str += "J";
                break;
            case 10:
                str += "K";
                break;
            case 11:
                str += "L";
                break;
            case 12:
                str += "M";
                break;
            case 13:
                str += "N";
                break;
            case 14:
                str += "O";
                break;
            case 15:
                str += "P";
                break;
            case 16:
                str += "Q";
                break;
            case 17:
                str += "R";
                break;
            case 18:
                str += "S";
                break;
            case 19:
                str += "T";
                break;
            case 20:
                str += "U";
                break;
            case 21:
                str += "V";
                break;
            case 22:
                str += "W";
                break;
            case 23:
                str += "X";
                break;
            case 24:
                str += "Y";
                break;
            case 25:
                str += "Z";
                break;
            default:
                break;
                
        }
        
    }
    
    
    
    return str;
}






