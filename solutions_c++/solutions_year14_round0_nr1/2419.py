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

void print(set<int> row) {
    for(set<int>::iterator it = row.begin(); it!= row.end(); ++it) {
        cout<<*it<<",";
    }
    cout<<endl;
}

void print2(vector<int> row) {
    cout<<"inter=";
    for(int i=0;i<row.size();++i) {
        cout<<row[i]<<",";
    }
    cout<<endl;
}

int main()
{
    int T, A;
    scanf("%d", &T);
    int grid[4][4];
    
    for(int t=1; t<=T; t++)
    {
        memset(grid,0,sizeof(grid));
        
        scanf("%d", &A);
        set<int> row1;
        for(int i=0;i<4;++i) {
            scanf("%d %d %d %d", &grid[i][0], &grid[i][1], &grid[i][2], &grid[i][3]);
            if(i+1==A) {
                row1.insert(grid[i][0]);
                row1.insert(grid[i][1]);
                row1.insert(grid[i][2]);
                row1.insert(grid[i][3]);
            }
        }
        if(DEBUG) print(row1);
        scanf("%d", &A);
        set<int> row2;
        for(int i=0;i<4;++i) {
            scanf("%d %d %d %d", &grid[i][0], &grid[i][1], &grid[i][2], &grid[i][3]);
            if(i+1==A) {
                row2.insert(grid[i][0]);
                row2.insert(grid[i][1]);
                row2.insert(grid[i][2]);
                row2.insert(grid[i][3]);
            }
        }
        if(DEBUG) print(row2);
        
        std::vector<int> inter(4);
        std::vector<int>::iterator it;
        it=std::set_intersection (row1.begin(), row1.end(), row2.begin(), row2.end(), inter.begin());
        inter.resize(it-inter.begin());
        if(DEBUG) print2(inter);
        
        printf("Case #%d: ", t);
        if(inter.size()==1) {
            printf("%d\n", inter[0]);
        }
        else if(inter.size()==0) {
            printf("Volunteer cheated!\n");
        }
        else {
            printf("Bad magician!\n");
        }
    }
}