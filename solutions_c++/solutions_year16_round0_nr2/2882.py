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

using namespace std;

//void flip(string& S){
     

int Pancake_op(string& S){
    if(S.size()==1) return S[0]=='-'?1:0;
    int result;
    int pos=S.size()-1;
    if(S[pos]=='+'){string tmp=S.substr(0,pos); return Pancake_op(tmp);}
    else if(S[pos]=='-'&&S[0]=='-'){
         string tmp="";
         for(int i=pos;i>=1;--i){
           if(S[i]=='-')tmp=tmp+"+";
           else if(S[i]=='+') tmp=tmp+"-";
           }
         result=1+Pancake_op(tmp);}                      
    else if(S[pos]=='-'&&S[0]=='+'){
         string tmp="";
         int j=0;
         while(S[j]=='+'){S[j]='-';++j;}
          for(int i=pos;i>=1;--i){
           if(S[i]=='-')tmp=tmp+"+";
           else if(S[i]=='+') tmp=tmp+"-";
           }
           result=2+Pancake_op(tmp);}
           
          return result;}
    

int main(){
    ifstream infile("B-large.txt");
    ofstream ofile("B-large-output.txt");
    int cases;
    if(infile.is_open()&&ofile.is_open()){
       infile>>cases;
       int curcase=1;
       while(curcase<=cases){
        string S;
        infile>>S;
        int res=Pancake_op(S);
        ofile<<"case #"<<curcase<<": "<<res<<endl;
          ++curcase;
                         }
           }
       infile.close();
       ofile.close();
       return 0;}


