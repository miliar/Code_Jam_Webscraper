#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int minFlips(string in){
    int i = 0;
    int flips = 0;
    char cur = 'o';
    while(i<in.length()){
        if (cur != in[i]){
            if (in[i] != cur){
                if (in[i] == '-')
                    flips+=2;

                cur = in[i];
            }
        }
        i++;
    }
    if (in[0] == '-')
        flips--;

    return flips;
}

int main(){
    int k;
    string in;
    cin >> k;
    for (int i=0;i<k;i++)
    {
        cin >> in;
        cout << "Case #" << (i+1) << ": " << minFlips(in) << endl;
    }
}
