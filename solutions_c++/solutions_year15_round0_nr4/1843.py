#include <iostream> // cin, cout
#include <fstream> // io redirection
using namespace std;


int main(){
    
    ifstream arq(getenv("INPUT"));
    cin.rdbuf(arq.rdbuf());
    
    ofstream brq(getenv("OUTPUT"));
    cout.rdbuf(brq.rdbuf());
    
    
    
    // Number of Testcases
    int T;
    cin >> T;
    
    for(int t=0;t<T;t++){
        
        int r,c,x,a,b;
        cin>> x >> a >> b;
        r=min(a,b);
        c=max(a,b);
        
        string winner;
        
        if(x==1){
            winner = "GABRIEL";
        }
        
        if(x==2){
            winner = (r*c)%2==0 ? "GABRIEL" : "RICHARD";
        }
        
        if(x==3){
            winner = (r==3 || (r==2 && c==3)) ? "GABRIEL" : "RICHARD";
        }
        
        if(x==4){
            winner = (c ==4 && r>=3 ) ? "GABRIEL" : "RICHARD";
        }
       
        
        // output result
        cout << "Case #" << (t+1) << ": " << winner << endl;
    }
    
    return 0;
    
}
