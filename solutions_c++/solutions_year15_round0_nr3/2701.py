#include <iostream> // cin, cout
#include <fstream> // io redirection
using namespace std;

string st;

char dp[10005][10005];
int sign[10005][10005];

char mult[4][4]  = {{'1','i','j','k'},
   {'i','1','k','j'},
   {'j','k','1','i'},
   {'k','j','i','1'}};

int f(char c){
    if(c=='1') return 0;
    else return c-'i' +1;
}
   
                 
int signs[4][4] =
   {{1,1,1,1},
    {1,-1,1,-1},
    {1,-1,-1,1},
    {1,1,-1,-1}};




int main(){
    
    ifstream arq(getenv("INPUT"));
    cin.rdbuf(arq.rdbuf());
    
    ofstream brq(getenv("OUTPUT"));
    cout.rdbuf(brq.rdbuf());
    
    
    
    // Number of Testcases
    int T;
    cin >> T;
    
    for(int t=0;t<T;t++){
        
        int l,x;
        cin >> l >> x;
        
        string s;
        cin >> s;
        
        st="";
        for(int i=0;i<x;i++){
            st=st+s;
        }
        
        for(int i=0;i<l*x;i++){
                    dp[i][i]=st[i];
                    sign[i][i]=1;

        }
        
        for(int i=0;i<l*x;i++){
            for(int j=i+1;j<l*x;j++){
                int sx= sign[i][j-1]*sign[j][j]*signs[f(dp[i][j-1])][f(dp[j][j])];
                char c =mult[f(dp[i][j-1])][f(dp[j][j])];
                dp[i][j]=c;
                sign[i][j]=sx;
                    
    
            }
        }
        
        bool possible = false;
        
    
        for(int i=1;i<l*x;i++){
            for(int j=i+1;j<l*x;j++){
                if(dp[0][i-1]=='i' && sign[0][i-1]==1 &&  dp[i][j-1]=='j' && sign[i][j-1]==1  && dp[j][l*x-1]=='k' && sign[j][l*x-1]==1 )
                    possible = true;
            }
        }
    
       
        
        // output result
        cout << "Case #" << (t+1) << ": " << (possible ? "YES" : "NO") << endl;
    }
    
    return 0;
    
}
