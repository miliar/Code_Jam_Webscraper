#include<iostream>
#include<map>
#include<sstream>

using namespace std;

map<string,int> inp;
map<string,int>::iterator it;
ostringstream s;

int main(){
  string a;
  int t,i,j,flag;
  scanf("%d",&t);
  for(int zz=1;zz<=t;zz++){
    int ans[10]={0};
    cin>>a;
    printf("Case #%d: ",zz);
    for(i=0;i<a.length();i++){
      s.str("");
      s.clear();
      s<<a[i];
      inp[s.str()]++;
    }
    flag=1;
    while(flag){
      if(inp["S"]&&inp["I"]&&inp["X"]){
        ans[6]++;
        inp["S"]--;
        inp["I"]--;
        inp["X"]--;
      }
      else{
        flag=0;
      }
    }

    flag=1;
    while(flag){
      if(inp["E"]&&inp["H"]&&inp["G"]&&inp["I"]&&inp["T"]){
        ans[8]++;
        inp["T"]--;
        inp["H"]--;
        inp["G"]--;
        inp["E"]--;
        inp["I"]--;
      }
      else{
        flag=0;
      }
    }
    flag=1;
    while(flag){
      if(inp["T"]&&inp["W"]&&inp["O"]){
        ans[2]++;
        inp["T"]--;
        inp["O"]--;
        inp["W"]--;
      }
      else{
        flag=0;
      }
    }

    flag=1;
    while(flag){
      if(inp["Z"]&&inp["R"]&&inp["E"]&&inp["O"]){
        ans[0]++;
        inp["Z"]--;
        inp["E"]--;
        inp["R"]--;
        inp["O"]--;
      }
      else{
        flag=0;
      }
    }
    flag=1;
    while(flag){
      if(inp["F"]&&inp["O"]&&inp["U"]&&inp["R"]){
        ans[4]++;
        inp["F"]--;
        inp["O"]--;
        inp["U"]--;
        inp["R"]--;
      }
      else{
        flag=0;
      }
    }
    flag=1;
    while(flag){
      if(inp["N"]&&inp["O"]&&inp["E"]){
        ans[1]++;
        inp["N"]--;
        inp["O"]--;
        inp["E"]--;
      }
      else{
        flag=0;
      }
    }
    flag=1;
    while(flag){
      if(inp["T"]&&inp["H"]&&inp["R"]&&(inp["E"]>1)){
        ans[3]++;
        inp["T"]--;
        inp["H"]--;
        inp["R"]--;
        inp["E"]-=2;
      }
      else{
        flag=0;
      }
    }
    flag=1;
    while(flag){
      if(inp["S"]&&(inp["E"]>1)&&inp["V"]&&inp["N"]){
        ans[7]++;
        inp["S"]--;
        inp["V"]--;
        inp["N"]--;
        inp["E"]-=2;
      }
      else{
        flag=0;
      }
    }
    flag=1;
    while(flag){
      if(inp["F"]&&inp["I"]&&inp["V"]&&inp["E"]){
        ans[5]++;
        inp["F"]--;
        inp["I"]--;
        inp["V"]--;
        inp["E"]--;
      }
      else{
        flag=0;
      }
    }
 
    flag=1;
    while(flag){
      if((inp["N"]>1)&&inp["I"]&&inp["E"]){
        ans[9]++;
        inp["E"]--;
        inp["N"]-=2;
        inp["I"]--;
      }
      else{
        flag=0;
      }
    }
    for(i=0;i<10;i++){
      for(j=0;j<ans[i];j++){
        cout<<i;
      }
    }
    // for(it=inp.begin();it!=inp.end();it++){
    //cout<<" "<<it->second;
    //}
    inp.clear();
    
    printf("\n");
  }
}
