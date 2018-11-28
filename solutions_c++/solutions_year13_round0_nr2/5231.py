#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;

int a[300][300];
int N,M;

bool crow(int num,int i){
     for(int j=0;j<M;j++)
        if(num<a[i][j])
              return false;
     return true;
}

bool ccol(int num,int j){
     for(int i=0;i<N;i++)
         if(num<a[i][j])
               return false;
     return true;
}

void check(){
     for(int i=0;i<N;i++)
        for(int j=0;j<M;j++)
           if(!(crow(a[i][j],i)||ccol(a[i][j],j))){
                cout<<"NO\n";
                return;
           }
     cout<<"YES\n";
}

int main(){
    int T;
    cin>>T;
    int t1=T;
    while(T--){
       cin>>N>>M;
       for(int i=0;i<N;i++){
          for(int j=0;j<M;j++){
                  cin>>a[i][j];
          }
       }
       cout<<"Case #"<<(t1-T)<<": ";
       check();
    }    
    cout<<endl;
    return 0;
}
