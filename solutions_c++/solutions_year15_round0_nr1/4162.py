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
        
        // the input data
        int smax;
        string s;
        cin>> smax >> s;
        
        // checking for each shyness level how much friend must be added
        int numFriends=0; // the number of friend to invite
        int counter=0; // running integral
        for(int i=0;i<smax+1;i++){
            numFriends=max(numFriends,i-counter);
            counter+=s[i]-'0';
        }
        
        // output result
        cout << "Case #" << (t+1) << ": " << numFriends << endl;
    }
    
    return 0;
    
}
