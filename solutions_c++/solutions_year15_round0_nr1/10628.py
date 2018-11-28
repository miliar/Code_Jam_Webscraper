#include <iostream>

int main(){
    
    int test_cases;
    
    std::cin >> test_cases;
    
    for(int i = 1; i <= test_cases; i++){
        
        int audience;
        int total = 0;
        int anwser = 0;
        char p;
        
        std::cin >> audience;
        
        for(int person = 0; person < audience; person++){
        
            std::cin >> p;
            
            if(p == '0' && person == 0){
            
                anwser++;
                //total++;
            }
            else{
                    if(total + anwser < person){
            
                    anwser+=person-total-anwser;
                    
                    }
                    
                    total += (p - '0');
                    //total += anwser;
                    //std::cout << "TOTAL: " << total<<std::endl<<"ANWSER: "<<anwser<<std::endl<<std::endl;
            }
        }
        
        if(total + anwser < audience+1 && audience != 0){
        
            anwser+=audience-total - anwser;
        }
        
        std::cin >> p;
        
        std::cout << "Case #" << i <<": " << anwser;
        if(i != test_cases) std::cout << std::endl;
    }
 
    return 0;
}
