//

//  a.cpp

//  

//

//  Created by liumingming on 4/9/16.

//

//



#include <stdio.h>

#include <iostream>

#include <set>

#include <map>

#include <string>

#include <string.h>

#include <cstring>

#include <algorithm>



using namespace std;



int main(){

    freopen("1.txt","r",stdin);

    int n;

    scanf("%d", &n);

    for(int i = 0; i < n; ++i){

        unsigned long long d;

        scanf("%llu", &d);

        bool mark[11];

        memset(mark, 0, sizeof(mark));

        int cntmark = 0;

        bool full = false;

        set<unsigned long long> number;

        bool first = true;

        unsigned long long ori = d;

        while(number.find(d) == number.end() || first){

            //cout << "##########################\n";

            first = false;

            //cout << "d is " <<  d << endl;

            number.insert(d);

            char cd[100];

            memset(cd, 0, sizeof(cd));

            sprintf(cd, "%llu", d);

            int len = strlen(cd);

            for(int j = 0; j < len; ++j){

                int meet = cd[j] - '0';

                if(!mark[meet]){

                    cntmark++;

                    mark[meet] = 1;

                }

                //cout << "cntmark is " << cntmark << endl;

                if(cntmark == 10){

                    break;

                }

            }

            if(cntmark == 10){

                full = true;

                printf("Case #%d: %s\n", i + 1, cd);

                break;

            }

            d = d + ori;

        }

        if(!full)

            printf("Case #%d: INSOMNIA\n", i + 1);

    } // end for

    return 0;

}