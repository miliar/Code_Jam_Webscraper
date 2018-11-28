#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    int t;
    cin >> t;
    
    for(int i=0;i<t;++i){
        string s;
        cin >> s;
        //We can see that "++--" is equal to "+-", because consecutive '+' or '-' must be flipped together, otherwise it will cause more complicated situation. And also the last '+' can be omitted.
        string news = "";
        news+=s[0];
        for(int j=1;j<s.length();j++){
            if(s[j]!=s[j-1]){
                news+=s[j];
            }
        }
        s=news;
        if(s[s.length()-1]=='+'){
            s=s.substr(0, s.length()-1);
        }
        //We use greedy algorithm, to generate longer consecutive '+' or '-', for the pattern we generated above, the flip time equal to the pattern's length
        cout << "Case #" << i+1 << ": " << s.length() << endl;
        
    }
    return 0;
}
