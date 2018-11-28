#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
    int T,X,R,C;
    cin >> T;
    for(int i = 1;i<=T;++i){
        cin >> X >> R >> C;
        int Area = R*C; 
        if(X==1){
           cout << "Case #" << i << ": GABRIEL\n";
        }    
        else if(X==2){
           if((Area)%2!=0) cout << "Case #" << i << ": RICHARD\n";
           else cout << "Case #" << i << ": GABRIEL\n";
        }
        else if(X==3){
           if(Area == 6 || Area == 9 || Area == 12)
              cout << "Case #" << i << ": GABRIEL\n";
           else 
              cout << "Case #" << i << ": RICHARD\n"; 
        }  
        else if(X==4){
           if(Area == 16 || Area == 12)
              cout << "Case #" << i << ": GABRIEL\n";
           else 
              cout << "Case #" << i << ": RICHARD\n"; 
        }     
    }
    return 0;
}
