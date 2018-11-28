#include <iostream>
using namespace std;
int main(){
    int ttCase;
    cin >> ttCase;
    for(int currC = 0;currC < ttCase;currC++){
        int result = 0;
        int a,b,k;
        int temp;
        cin >> a >> b >> k;
        
        if ( b > a ){
            temp = a;
            a = b;
            b = temp;
        }
        for(int i=0;i<a;i++){
    
            for (int j=0;j<b;j++){
                if((i&j) < k){
                    result++;
                }
               
            }
            
            
        }
        
        
    
        
        cout << "Case #" << currC+1 << ": " << result << endl;
    }
}