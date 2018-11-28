
//CODER: Adolfo Ccanto Ad...
#include<iostream>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<algorithm>
#include<sstream>
#include<stack>
#include<math.h>
#include<string>

#define F(i,a,b) for(int i=a;i<b;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define pii pair<int,int>

#define FE(it,sto) for(typeof(sto.begin())it=sto.begin();it!=sto.end();++it)
//UN LIKE :D
using namespace std;
char a[4][4];

bool gano(char x){
 char b[4][4];
 F(i,0,4)F(j,0,4)b[i][j]=a[i][j];
 F(i,0,4)F(j,0,4)if(b[i][j]=='T')b[i][j]=x;
 
 int c=0;
 F(i,0,4)if(b[i][i]==x)c++;      
 if(c==4)return true;
 
 c=0;
 F(i,0,4)if(b[i][4-i-1]==x)c++; 
 if(c==4)return true;
 
 F(i,0,4){
    c=0;
    F(j,0,4)if(b[i][j]==x)c++;
    if(c==4)return true;         
 }
      
 F(j,0,4){
    c=0;
    F(i,0,4)if(b[i][j]==x)c++;
    if(c==4)return true;         
 }
 return false;    
 
}

bool empate(){
  int c=0;   
  F(i,0,4)F(j,0,4)if(a[i][j]=='.')c++;     
  if(c==0)return true;
  return false;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("ou.txt","w",stdout);
    
    int test;
    cin>>test;
    for(int t=1;t<=test;t++){
       
       string s;
       F(i,0,4){
        cin>>s;
        F(j,0,s.size())a[i][j]=s[j]; 
       }    
       cout<<"Case #"<<t<<": ";
       if(gano('X')){
         cout<<"X won"<<endl;
       }
       else if(gano('O')){
                cout<<"O won"<<endl;
            }  
            else if(empate()){
                   cout<<"Draw"<<endl;
                 }
                 else{
                   cout<<"Game has not completed"<<endl;
                 }
    }
            
}
