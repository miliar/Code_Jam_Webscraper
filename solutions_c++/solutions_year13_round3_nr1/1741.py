/* 
 * File:   main.cpp
 * Author: tamer
 *
 * Created on April 13, 2013, 2:03 AM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include<math.h>
using namespace std;
typedef std::pair<int, int > mypair;

bool comparator(const mypair& l, const mypair& r) {
    return l.first > r.first;
}

long long solve(char str [], int n, int L) {
    long long res = 0;
    int cons=0;
    for(int len=n;len<L+1;len++){
        for(int b=0;b<L-len+1;b++){
            cons=0;
            //within substring check
            for(int w=b;w<len+b;w++){
                if(str[w]=='o' ||
                        str[w]=='u' ||
                        str[w]=='i' ||
                        str[w]=='e' ||
                        str[w]=='a' ){
                    cons=0;
                }
                else{
                    cons++;
                } 
                
                if(cons>=n)
                    break;
            }
            if(cons>=n)
                res++;
        }
    }
    return res;
   
}

int main(int argc, char** argv) {

    long A, entry, L;
    int m;
    int  N, T;
    char ch[1000001]={'\0'};
       
    long long ans;
    char str [80];
    FILE * pFile;
    FILE * oFile;

    pFile = fopen("/Users/tamer/Desktop/A-small-attempt0.in", "r");
    oFile = fopen("/Users/tamer/Desktop/out.txt", "w+");
    fscanf(pFile, "%d\n", &T);

    for (int t = 1; t <= T; t++) {

//        fscanf(pFile, "%ld %d\n", &A, &N);
//        vector<long> v(N, 0);
        int n=0;
        for (;;) {
            fscanf(pFile, "%c", &ch[n]);
            if(ch[n]==' '){
                ch[n]='\0';
                L=n;
                break;
            }
            n++;
        }
        
        fscanf(pFile, "%d\n", &m);
        for (int i = 0; i < L; i++) {
            cout << ch[i] << " ";
        }
        cout << endl;

        
       ans= solve(ch, m, L);
//        cout << "ans: " << ans << endl;
        fprintf(oFile, "Case #%d: %d", t, ans);
        if (t != T)
            fprintf(oFile, "\n");
    }

    fclose(oFile);
    fclose(pFile);
    return 0;
}
