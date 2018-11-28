#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>


using namespace std;

bool isPalendrome(int a);

int main(){
    fstream in;
    in.open("C-small-attempt0.in");
    ofstream out;
    out.open("output.txt");
    int test;
    in>>test;
    int count=1;
    while(test>0){
                  
          int l,u,result;
          result=0;
          in>>l;
          in>>u;        
          //cout<<l<<" "<<u<<endl;        
          for(int i=l;i<=u;i++){
                  if(isPalendrome(i) && isPalendrome(sqrt(i))){
                        int temp = (int)sqrt(i);
                        if((sqrt(i)-temp)>0){
                                                  
                        } else {             
                        //cout<<i<<" "<<sqrt(i)<<endl;             
                        result++;}                                
                  }       
                  
          }
                  
          out<<"Case #"<<count<<": "<<result<<endl;        
          test--;
          count++;                      
    }
    
    
    
    
    in.close();
    out.close();
    //cout<<sqrt(1)<<endl;
    
    /**/
    //system("pause");
    return 0;    
}


bool isPalendrome(int a){
     
     vector<int> vec;
     int temp = a;
     while(temp!=0){
                 
         vec.push_back(temp%10);
         temp=temp/10;
              
     }
     
     vector<int>::iterator it1;
     vector<int>::iterator it2;
     it1 = vec.begin();
     it2=vec.end();
     it2--;
     while(it1<it2){
                    
            if(*it1!=*it2)
                 return false;
                                        
            it1++;
            it2--;        
     }
          
     return true;     
}































