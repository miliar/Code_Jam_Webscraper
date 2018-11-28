#include<iostream>
using namespace std;

int main() {
    int T=0;
    cin>>T;
    int t = T;
    int n=0,m=0;
    
    
    int gh[10][10] = {0}; //grass height
    
    while(t--) {
               cin>>n>>m;
        int breaked =0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                cin>>gh[i][j];
            }
        }
    
        
        //inefficient coding
        for(int i=0; i<n; i++) {
            if(breaked) break;
            for(int j=0; j<m; j++) {
                if(breaked) break;
                
                if(gh[i][j] == 1) {
                    int rowwise = 1;
                    int colwise = 1;
                    for(int k=0; k<n; k++) {
                        if(gh[k][j] != 1) {
                            rowwise = 0;
                            break;
                        }
                    }
                    for(int k=0; k<m; k++) {
                        if(gh[i][k] != 1) {
                            colwise = 0;
                            break;
                        }
                    }
                
                    if(!(rowwise || colwise)) {
                        breaked = 1;                      
                    }
                }
            }
        }
        
        if(breaked) {
            cout<<"Case #"<<T-t<<": NO\n";
        } else {
            cout<<"Case #"<<T-t<<": YES\n";
        }
    }
    return 0;
}
