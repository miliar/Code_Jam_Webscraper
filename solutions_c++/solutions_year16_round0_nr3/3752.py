#include <iostream>
#include <string>
#include <math.h>
#include <bitset> 

using namespace std;

main(){
    
    int TestCases;
    cin >> TestCases;
    
    for(int tc=1; tc<=TestCases; tc++){
        int bits;
        int coins;
        cin >> bits;
        cin >> coins;
        
        unsigned long permutations = pow(2,(bits-2));

        string str(bits,'1');
        
        cout << "Case #"<<tc<<":"<<endl;
        for (unsigned long i=0; i<permutations;i++){
            
            int baseDividers[9] = {0};
            
            string bitString = bitset<14>((i>>1) ^ i).to_string();
            //cout << " "<<bitString<<endl;
            str.replace(str.begin()+1,str.begin()+(bits-2)+1,bitString);
//cout<<"permutation "<<i<<" - "<<str<<endl;              
            for(int base=2;base<=10;base++){
                unsigned long long value = 0;
                int power = 0;
//cout<<"base= "<<base<<endl;            
                for (std::string::reverse_iterator rit=str.rbegin(); rit!=str.rend(); ++rit){
                if(*rit == '1'){
                        value += pow(base,power);
                    }
                power++;
                }
//cout<<"value= "<<value<<endl;
                for(int i =2;i<sqrt(value)+1;i++)
                {
                    if(!(value%i)){
                        baseDividers[base-2] = i;
                        break;
                    }
                }
//cout<<"divisor= "<<baseDividers[base-2]<<endl;
                if(baseDividers[base-2] == 0) break;
            }
            
            bool allDividersFound = true;
            for(int i=0;i<9;i++){
                if (baseDividers[i]==0) allDividersFound = false;
            }
            if(allDividersFound){
                cout<<str;
                for(int i=0;i<9;i++) cout<<" "<<baseDividers[i];
                if(--coins == 0)break;
                if(i!=permutations-1)cout<<endl;
            }
            else continue;
        }
    }
    
    return 0;
}