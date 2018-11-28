#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{

    FILE *fin = freopen("B-large.in", "r", stdin);
    FILE *fout = freopen("B-large.out", "w", stdout);
    long T,j=0,maneuver=0;
    string pancakes;
    cin>>T;
    while(T--){
        maneuver=0;
        cin>>pancakes;
        j++;
        for(int i=1;i<pancakes.length();i++){
            if(pancakes[i]!=pancakes[i-1])
                maneuver++;
        }
        if(pancakes[pancakes.length()-1]=='-')
            maneuver++;
        cout<<"Case #"<<j<<": "<<maneuver<<endl;
    }
    return 0;
}