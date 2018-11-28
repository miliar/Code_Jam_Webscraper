#include <iostream>
#include <cstdio>
#include <string.h>

using namespace std;

int main(){
freopen("B-large.in","r",stdin);
freopen("resultQ2.txt","w",stdout);

int num;
cin >> num;

for(int times = 1; times <= num; times++){
    string s;
    cin >> s;
    int counter = 1;
    char pre = s[0];
    for(int i = 0; i < s.length();i++){
        if(s[i] != pre){
            counter++;
            pre = s[i];
        }
    }
    if(s[s.length()-1] == '+'){
        counter = counter-1;
    }
    cout << "Case #" << times << ": " << counter << endl;
}

return 0;
}
