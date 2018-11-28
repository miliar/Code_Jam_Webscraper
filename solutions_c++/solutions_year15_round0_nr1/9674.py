#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main(){
    int tcase,smax,count=1;
    string shyst;
    
    cin>>tcase;
    
    while(tcase--){
        
        int pplstn = 0;
        int extppl = 0;
        
        cin>>smax;
        cin>>shyst;
        
        pplstn = shyst[0] - '0';
        
        for(int i=1;i<shyst.length();i++){
            if(pplstn >= i){
                pplstn += shyst[i] - '0';
            }
            else{
                if(shyst[i] != '0'){
                    extppl += i - pplstn;
                    pplstn += extppl + shyst[i] - '0';
                }
            }
        }
        
        cout<<"Case #"<<count++<<": "<<extppl<<endl;
    }
    
    return 0;
}
