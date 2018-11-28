#include<iostream>
#include<stdio.h>
#include<vector>
#include<set>
#include<string>
#include <sstream>

using namespace std;
long long pow(int a,int b);
string getString(int data,int num);
long long getNum(string data,int num);
int main(){
    FILE *inf, *outf;
    inf=fopen("C-small-attempt1.in","r");
    outf=fopen("C-small-attempt1-result.in","w");
    
    int T;
    vector<int> primelist;
    primelist.push_back(2);
    primelist.push_back(3);
    
    fscanf(inf,"%d",&T);
    for(int i=0;i<T;i++){
            int N,J;
            fscanf(inf,"%d %d",&N,&J);
            fprintf(outf,"Case #%d:\n",i+1);
            for(int ii=5;ii<=65537;ii+=2){
              bool check = true;
              for(int j=0;j<primelist.size();j++){
                if(ii%primelist[j]==0){
                                      check=false;
                                      break;
                }        
              }
              if(check)primelist.push_back(ii);                
            }
            long long startval = pow(2,N-1)+1;
            long long endval = pow(2,N);
            int retcnt = 0;
//            cout<<startval<<endl;            
            for(long long ll = startval; ll<endval; ll=ll+2){
              vector<long long> datalist;
              string nowstring = getString(ll,2);
//              cout<<nowstring<<endl;
              for(int j = 2; j<=10;j++){
                      long long nowval = getNum(nowstring,j);
//                      cout<<"j  "<<j<<"  nowval "<<nowval<<endl;
                      bool check = false;
                      for(int k=0;k<primelist.size();k++){
                              if(nowval>primelist[k]){
                                if(nowval%primelist[k]==0){
                                    check=true;
                                    datalist.push_back(primelist[k]);
                                    break;
                                }
                              }        
                      }
                      if(check==false){
                        datalist.clear();
                        break;
                      }
              }
              if(datalist.size()==9){
                cout<<nowstring<<endl;
                fprintf(outf,"%s",nowstring.c_str());
                for(int kk=0;kk<datalist.size();kk++){
                          fprintf(outf," %d",datalist[kk]);
                }
                fprintf(outf,"\n");
                retcnt++;
                if(retcnt==J)break;                        
              } 
            }  
            
            
    }
    getchar();
}

long long pow(int a,int b){
    long long ret = 1;
    for(int i=0;i<b;i++){
            ret*=a;        
    }
    return ret;
}

string getString(int data,int num){
    std::ostringstream ostr;
    int datadump = data;
    string ret = "";
    int order = 1;
    int nowval = 1;
    while(nowval * num <= datadump){
                 order++;
                 nowval = nowval * num;
    }
//    cout<<"order "<<order<<" , nowval "<<nowval<<endl;
    for(int i=order;i>=1;i--){
            int nowpart = datadump/nowval;
            ostr.str("");
            ostr << nowpart;
            ret = ret + ostr.str();
            datadump = datadump - nowpart*nowval;
            nowval= nowval/ num;                        
    }
    return ret;
}

long long getNum(string data,int num){
    int size = data.size();
    long long order = 1;
    long long ret = 0;
    for(int i=size-1;i>=0;i--){
            int val = data[i]=='1'?1:0;
            ret = ret + val*order;
            order = order*num;         
    }    
    return ret;
}
