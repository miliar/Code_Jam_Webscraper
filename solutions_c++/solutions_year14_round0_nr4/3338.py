#include <iostream>
#include <list>
#include <fstream>
using namespace std;

int main(){
    ifstream in("D-large.in");
    ofstream out("D-large.out");
    int cases;
    in>>cases;
    int blocks;
    
    list<float> naomi;
    list<float> naomi2;
    list<float> ken2;
    list<float> ken;
    
    list<float>::iterator it;
    
    int i=0;
    int j=0;
    int war;
    int dwar;
    float temp;
    while(i<cases){
        war = 0;
        dwar = 0;
        in>>blocks;
        for(j=0; j<blocks; j++){
            in>>temp;
            naomi.push_back(temp);  
            naomi2.push_back(temp);
        }
        for(j=0; j<blocks; j++){
            in>>temp;
            ken.push_back(temp); 
            ken2.push_back(temp);
        }
        naomi.sort();
        ken.sort();
        naomi2.sort();
        ken2.sort();
        /*
        for(it= naomi.begin(); it != naomi.end(); ++it){
            cout<<*it<<"    ";   
        }
        cout<<endl;
        for(it= ken.begin(); it != ken.end(); ++it){
            cout<<*it<<"    ";   
        }
        cout<<endl;*/
        while(ken.empty() == false){
            if(ken.back() > naomi.back()){
                naomi.pop_back();
                ken.pop_back();   
            }else{
                naomi.pop_back();
                ken.pop_front();
                war++;   
            }
            
            /*if(ken2.back()>naomi2.front()){
                ken2.pop_back();
                naomi2.pop_front();   
            }else{
                ken2.pop_front();
                naomi2.pop_front();
                dwar++;   
            }*/
            if(naomi2.back()> ken2.back()){
                naomi2.pop_back();
                ken2.pop_back();
                dwar++; 
            }else{
                ken2.pop_back();
                naomi2.pop_front();  
            }
        }
        
        
        
        out<<"Case #"<<i+1<<": "<<dwar<<"  "<<war<<endl;
        naomi.clear();
        ken.clear();
        i++;
    }
    in.close();
    out.close();
    //system("pause");
    return 0;   
}
