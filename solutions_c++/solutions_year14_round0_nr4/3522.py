#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>
#include <set>
using namespace std;

void readBlocks(ifstream &in,set<double> &st,int &n){
    for(int j=0;j<n;j++){
        double item=0;
        in>>item;
        st.insert(item);
}
}

int getDpoints(set<double> &nset,set<double> &kset){
    set<double>::iterator itn=nset.begin();
    set<double>::iterator itk=kset.begin();
    int count=0;
    int last=nset.size();
    for(int i=0;i<last;i++){
        if(*itn > *itk){
            count++;
            itn++;
            itk++;
        }
        else{
            itn++;
        }
    }  
    return count;
}

int getOpoints(set<double> &nset,set<double> &kset){
    set<double>::iterator itn=nset.begin();
    set<double>::iterator itk=kset.begin();
    int count=0;
    while(itk!=kset.end()){
        if(*itn<*itk){
            itn++;
            itk++;
        }
        else{
            while(!(*itn<*itk)){
                itk++;
                count++;
            }
        }
    }
    return count;
}

int main(){
ifstream in("D-large.in");
FILE* f=fopen("outL.txt","w");
//read in number of test cases
int tc=0;
in>>tc;
for(int i=1;i<=tc;i++){
int n=0;
in>>n;
set<double> nset,kset;
readBlocks(in,nset,n);
readBlocks(in,kset,n);
int y=getDpoints(nset,kset);
int z=getOpoints(nset,kset);
fprintf(f,"Case #%d: %d %d\n",i,y,z);
}
in.close();
}