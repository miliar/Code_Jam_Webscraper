#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
bool check(vector<bool> &v){
     int current=-1; 
     for(int i=0;i<v.size();i++)
    {
            if(v[i]==0)
            current = i;
    }
             if(current == -1)
             return true;
      //cout<<"current "<<current<<endl;
      for(int i=0;i<=current;i++){
              if(v[i]==0){
                          v[i] =1;
              }
              else{
              v[i]=0;
              }
      }
      return false;            
             
}
int main(){
     ifstream fin("B-large.in");
     ofstream fout("output.out");
     int tt;
     fin>>tt;
     string waste;
     getline(fin,waste);
     for(int i=0;i<tt;i++){
             //cout<<"vikash"<<endl;
             vector<bool> v;
             string s;
             getline(fin,s);
             for(int j=0;j<s.size();j++){
                     
                     if(s[j]=='-')
                     v.push_back(0);
                     else{
                     v.push_back(1);
                     }          
             }
            // for(int j=0;j<s.size();j++){
          //           cout<<v[j] << " " <<endl;
             //}
        //     cout<<endl;
             int count=0;
             while(!check(v)){         
                         count++;    
             }
             fout<<"Case #"<<i+1<<": "<<count <<endl;
     }
     system("pause");
}
