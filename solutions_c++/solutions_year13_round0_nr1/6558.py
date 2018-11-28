#include <cstdio>
#include <iostream>
#include <cstring>
#include <fstream>
int n=4, red[5],stupac[5],t,redo[5],stupaco[5],d1,d2,d3,d4,casee;
bool check;
char p[5][5];
FILE *fout= fopen( "izlaz.out","w");

void init() {
     
     casee++;
     d1=d2=d3=d4=0;
    for (int i=0;i<n;i++) scanf("%s",p[i]);
    memset(red,0,sizeof(red));
    memset(stupac,0,sizeof(stupac));
    memset(redo,0,sizeof(red));
    memset(stupaco,0,sizeof(stupac));
    check=false;}
    
    
void solve() {
     init();
     for (int i=0;i<n;i++) {
         for (int j=0;j<n;j++) {
             if (p[i][j]=='X') {
                if (i==j) d1++;
                if (i+j==3) d2++;
                stupac[j]++;
                red[i]++;}
             else if(p[i][j]=='O') {
                  if (i==j) d3++;
                  if (i+j==3) d4++;
                  stupaco[j]++;
                  redo[i]++;}
             else if (p[i][j]=='T') {
                  if (i==j) d1++;
                if (i+j==3) d2++;
                if (i==j) d3++;
                if (i+j==3) d4++;
                  stupac[j]++;
                  red[i]++;
                  stupaco[j]++;
                  redo[i]++;}
             else check=true;}}
     


     for (int i=0;i<n;i++) {
         for(int j=0;j<n;j++) {
                 if (red[i]==4) {fprintf(fout,"Case #%d: X won\n",casee); return;}
                 if (stupac[i]==4) {fprintf(fout,"Case #%d: X won\n",casee); return;}
                 if (redo[i]==4) {fprintf(fout,"Case #%d: O won\n",casee); return;}
                 if (stupaco[i]==4) {fprintf(fout,"Case #%d: O won\n",casee); return;}}}
                 
     if (d1==4) {fprintf(fout,"Case #%d: X won\n",casee); return;}
     if (d2==4) {fprintf(fout,"Case #%d: X won\n",casee); return;}
     if (d3==4) {fprintf(fout,"Case #%d: O won\n",casee); return;}
     if (d4==4) {fprintf(fout,"Case #%d: O won\n",casee); return;}
     
     if (check==true) {fprintf(fout,"Case #%d: Game has not completed\n",casee); return;}
     else {fprintf(fout,"Case #%d: Draw\n",casee); return;}
     }
     
int main() {
    
    scanf("%d",&t);
    while(t--) solve();
    
    return 0;}
