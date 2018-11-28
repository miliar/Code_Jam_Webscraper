
//#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <string>
using namespace std;

ifstream cin("/Users/Nagi2/Downloads/GCJ2016/B-large.in");
ofstream cout("/Users/Nagi2/Downloads/bbbL.txt");


int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        string s;
        cin >> s;
        string s2=s.substr(0,1);
        for(int i=1;i<s.size();i++){
            if(s[i]!=s[i-1]) s2+=s[i];
        }
        int ans=0;
        if(s2.size()%2==1 && s[0]=='+') ans = s2.size()-1;
        if(s2.size()%2==1 && s[0]=='-') ans = s2.size();
        if(s2.size()%2==0 && s[0]=='+') ans = s2.size();
        if(s2.size()%2==0 && s[0]=='-') ans = s2.size()-1;
        cout << "Case #" << t+1<< ": " << ans << endl;
        


        
    }
    
    return 0;
}
