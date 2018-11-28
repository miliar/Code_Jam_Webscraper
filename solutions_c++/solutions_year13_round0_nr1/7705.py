#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <iostream>
using namespace std;


string solve(vector<string> lst){
    int cntx=0;
    int cnty=0;
    int cntdot=0;

    for(int j=0;j<4;j++){
        for(int i=0;i<4;i++){
            if(lst[j].substr(i,1)=="X"){
                cntx++;
            }else if(lst[j].substr(i,1)=="O"){
                cnty++;
            }else if(lst[j].substr(i,1)=="T"){
                cntx++;
                cnty++;
            }else if(lst[j].substr(i,1)=="." && cntdot==0){
                cntdot++;
            }
        }
        if(cntx==4)return "X won";
        if(cnty==4)return "O won";
        cntx=0;
        cnty=0;
    }
    
    
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(lst[j].substr(i,1)=="X"){
                cntx++;
            }else if(lst[j].substr(i,1)=="O"){
                cnty++;
            }else if(lst[j].substr(i,1)=="T"){
                cntx++;
                cnty++;
            }
        }
        if(cntx==4)return "X won";
        if(cnty==4)return "O won";
        cntx=0;
        cnty=0;
    }
    
    for(int i=0;i<4;i++){
        if(lst[i].substr(i,1)=="X"){
            cntx++;
        }else if(lst[i].substr(i,1)=="O"){
            cnty++;
        }else if(lst[i].substr(i,1)=="T"){
            cntx++;
            cnty++;
        }
    }
    if(cntx==4)return "X won";
    if(cnty==4)return "O won";
    cntx=0;
    cnty=0;
    
    for(int i=0;i<4;i++){
        if(lst[i].substr(3-i,1)=="X"){
            cntx++;
        }else if(lst[i].substr(3-i,1)=="O"){
            cnty++;
        }else if(lst[i].substr(3-i,1)=="T"){
            cntx++;
            cnty++;
        }
    }
    if(cntx==4)return "X won";
    if(cnty==4)return "O won";
    cntx=0;
    cnty=0;
    
    if(cntdot!=0){
        return "Game has not completed";
    }
    
    return "Draw";
}


int main(int argc, const char * argv[])
{
        //CodeJam *codejam;
        
        char array[1001];
        std::string str;
        
        std::ifstream ifs( "a.txt" );
        
        //ifs.getline(array,1001);//捨行
        
        int k=1;
            
        while(!ifs.eof()){
            vector<string> lst;
            lst.clear();
            
            ifs.getline(array,1001);//捨行
            ifs.getline(array,1001);
            string str=array;
            lst.push_back(str);
            ifs.getline(array,1001);
            str=array;
            lst.push_back(str);
            ifs.getline(array,1001);
            str=array;
            lst.push_back(str);
            ifs.getline(array,1001);
            str=array;
            lst.push_back(str);
            
            string ret = solve(lst);
            
            std::cout << "Case #" << k << ": " << ret << std::endl;
            k++;
            
            str.clear();
        }
        return 0;

}