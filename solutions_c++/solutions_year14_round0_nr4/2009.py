#include <string>
#include <iostream>
#include <algorithm>
#include <list>
using namespace std;

int main()
{
    int T, N, i, h, j, k, win, cheatWin, last;
    cin>>T; 
    double mass;
    list<double> masses[2];

    list<double>::iterator it[2];
    for(i = 0; i < T;i++)
    {
        cin>>N;
      
        for(h = 0; h < 2; h++)
        {
            for(j = 0; j < N; j++)
            {               
                cin>> mass;    
                masses[h].push_back(mass); 
            } 
            masses[h].sort();  
        }

        list<double> massesWithCheat(masses[0].begin(), masses[0].end());
        list<double> massesNoCheat(masses[1].begin(), masses[1].end());

        it[0] = masses[0].begin();
        it[1] = masses[1].begin();
        win = 0;
        while(false == masses[0].empty() && false == masses[1].empty()){
            if(it[1] == masses[1].end()){
                it[1]--;
                if(*it[0] > *it[1]){                    
                    win ++;
                }
                it[0] = masses[0].erase(it[0]);
                it[1] = masses[1].erase(masses[1].begin());
            }
            if(*it[0] < *it[1]){
                it[0] = masses[0].erase(it[0]); 
                it[1] = masses[1].erase(it[1]);
                it[1] -- ;
            }    
            it[1]++;
        }
        

        it[0] = massesWithCheat.begin();
        it[1] = massesNoCheat.begin();
        cheatWin = 0;
        while(false == massesWithCheat.empty() || false == massesNoCheat.empty()){
            if(*it[0] < *it[1]){
                it[1] = massesNoCheat.end();
                it[1] --;
            }else{
               cheatWin ++; 
            } 
            massesNoCheat.erase(it[1]);
            it[1] = massesNoCheat.begin();
            it[0] = massesWithCheat.erase(it[0]);   
        }
        cout<<"Case #"<<i+1<<": "<<cheatWin<<" "<<win<<endl;
    }
    return 0;
}


