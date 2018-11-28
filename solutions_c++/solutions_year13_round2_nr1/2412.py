#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <math.h>
using namespace std;


long long solve(long long size, vector<int> vec, int b){

    long long count=0;
    for (int i=0;i<vec.size();i++){
        if (size > vec[i]){
           size+=vec[i];         
        }else{
              long long n=1;
              while ((size*pow(2,n)-pow(2,n))<vec[i]){      
              n++;
              }
              long long moves=n;
              //long long moves=ceil(log(vec[i]*1.0/((size-1)*1.0))/log(2)*1.0) ;
              //cout << size << " " << vec[i] << " " <<moves <<" " <<i <<" " << vec.size()<<" "<<b<< " " <<count<< "\n" ; 
              if (moves>= vec.size()-i){return count+ vec.size()-i;}else{
              while(size <= vec[i]){
                        // if(b==9){cout<<" s "<<size <<" "<<vec[i]<<" s ";}
                         size=size+size-1;
                         count+=1;           
              }
              size+=vec[i];          
        }
        
        }
    
    }        
    
    return count;
}



int main(){
ifstream in ("motes.in");
ofstream out ("motes.out");       
int quantity;
in>>quantity;
for (int i=0;i<quantity;i++){
    int motes;
    long long size;
    in>>size>>motes;
    vector<int> vec;
    for (int j=0;j<motes;j++){
        int a;
        in>>a;
        vec.push_back(a);    
    }
    
    sort(vec.begin(),vec.end());
    if (size==1){
       out<<"Case #"<<(i+1)<<": "<<vec.size()<<"\n";             
    }else{
       out<<"Case #"<<(i+1)<<": "<< solve(size,vec,(i+1))<<"\n";    
    }
}






     
   
}
