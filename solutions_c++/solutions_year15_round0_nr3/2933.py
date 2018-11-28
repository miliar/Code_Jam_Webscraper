#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


pair<char, bool> getResult(pair<char, bool> p1, pair<char, bool> p2){
     
     char answer;
     bool negative = p1.second != p2.second;
     char char1 = p1.first;
     char char2 = p2.first;
           
     if(char1 == '1'){
              answer = char2;         
     }else if(char2=='1'){
            answer = char1;      
     }else if(char1 == char2){
           answer = '1';     
           negative = true != negative;   
     }else if(char1 == 'i'){
           if(char2 == 'j'){
                 answer='k';      
           }else{
                     answer='j';
                     negative = true != negative;                        
           }      
     }else if(char1 == 'j'){
           if(char2 == 'i'){
               answer='k';      
               negative = true != negative;  
           }else{
                 answer='i';      
           }      
     }else if(char1 == 'k'){
           if(char2 == 'i'){
                    answer='j';         
           }else{
                 answer = 'i';   
                 negative = true != negative;     
           }      
     }          
     
     return pair<char, bool>(answer, negative);           
}

int main(){
    
    ifstream in("C.in");
    ofstream out("C.out");
        
        
    int cases;
    in>>cases;
    
    for(int i=0;i<cases;i++){
            int len, repeat;
            in >> len >> repeat;
            string s, str;
            
            in >> s;
            
            while(repeat > 0){
                str+= s;
                repeat--;       
            }
            
            bool found = false;
            
            pair<char, bool> current(str[0], false);
            
            char lookingFor = 'i';
            
            vector<string> v;
            int li =0;
            
            for(int j=1;j<str.length();j++){
                    
                    if(current.first == lookingFor && current.second == false){
                                     v.push_back(str.substr(li, j-li));
                                     li = j;
                                     if(lookingFor == 'i') lookingFor = 'j';    
                                     else if(lookingFor == 'j') lookingFor = 'y';                                 
                       current = make_pair(str[j], false);            
                    }else{
                          current = getResult(current, make_pair(str[j], false));
                          
                    }
                           
            }
            
            //current = getResult(current, make_pair(str[str.length()-1], false));
            
            
            if(lookingFor =='y' && current.second == false && current.first == 'k'){
                             found = true;
                             v.push_back(str.substr(li, str.length()-li));
                             //out << current.first << "  " << li <<"  " << str.length() <<  "\n";
            }
            
            string f = "NO";
            if(found == true) f = "YES";
            
            
            out << "Case #" << (i+1) << ": " << f <<"\n";
            
            
            for(int j=0;j<v.size();j++){
                    //out << v[j] << "\n";        
            }                
    }
    
    
    
    
    
}
