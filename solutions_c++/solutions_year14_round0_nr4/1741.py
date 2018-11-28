#include <iostream>
#include <fstream>
#include <utility>
#include <algorithm>
using namespace std;
ifstream inp;
ofstream oup;
bool fn(pair<double,int> a, pair<double,int> b){
     return a.second<b.second;     
}
std::pair<double,int> Ken[1000];
std::pair<double,int> Nao[1000];

int main(){
    inp.open("input4.in");
    oup.open("output4.txt");
    int T;
    inp>>T;
    for (int t=1;t<=T; t++){
        //input
        for (int i=0; i<1000; i++){
            Ken[i].first=0;
            Nao[i].first=0;
            Ken[i].second=i;
            Nao[i].second=i;    
        }
        int N;
        inp>>N;
        for (int i=0; i<N; i++){
            inp>>Nao[i].first;    
        }
        for (int i=0; i<N; i++){
            inp>>Ken[i].first;    
        }
        
        
        //solve DWar
        std::sort(Nao,Nao+N);//increasing
        std::sort(Ken,Ken+N);
        int test=1;
        while(1){
            bool meh=0;
            for (int i=0; i<test; i++){
                if (Nao[N-i-1]<Ken[test-i-1]){
                   meh=1;                       
                }    
            }     
            if (meh==1){
               test--;
               break;            
            }
            else if (test==N){
                 break;     
            }
            else{
                 test++;     
            }     
        } 
        oup<<"Case #"<<t<<": "<<test<<" ";
        
        std::sort(Nao,Nao+N,fn);
        std::sort(Ken,Ken+N,fn);
        //solve War
        std::sort(Nao,Nao+N);//increasing
        std::sort(Ken,Ken+N);
        int win=N;
        int countN=N-1;
        int countK=N-1;
        while (countN>=0){
              if (Ken[countK].first>Nao[countN].first){
                 win--;
                 countN--;
                 countK--;                                         
              }
              else countN--;
              
        }
        oup<<win<<endl;
    
        
            
        
    }
    system("PAUSE");
}
