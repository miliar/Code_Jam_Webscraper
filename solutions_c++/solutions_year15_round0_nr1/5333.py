#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <fstream>
#include <cstdio>
using namespace std;
int main(int argc, char* argv[]) {
    ifstream input(argv[1]);
    ofstream output(argv[2]);
    int t;
    input>>t;
    for(int i=0; i<t; i++) {
        int val;
        string value;
        input>>val>>value;
        int standing=(int)(value[0]-'0');
        int ans=0;
        for(int j=1; j<=val; j++) {
            if(standing<j && value[j]!='0'){
                ans+=(j-standing);
                standing=j;
            }
            standing+=(int)(value[j]-'0');
        }
        output<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    input.close();
    output.close();
    return 0;
}
