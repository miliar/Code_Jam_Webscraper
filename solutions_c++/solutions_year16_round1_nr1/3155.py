#include<vector>
#include<stack>
#include<set>
#include<queue>
#include<map>
#include<list>
#include<deque>
#include<iostream>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<algorithm>
#include<bitset>
#include<complex>
#include<functional>
#include<limits>
#include<locale>
#include<numeric>
#include<string>
#include<utility>
#include<climits>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<ctime>

using namespace std;

string last_word(string S){
       
       string res;
       res.push_back(S[0]);
       for(int i=1;i<S.size();++i){
               if(S[i]>=res[0])res.insert(res.begin(),S[i]);
               else res.push_back(S[i]);}
       return res;}
               
              

int main(){
    ifstream infile("A-large.txt");
    ofstream ofile("A-large-output.txt");
    int cases;
    if(infile.is_open()&&ofile.is_open()){
       infile>>cases;
       int curcase=1;
       while(curcase<=cases){
          string S;
          infile>>S;
          string res;
          res=last_word(S);
          ofile<<"Case #"<<curcase<<": "<<res<<endl;
          
          ++curcase;
                         }
           }
       infile.close();
       ofile.close();
       return 0;}
