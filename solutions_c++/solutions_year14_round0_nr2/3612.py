#include <fstream>
#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
    ifstream fin("cookie.in");
    FILE *fout;
    fout = fopen("cookie.out", "w");
    
    int t=0; fin >> t;
    for(int i=0; i<t; ++i) {
        double total=0;
        double farm,sec,win; fin >> farm >> sec >> win;
        double per=2;
        
        fprintf(fout, "Case #%d: ", i+1);
        if(farm>win) {fprintf(fout, "%.9f\n", win/per); continue;}
        
        while(true) {
            // if buying a farm is most optimal, buy
            if(farm/per + win/(per+sec) < win/per) {
                total += farm/per;
                per += sec;
            } else {
                // WIN!!!
                fprintf(fout, "%.9f\n", total+win/per);
                break;
            }
        }
    }
}
