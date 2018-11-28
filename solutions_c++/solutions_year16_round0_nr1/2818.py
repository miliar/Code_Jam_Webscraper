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

int find_all(int N){
    int inc=1;
    vector<bool> found(10,false);
    int ne=N;
    while(1){
        int tmp=ne;
        while(tmp>0){int pos=tmp%10; found[pos]=true; tmp=tmp/10;}
        int count=0;
        for(int i=0;i<10;++i) if(found[i]) count++;
        if(count==10) return ne;
        inc++;
        ne=inc*N;}
}


int main(){
    ifstream infile("A-large.txt");
    ofstream ofile("A-large-output.txt");
    int cases;
    if(infile.is_open()&&ofile.is_open()){
       infile>>cases;
       int curcase=1;
       while(curcase<=cases){
        int N;
        infile>>N;
        if(N==0) ofile<<"case #"<<curcase<<": "<<"INSOMNIA"<<endl;
        else{ int res=find_all(N);
              ofile<<"case #"<<curcase<<": "<<res<<endl;}
          ++curcase;
                         }
           }
       infile.close();
       ofile.close();
       return 0;}


