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
 * Le problème avec le code actuel c'est que l'on "s'enfonce" jusqu'au bout avant *
 * de se rendre compte que c'est impossible et que le tout premier choix n'était  *
 * pas le bon...                                                                   *
 *                                                                                 *
 * => il faut ajouter du Forward checking
 ***********************************************************************************
 */

#define DEBUG 0

void display(vector<float>& somebody)
{
    for(int i=0;i<somebody.size();++i) {
        cout<<somebody[i]<<",";
    }
    cout<<endl;
}

int playWar(vector<float>& noemie, vector<float>& ken)
{
    sort(noemie.begin(),noemie.end());
    sort(ken.begin(),ken.end()); //Ken strategy :
    int tab[ken.size()];
    memset(tab,0,sizeof(tab));
    
    int cpt=0;
    for(int i=0;i<noemie.size();++i) {
        for(int j=0;j<ken.size();++j) {
            if(ken[j]<noemie[i]) continue; //the first greater than Noemie
            if(! tab[j]) {
                tab[j]=1;
                ++cpt;
                break;
            }
        }
    }
    return noemie.size()-cpt;
}

bool NoemieWinAll(vector<float> noemie, vector<float>& ken, int i)
{
    if(DEBUG) cout<<"i="<<i<<endl;
    sort(noemie.begin()+i,noemie.end(),std::greater<float>());
    if(DEBUG) display(noemie);
    if(DEBUG) display(ken);
    for(;i<noemie.size();++i) {
        if(noemie[i]<ken[i]) return false;
    }
    return true;
}

int playDeceitfulWar(vector<float>& noemie, vector<float>& ken)
{
    sort(noemie.begin(),noemie.end()); //Noemie strategy :
    sort(ken.begin(),ken.end(),std::greater<float>());
    int tab[ken.size()];
    memset(tab,0,sizeof(tab));
    int cpt=0;
    while(! NoemieWinAll(noemie,ken,cpt)) {
        ++cpt;
    }
    return noemie.size()-cpt;
}

int main()
{
    int T, N;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        scanf("%d", &N);
        vector<float> noemie(N);
        vector<float> ken(N);
        for(int i=0;i<N;++i) {
            scanf("%f", &noemie[i]);
        }
        for(int i=0;i<N;++i) {
            scanf("%f", &ken[i]);
        }
        
        int d = playDeceitfulWar(noemie, ken);
        int w = playWar(noemie, ken);
        
        printf("Case #%d: %d %d\n", t, d, w);
    }
}