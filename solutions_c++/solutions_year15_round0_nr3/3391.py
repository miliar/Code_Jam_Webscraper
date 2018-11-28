//  Created by Lyamani Moulay Abdellatif on 11/04/2015.
//  Copyright (c) 2015 Lyamani Moulay Abdellatif. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

typedef long long LL;
typedef pair<char, int> PS;

#define LINESZ 1024

PS marray[4][4] = {   {PS('1',1),     PS('i',1) ,    PS('j',1),     PS('k',1)} ,
                      {PS('i',1),     PS('1',-1),    PS('k',1),     PS('j',-1)},
                      {PS('j',1),     PS('k',-1),    PS('1',-1),    PS('i',1)} ,
                      {PS('k',1),     PS('j',1) ,    PS('i',-1),    PS('1',-1)} };

int index(char s) {
    
    if(s == 'i'){
        return 1;
    }
    else if(s == 'j'){
        return 2;
    }
    else if(s == 'k'){
        return 3;
    }
    
    return 0;
}

PS multiply(char s1, char s2) {
    
    int i = index(s1);
    int j = index(s2);
    
    return marray[i][j];
}

bool perform (string  ijk ){
    
    int sign = 1;
    
    if (ijk.find('i') == std::string::npos && ijk.find('j') == std::string::npos )
        return false;
    if (ijk.find('i') == std::string::npos && ijk.find('k') == std::string::npos )
        return false;
    if (ijk.find('k') == std::string::npos && ijk.find('j') == std::string::npos )
        return false;
        
        
    while (ijk.size() > 3 ) {
        size_t index = 0;
        if(ijk[0] == 'i' && ijk[1] == 'j')
            index = 2;
        else if(ijk[0] == 'i' )
            index = 1;
        
        PS res = multiply( ijk[index] , ijk[index+1]);
        
        if(res.first == '1' )
            ijk.erase(index, 2);
        else{
            ijk[index] = res.first;
             ijk.erase(index+1, 1);
           
           // ijk.replace(index, 2, &res.first);
        
        }
        sign *= res.second;
    }
    
    if (ijk.size() == 3  && ijk == "ijk" && sign == 1)
        return true;
    else
        return false;
}

int main(int argc, const char * argv[])
{

    
    freopen("output.out","w", stdout);
    FILE* in = freopen("input.in","r", stdin);
    
    int test,cases;
    long L, X;
    
    
    char str[LINESZ] ;
    char S[10000] ;
    
    cases=0;
    scanf("%d",&test);
    fgets (str, LINESZ, in) ;
    while (test){
        test--;
        cases++;
        
        
        scanf("%lu",  &L) ;
        scanf("%lu",  &X) ;
        scanf("%s", S) ;
        
        string fullstr = "";
        for (int i = 0; i < X; i++) {
            fullstr += S ;
        }

        bool res = perform(fullstr);
        
        if(res)
            cout<<"Case #"<<cases<<": "<< "YES" <<endl;
        else
            cout<<"Case #"<<cases<<": "<< "NO" <<endl;
    }
    
    return 0;
}

