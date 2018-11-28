#include <iostream>
#include <string> 
#include <cstring>

using namespace std;

bool allSeen(bool* digits){
    for(int i =0; i<10; i++){
        //cout<<i<<": "<<"  "<<digits[i];
        if(digits[i]==false)return false;
    }
    return true;
}

main(){
    
    int TestCases;
    cin >> TestCases;
    
    for(int tc=1; tc<=TestCases; tc++){
        int input;
        cin >> input;
        
        if(input == 0){
            cout << "Case #"<<tc<<": INSOMNIA";
            if(tc!=TestCases)cout<<endl;
            continue;
        }
        
        bool digitsSeen[10] = {false};
        long unsigned currentNumber;
        long unsigned iteration = 0;
        
        do{
            iteration++;
            currentNumber = iteration * input;
            //cout<<" "<<currentNumber<<endl;
            std::string str = std::to_string(currentNumber);
            char * cstr = new char [str.length()+1];
            std::strcpy (cstr, str.c_str());
            
            for(int i=0;cstr[i]!=0;i++){
                digitsSeen[cstr[i]-48] = true;
            }
            
            delete[] cstr;
            
        }while(!allSeen(digitsSeen));
        
        cout << "Case #"<<tc<<": "<<currentNumber;
        if(tc!=TestCases)cout<<endl;
    }
    
    return 0;
}