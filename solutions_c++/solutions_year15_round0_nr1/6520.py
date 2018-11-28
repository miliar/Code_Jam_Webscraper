#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;


int main(){
    freopen("/Users/Omar/Desktop/input.txt","r",stdin);
    freopen("/Users/Omar/Desktop/output.txt","w",stdout);
    int t;
    cin >> t;
    
    for (int i=1; i<=t; i++){
        int shy;
        string aud;
        cin >> shy >> aud;
        int standing = 0, invited = 0;
        for (int j=0; j<(int)aud.size(); j++){
            if (standing >= j){
                standing += (aud[j] - '0');
            }
            else{
                if (aud[j] != '0'){
                    invited += (j - standing);
                    standing += ((j - standing) + (aud[j] - '0'));
                }
            }
            //cout << "---" << aud[j] << "---" << j << " " << standing << " " << invited << endl;
        }
        //cout << endl;
        cout << "Case #" << i << ": " << invited << endl;
    }
    
    return 0;
}