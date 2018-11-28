#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    int T;
    in>>T;
    for(int k=0;k<T;k++) {
        cout<<k<<"\n";
        int firstanswer;
        in>>firstanswer;
        int grid[4];
        int nil;
        for(int i=0;i<4;i++)
            for(int i2=0;i2<4;i2++) {
                if(i==firstanswer - 1)
                    in>>grid[i2];
                else
                    in>>nil;
            }
        int secondanswer;
        in>>secondanswer;
        int grid2[4];
        for(int i=0;i<4;i++)
            for(int i2=0;i2<4;i2++)
                if(i==secondanswer - 1)
                    in>>grid2[i2];
                else
                    in>>nil;
        sort(&grid[0],&grid[4]);
        sort(&grid2[0],&grid2[4]);
        int* p1 = &grid[0];
        int* p2 = &grid2[0];
        int solution = -1;
        int count = 0;
        while(p1 != &grid[4] && p2 != &grid2[4]) {
            if(*p1 == *p2) {
                solution = *p1;
                count++;
                p1++;
                p2++;
            }
            else if(*p1 < *p2)
                p1++;
            else if(*p1 > *p2)
                p2++;
        }
        if(count == 0)
            out<<"Case #"<<(k+1)<<": Volunteer cheated!"<<"\n";
        else if(count > 1)
            out<<"Case #"<<(k+1)<<": Bad magician!"<<"\n";
        else
            out<<"Case #"<<(k+1)<<": "<<solution<<"\n";
    }
}