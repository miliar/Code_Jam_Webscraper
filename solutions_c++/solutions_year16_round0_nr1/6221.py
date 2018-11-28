#include <iostream>
#include <string>
using namespace std;
bool a[10];
int main() {
    int t;
    long long int n;
    cin>>t;
    
    for(int j=0; j<t; j++){
        cin>>n;
        for(int i = 0; i<10; i++)
            a[i] = false;
        
        bool flag = true;
        cout<<"Case #"<<j+1<<": ";
        string s = to_string(n);
        int c = 1;
        long long int x = n;
        if(n == 0){
            cout<<"INSOMNIA"<<endl;
        }
        else{
            while(flag){
                
                
                
                for(int i = 0; i<s.length(); i++){
                    
                    switch(s[i]){
                        case '0': a[0] = true;break;
                        case '1': a[1] = true;break;
                        case '2': a[2] = true;break;
                        case '3': a[3] = true;break;
                        case '4': a[4] = true;break;
                        case '5': a[5] = true;break;
                        case '6': a[6] = true;break;
                        case '7': a[7] = true;break;
                        case '8': a[8] = true;break;
                        case '9': a[9] = true;break;
                    }
                    
                }
                if(a[0] &&a[1] && a[2] && a[3] && a[4] && a[5] && a[6] && a[7]&& a[8] && a[9]){
                    flag = false;
                    cout<<x<<endl;
                }
                c++;
                x = n*c;
                s = to_string(x);
                
                
            }
            
        }
    }
}