#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(){
    
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        string str;
        cin>>str;
        char c = str[0];
        int times = 0;
        int j=0;
        while(j<str.length()-1){
            while(str[j] == c && j<str.length())
                j++;
            if(j >=str.length()) break;
            c = str[j];
            times++;
            
        }
        if( (j>=str.length()  && str[j-1] == '-') || str[j] == '-'  )
            cout<<"Case #"<<i+1<<": " << times+1<<endl;
        
        else if((j>=str.length()  && str[j-1] == '+') ||str[j] == '+')
            cout<<"Case #"<<i+1<<": " <<times<<endl;
    }

}