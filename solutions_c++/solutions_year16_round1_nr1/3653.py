#include <algorithm>

#include <iostream>
#include <fstream>

#include <string.h>
#include <limits>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>

#include <map>
#include <set>
#include <vector>
#include <list>
#include <set>
#include <set>
#include <sstream>
#include <stack>
#include <queue>

using namespace std;

string lastword(string earlier, string word , int i){

    if(word.length() == i){
        return earlier;
    }

    stringstream ss;
    string s;
    char c = word[i];
    ss << c;
    ss >> s;

    string a = earlier + s;
    string b = s + earlier;

    if(a<b){
        return lastword(b,word,i+1);
    }else{
        return lastword(a,word,i+1);
    }
}

int main(){

    ofstream myfile;
    myfile.open ("output.in");

    int T;

    cin>>T;

    for(int case_i = 1 ; case_i<=T ; case_i++){

        //char earlier[1000] = "";
        string earlier = "";
        string word;
        cin>>word;

        int i = 0;
        cout<<lastword(earlier,word,i)<<endl;
        myfile<<"Case #"<<case_i<<": "<<lastword(earlier,word,i)<<endl;


//        myfile<<"Case #"<<case_i<<": "<<22<<endl;
   	}

    return 0;
}










