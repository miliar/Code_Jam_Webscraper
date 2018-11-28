#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>

int main(int argc, const char * argv[])    {
    
    //std::ifstream file("A-small-practice.in-2.txt");
    
    std::ifstream file("sample2.txt");
    std::ofstream oFile;
    oFile.open("Task2_answer_Large.txt");
    
    //std::vector<char> stack;
    std::stack<char> stk;
    
    std::string str;
    std::getline(file,str);
    int T = std::stoi(str);
    
    if(T>100 && T<1)
        return 0;
    
    int count =0;
    
    for(int i=1;i<=T;i++){
        std::getline(file,str);
        //std::cout<<str<<std::endl;
        
        
        for(int y=str.length()-1;y>=0;y--){
            //std::cout<<str.length();
            if(str[y]=='-'){
                //flip entire
                //stk.push('+');
                count++;
                std::string sub = str.substr(0,y+1); //top to i
                /*for(int k=0;k<sub.length();k++){
                 if(sub[k]=='-')
                 stk.push('+');
                 else
                 stk.push('-');
                 }*/
                str.erase(0,sub.length());
                //std::cout<<"sub "<<sub<<std::endl;
                //std::reverse(sub.begin(),sub.end());
                //insert
                std::string neww;
                for(int k=sub.length()-1;k>=0;k--){
                    if(sub[k]=='-'){
                        neww = '+' + neww;
                    }
                    else
                        neww = '-' + neww;
                    //std::cout<<"NEWW "<<neww<<std::endl;
                    
                }
                /*std::reverse(neww.begin(), neww.end());
                 std::cout<<"NEWW "<<neww<<std::endl;
                 
                 if(neww==sub){
                 std::string neww;
                 for(int u=0;u<sub.length();u++){
                 neww = neww + '-';
                 count++;
                 }
                 }
                 */
                str = neww+str;
                //std::cout<<"final "<<str<<std::endl;
            }
        }
        
        oFile<<"Case #"<<i<<": "<<count<<std::endl;
        count=0;
    }
    
    
    return 0;
}

