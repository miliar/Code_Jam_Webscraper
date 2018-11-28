#include <iostream>
#include <string>

using namespace std;

bool isAllHappy(string input);
string filp(string input, int index);
int main(){
    
    int k;
    cin >> k;
    for (int i=0; i<k; i++){
        
        string input;
        cin >> input;
        
        
        int count = 0;
        while (!isAllHappy(input)) {
            
            int filpIndex = -1;
            if (input.length() != 1){
                
                
                for (int j=0; j<input.length(); j++){
                    
                    if (j+1 == input.length()){
                        
                        if (input.at(0) == '-'){
                            input = filp(input, input.length());
                        }
                        
                    }else{
                        
                        if (input.at(j) != input.at(j+1)){
                            filpIndex = j+1;
                        }
                    }
                    
                    if (filpIndex != -1){
                        input = filp(input, filpIndex);
                        break;
                    }
                    
                }
                
            }else{
                count = 1;
                break;
            }
            
            
            
            count++;
        }
        
        
        cout << "Case #" << i+1 << ": " << count << endl;
    }
    
    
    
    return 0;
}

bool isAllHappy(string input){
    
    bool happy = true;
    for (int i=0; i<input.length(); i++){
        
        if (input.at(i) == '-'){
            happy = false;
            break;
        }
    }
    return happy;
}

string filp(string input, int index){
    
    bool isHappy = false;
    if (input.at(0) == '+'){
        isHappy = true;
    }else{
        isHappy = false;
    }
    
    string instanceString = "";
    for (int i=0; i<index; i++){
        
        if (isHappy) instanceString = instanceString + "-";
        else instanceString = instanceString + "+";
    }
    
    instanceString = instanceString + input.substr(index, input.length());
    return instanceString;
    
}


