#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int firstSomething(char s, string line){
    for(int i = 0; i <= line.size(); i++){
        if(line[i] == s)
            return i;
    }
    return -1;
}

int firstMin(string line){
    return firstSomething('-', line);
}

int firstPlus(string line){
    return firstSomething('+', line);
}


int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output", "w", stdout);
    int n;
    scanf("%d\n", &n);

    for(int i=0; i<n; i++){
        int times = 0;
        string line;
        getline(cin, line);
        while(true){
            if(firstMin(line) == -1)
                break;
            if(firstPlus(line)== -1){
                times++;
                break;
            }
            if(firstMin(line)==0){
                int val = firstPlus(line);
                for(int j=0; j<val; j++){
                    line[j] = '+';
                }
            }
            else if(firstPlus(line)==0){
                int val = firstMin(line);
                for(int j=0; j<val; j++){
                    line[j] = '-';
                }
            }
            times++;
        }
        printf("Case #%d: %d\n", i+1, times);
    }
    return 0;
}
