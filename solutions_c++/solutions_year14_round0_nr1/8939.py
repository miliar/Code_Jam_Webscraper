#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

FILE *in,*out;
int x,y;

#define deb 0

map <int,int> mark;

int main() {
    in=fopen("input.in","r");
    ofstream myfile;
    myfile.open ("output.out");

    int cases;
    fscanf(in,"%d",&cases);

    for(int test=0; test<cases; test++) {
        mark.clear();
        int counter = 0,ans;
        int n;
        fscanf(in,"%d",&n);
        for(int t=0; t<4; t++) {
            for(int tt=0; tt<4; tt++) {
                int temp;
                fscanf(in,"%d",&temp);
                if(t+1 == n)mark[temp]=1;
            }
        }
        fscanf(in,"%d",&n);
        for(int t=0; t<4; t++) {
            for(int tt=0; tt<4; tt++) {
                int temp;
                fscanf(in,"%d",&temp);
                if(t+1 == n && mark[temp]) {
                    counter++;
                    ans=temp;
                }
            }
        }if(counter == 1)myfile<<"Case #"<<test+1<<": "<<ans<<endl;
        else if(counter == 0)myfile<<"Case #"<<test+1<<": Volunteer cheated!"<<endl;
        else myfile<<"Case #"<<test+1<<": Bad magician!"<<endl;
    }
    fclose(in);
    return 0;
}
