#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
#include<cstring>
#include<vector>
using namespace std;

FILE *IN,*OUT;

int abss(int a){
    if(a < 0) a = -a;
    return a;
}

void solve(int t){
    vector<pair<int,int> > V;
    int NoT;

    fscanf(IN,"%d",&NoT);
    for (int i = 0; i < NoT; i++) {
        int num;
        fscanf(IN,"%d",&num);
        V.push_back(make_pair(num,i+'A'));
    }
    
    if (NoT == 2) {
        if (V[0].first < V[1].first) {
            swap(V[0],V[1]);
        }
        fprintf(OUT,"Case #%d:",t+1);
        
        int delta = V[0].first - V[1].first;
        char saki = V[0].second;
        for (int i = 0; i < delta; i++) {
            fprintf(OUT," %c",saki);
        }
        for (int i = 0; i < V[1].first; i++) {
            fprintf(OUT," AB");
        }
        fprintf(OUT,"\n");
        return;
    }else{
        int max = V[0].first;
        int koukan = 0;
        for (int i = 1; i < NoT; i++) {
            if (V[i].first > max) {
                max = V[i].first;
                koukan = i;
            }
        }
        swap(V[0],V[koukan]);
        
        max = V[1].first;
        koukan = 1;
        for (int i = 2; i < NoT; i++) {
            if (V[i].first > max) {
                max = V[i].first;
                koukan = i;
            }
        }
        swap(V[1],V[koukan]);
        fprintf(OUT,"Case #%d:",t+1);
        
        for (int i = 0; i < V[0].first-V[1].first; i++) {
            char cc = V[0].second;
            fprintf(OUT," %c",cc);
        }
        
        for (int i = 2; i < NoT; i++) {
            char cc = V[i].second;
            while (V[i].first != 0) {
                V[i].first--;
                fprintf(OUT," %c",cc);
            }
        }
        char s1 = V[0].second,s2 = V[1].second;
        for (int i = 0; i < V[1].first; i++) {
            fprintf(OUT," %c%c",s1,s2);
        }
        fprintf(OUT,"\n");
        return;
    }
}

int main(){
    IN = fopen("/Users/hashimototatsuya/Downloads/A-large.in","r");
    OUT = fopen("/Users/hashimototatsuya/Desktop/alarge.txt","w");
    int T;
    fscanf(IN,"%d",&T);
    for (int t = 0; t < T; t++) {
        solve(t);
    }
    fclose(IN);
    fclose(OUT);
    return 0;
}