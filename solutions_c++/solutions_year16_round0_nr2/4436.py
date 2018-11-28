#include <iostream>
#include <string>
using namespace std;

string s;
int main(int argc, const char * argv[]) {
    int t, ans, l;
    cin >> t;
    for (int x=1; x <= t; x++){
        s="";
        cin >> s;
        ans=0;
        while(s!=""){
            l=(int) s.length();
            if(s[l-1]=='-'){
                for(int i=0; i < l;i++){
                    if(s[i]=='+') s[i]='-';
                    else s[i]='+';
                }
                ans++;
            }
            while(s[l-1]=='+') s.erase(l-1,1);
        
        }

        cout << "Case #"<<x<<": ";
        cout << ans <<endl;
        
    }
    
    return 0;
}
