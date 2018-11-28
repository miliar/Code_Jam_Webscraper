#include <iostream>
#include <string>
#include <vector>
using std::cout;
using std::cin;
using std::string;
using std::vector;
using std::endl;
int main(){
    int n;
    
    cin>>n;
    for(int i=0;i<n;i++){
        int t;
        string str;
        cin>>t>>str;
        int total_audience = 0;
        int result = 0;
        for(int j=0;j<=t;j++){
            if(j>total_audience){
                result += j-total_audience;
                total_audience += j-total_audience;
            }
            total_audience+=str[j]-'0';
        }
        
        cout<<"Case #"<<i+1<<": "<<result<<endl;
    }
    return 0;
}