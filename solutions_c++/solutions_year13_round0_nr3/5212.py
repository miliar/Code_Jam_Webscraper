#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <cstring>
#include <math.h>
#include <iomanip>
#include <locale>
#include <sstream>
#include <string>

using namespace std;

//function declaraions
bool pallindromic(int n);

int main(){

    string fname = "small";
    freopen((fname+".in").c_str(), "r", stdin);
    freopen((fname+".out").c_str(), "w", stdout); //------- needed to output to file

    //number of cases to follow
    int cases;
    scanf("%d", &cases);

    for (int i = 1; i <= cases; ++i) {
        //values about each case
        int s,f;
        scanf("%d%d", &s, &f);

        // logic
        //first find root of s and f
        int rS,rF;
        rS = ceil(sqrt(s));
        rF = sqrt(f);
        int numPerfects;
        numPerfects = 0;
        for(int aa = rS;aa<=rF;aa++){
            if(pallindromic(aa)&&pallindromic(aa*aa)){
                numPerfects++;
            }
        }



        // answer
        printf("Case #%d: ", i);
        cout<<numPerfects<<endl;
    }

    return 0;
}

bool pallindromic(int n){
    string nStr;
    ostringstream convert;
    convert << n;
    nStr = convert.str();

    int l;
    l = nStr.length();
    for (int i = 0; i<l/2;i++){
        if(nStr[i] != nStr[l-i-1]){
            return false;
        }
    }
    return true;
}
