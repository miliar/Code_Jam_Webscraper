#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<utility>
#include<iomanip>
#include<cmath>

using namespace std;

vector<long long> find_pos(int K,int C,int S){
            vector<long long> pos(S,0);
            long long tmp=(long long)pow((double)K,(double)(C-1));
            for(int i=0;i<K;++i){
                    pos[i]=1+tmp*i;}
            return pos;}



int main(){
    ifstream infile("D-small-attempt0.txt");
    ofstream ofile("D-small-output.txt");
    int cases;
    if(infile.is_open()&&ofile.is_open()){
       infile>>cases;
       int curcase=1;
       while(curcase<=cases){
          int K,C,S;
          infile>>K>>C>>S;
          vector<long long> pos(S,0);
          pos=find_pos(K,C,S);
          ofile<<"Case #"<<curcase<<": ";
          for(int i=0;i<S;++i){
                  ofile<<pos[i]<<" ";}
          ofile<<endl;
          ++curcase;
                         }
           }
       infile.close();
       ofile.close();
       return 0;}


