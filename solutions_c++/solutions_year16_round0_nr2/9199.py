#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <unordered_set>
#include <string>


using namespace std;

void leastManeuvers(string);

void leastManeuvers(string s){
    char prev = s[0];
    int count = 0;
    for (size_t i=1;i<s.length();++i){
        if (s[i] != prev)
            count++;
        prev = s[i];
    
    }
    
    if (prev == '-')
        count++;
   
    cout<<count<<endl;

}



int main(){
    
    
    int n;
    string input;
    istringstream ss;
    string  s;
    getline(cin,s);
    ss.str(s);
    ss>>n;
    ss.clear();
    for (int i=0;i<n;++i){
       
        getline(cin,s);
        ss.str(s);
        ss>>input;
        ss.clear();
        cout<<"Case #"<<i+1<<": ";
        leastManeuvers(input);
    
    
        
 
    
    }
    
}