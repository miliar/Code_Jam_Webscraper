#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<string>
using namespace std;

#include <unordered_set>


//source here
#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip> 
#include <algorithm>
using namespace std;

int main(){
    ifstream fi("F:/draft/D-small-attempt0.in");
    ofstream fo("F:/draft/D-small-attempt0.out");
    //ifstream fi("F:/draft/in.txt");
    //ofstream fo("F:/draft/out.txt");
    int T=0;
    fi>>T;
    //int A[ ][4]={{1,2,3,4},{1,2,3,4},{1,2,3,4},{1,2,3,4}};
    //int B[ ][4]={{1,2,3,4},{1,2,3,4},{1,2,3,4},{1,2,3,4}};
    vector<double> me(1000,1.0);
    vector<double> him(1000,1.0);
    for(int caseInd=1;caseInd<=T;++caseInd){
        int N;
        fi>>N;
        for(int i=0;i<N;++i){
            fi>>me[i];
        }
        for(int i=0;i<N;++i){
            fi>>him[i];
        }
        sort(me.begin(),me.begin()+N);
        sort(him.begin(),him.begin()+N);
        int numCheat=0;
        int numNoCheat=0;
        int j=N-1;
        for(int i=N-1;i>=0;--i){
            if(me[i]>him[j]){
                ++numNoCheat;
            }else if(me[i]==him[j]){
                ++numNoCheat;
                --j;
                --i;
            }else{
                --j;
            }
        }
        //cheat him
        j=N-1;
        for(int i=N-1;i>=0;--i){
            while(j>=0&&me[i]<=him[j]){
                --j;
            }
            if(j>=0&&me[i]>him[j])
                ++numCheat;
            --j;
        }
        fo<<"Case #"<<caseInd<<": "<<numCheat<<" "<<numNoCheat<<"\n";
    }
   
    
    return 0;
}