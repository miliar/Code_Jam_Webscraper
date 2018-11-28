#include<iostream>
#define Si(i) scanf("%d",&i);
#define F first
#define S second

using namespace std;
int ar[106][106];
pair<int ,pair <int,int  > > q[10018], tmp;

int main(){
int tt;
cin>>tt;
int n,m;
for(int ww=1;ww<=tt;ww++){
Si(n);
Si(m);

int pp=0,not_pos=0;


for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
                Si(ar[i][j]);
        
        q[pp].F=ar[i][j];
        q[pp].S.F =i;
        q[pp].S.S =j;
                pp++;
        
                }
                
                }
                
                sort(q,q+pp);
                
for(int p=0;p<pp;p++){
       
       if(ar[ q[p].S.F ] [ q[p].S.S ]==-1)continue;
        
        
       int  mx=-1,flg=0;
        for(int x=0;x<m;x++){
             mx=max( mx,  ar[q[p].S.F][x] );
                
                }
                
                if(mx==ar[ q[p].S.F ] [ q[p].S.S ]){
                           flg=1;
                ar[ q[p].S.F ] [ q[p].S.S ]=-1;
                           
                }
                
                
         mx=-1;
         if(flg==0){
        for(int x=0;x<n;x++){ mx=max( mx,  ar[x][q[p].S.S] ); }
                if(mx==ar[ q[p].S.F ] [ q[p].S.S ]){
                           flg=1;
                ar[ q[p].S.F ] [ q[p].S.S ]=-1;
                
                }          
                }
                
                if(flg==0){not_pos=1; break;}
                
                }
        
        
        if(not_pos==1)cout<<"Case #"<<ww<<": NO\n";
        else cout<<"Case #"<<ww<<": YES\n";
        
        }





} 
    
    
