#include <iostream>
 
using namespace std;
 
int main(){
    
 
    int t, aaa = 0;
    cin>>t;int i;
    for(i=0;i<t;i++){
        string str;
        int number, ovation = 0, result = 0;
        cin>>number;
        cin>>str;
        int len = str.size();
        ovation = int(str[0] - '0');
        for(int i=1;i<len;i++){
            if(ovation + result < i)
                result++;
            ovation = ovation + int(str[i] - '0');
        }
 
        cout<<"Case #"<<++aaa<<": "<<result<<endl;
    }
}
