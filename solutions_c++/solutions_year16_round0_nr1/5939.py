#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <set>
#include<math.h>

int main(int argc, const char * argv[])    {
    
    //std::ifstream file("A-small-practice.in-2.txt");
    
    std::ifstream file("sample.txt");
    std::ofstream oFile;
    oFile.open ("Task1_answer_Large.txt");
    
    std::set<int> Num;
    int N=0;
    
    std::string str;
    long val =0;
    
    
    std::getline(file,str);
    int T = std::stoi(str);
    
    if(T>100 && T<1)
        return 0;
    
    
    for(int i=1;i<=T;i++){
        std::getline(file,str);
        N = std::stoi(str);
        
        if(N<0)
            return 0;
        
        if(N==0){
            oFile<<"Case #"<<i<<": "<<"INSOMNIA"<<std::endl;
            continue;
        }
        
        int mul=1;
        
        
        while(Num.size()<10){
            //std::cout<<"loop"<<Num.size()<<std::endl;
            val = mul * N;
            //std::cout<<"VAL"<<val<<std::endl;
            
            long dup = val;
            
            while(dup>0){
                int part = dup%10;
                dup/=10;
                Num.insert(part);
            }
            mul++;
            
        }
        
        oFile<<"Case #"<<i<<": "<<val<<std::endl;
        Num.clear();
        
    }
    
    return 0;
}

