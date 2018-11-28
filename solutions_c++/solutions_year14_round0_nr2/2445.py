//
//  main.cpp
//  GoogleJam
//
//  Created by Alexandre Decuq on 24/03/14.
//  Copyright (c) 2014 Alexandre Decuq. All rights reserved.
//

//#include "main.h"

#include <vector>
#include <set>
#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <cassert>
#include <iomanip> // for setprecision()
#include <cmath> //ceil() or floor()

using namespace std; //std::to_string(int)



/* *********************************************************************************
 *      Backtracking solution : ok for small input.                                   *
 * *********************************************************************************
 * Le problÃ¨me avec le code actuel c'est que l'on "s'enfonce" jusqu'au bout avant *
 * de se rendre compte que c'est impossible et que le tout premier choix n'Ã©tait  *
 * pas le bon...                                                                   *
 *                                                                                 *
 * => il faut ajouter du Forward checking
 ***********************************************************************************
 */

#define DEBUG 0

double arrounded(double input)
{
    cout<<"input="<<input<<" & ";
    double tmp=ceil(input*10000000)/10000000.0;
    cout<<"arrounded="<<tmp<<endl;
    return input;
}

bool buyFarm(double X, double C, double F, double curF) {
    double no = X/curF; //on n'achte plus aucune farm
    double yes=C/curF+X/(curF+F); //on achte 1 farm
    if(DEBUG) cout<<"no="<<no<<" & yes="<<yes<<endl;
    return yes<no;
}

int main()
{
    int T, A;
    scanf("%d", &T);
    double C, F, X, result, curF;
    
    for(int t=1; t<=T; t++)
    {
        scanf("%lf %lf %lf", &C, &F, &X);
        if(DEBUG) cout<<"C="<<C<<",F="<<F<<",X="<<X<<endl;
        result=0.0;
        curF=2.0;
        while(true) {
            if(DEBUG) cout<<setprecision(16)<<"result="<<result<<endl;
            if(DEBUG) cout<<"curF="<<curF<<endl;
            if(! buyFarm(X,C,F,curF) ) {
                result+=X/curF;//pareil que 10000
                break;
            }
            else {
                if(DEBUG) cout<<"C/curF="<<C<<"/"<<curF<<endl;
                result+=C/curF;
                curF+=F;
            }
            
        }

        if(DEBUG) cout<<"result="<<result<<endl;
        printf("Case #%d: %.7f\n", t, result);
    }
}