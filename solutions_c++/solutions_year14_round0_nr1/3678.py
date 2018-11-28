#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <sstream>
#include <map>
using namespace std;

string readRow(ifstream &in,map<int,int> &mp,int &ans,bool is2){
    int count=0;
    int card=0;
    for(int x=1;x<=4;x++){
        for(int y=1;y<=4;y++){
            int item=0;
            in>>item;
            if(ans==x){
                mp[item]++;
                if(is2){
                    if(mp[item]>1)
                        count++;
                    if(count==1 && card==0)
                        card=item;
                }
            }
        }
     }
    stringstream ss;
    ss<<card;
    switch(count){
        case 0: return "Volunteer cheated!"; break;
        case 1: return ss.str(); break;
        default: return "Bad magician!";
    }
}

int main(){
ifstream in("A-small-attempt0.in");
FILE* f=fopen("out.txt","w");
//read in number of test cases
int tc=0;
in>>tc;
for(int i=1;i<=tc;i++){
int ans1=0;
map<int,int> mp;
in>>ans1;
readRow(in,mp,ans1,false);
int ans2=0;
in>>ans2;
string s=readRow(in,mp,ans2,true);

fprintf(f,"Case #%d: %s\n",i,s.c_str());
}
in.close();
}