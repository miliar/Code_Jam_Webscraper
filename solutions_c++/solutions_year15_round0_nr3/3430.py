#include <cstdio>
#include <string>
#include<iostream>
using namespace std;
char op(char q1, char q2){
   if(q1=='1'){
      if(q2=='1') return '1';
      if(q2=='i') return 'i';
      if(q2=='j') return 'j';
      if(q2=='k') return 'k';
      if(q2=='a') return 'a';
      if(q2=='b') return 'b';
      if(q2=='c') return 'c';
      if(q2=='m') return 'm';
   }
   if(q1=='i'){
      if(q2=='1') return 'i';
      if(q2=='i') return 'm';
      if(q2=='j') return 'k';
      if(q2=='k') return 'b';
      if(q2=='a') return '1';
      if(q2=='b') return 'c';
      if(q2=='c') return 'j';
      if(q2=='m') return 'a';
   }
   if(q1=='j'){
      if(q2=='1') return 'j';
      if(q2=='i') return 'c';
      if(q2=='j') return 'm';
      if(q2=='k') return 'i';
      if(q2=='a') return 'k';
      if(q2=='b') return '1';
      if(q2=='c') return 'a';
      if(q2=='m') return 'b';
   }
   if(q1=='k'){
      if(q2=='1') return 'k';
      if(q2=='i') return 'j';
      if(q2=='j') return 'a';
      if(q2=='k') return 'm';
      if(q2=='a') return 'b';
      if(q2=='b') return 'i';
      if(q2=='c') return '1';
      if(q2=='m') return 'c';
   }
   if(q1=='a'){
      if(q2=='1') return 'a';
      if(q2=='i') return '1';
      if(q2=='j') return 'c';
      if(q2=='k') return 'j';
      if(q2=='a') return 'm';
      if(q2=='b') return 'k';
      if(q2=='c') return 'b';
      if(q2=='m') return 'i';
   }
   if(q1=='b'){
      if(q2=='1') return 'b';
      if(q2=='i') return 'k';
      if(q2=='j') return '1';
      if(q2=='k') return 'a';
      if(q2=='a') return 'c';
      if(q2=='b') return 'm';
      if(q2=='c') return 'i';
      if(q2=='m') return 'j';
   }
   if(q1=='c'){
      if(q2=='1') return 'c';
      if(q2=='i') return 'b';
      if(q2=='j') return 'i';
      if(q2=='k') return '1';
      if(q2=='a') return 'j';
      if(q2=='b') return 'a';
      if(q2=='c') return 'm';
      if(q2=='m') return 'k';
   }
   if(q1=='m'){
      if(q2=='1') return 'm';
      if(q2=='i') return 'a';
      if(q2=='j') return 'b';
      if(q2=='k') return 'c';
      if(q2=='a') return 'i';
      if(q2=='b') return 'j';
      if(q2=='c') return 'k';
      if(q2=='m') return '1';
   }
   
}
int main() {
	int I,IT;
    int i,l,ll,k,inc,fr,NA;
    //int cad[9000];
    int ban,p,q,exi;
    char L1,L2;
    long L,X,F,LL;
    string s,cad;
    freopen("C-small.in","r",stdin);
    freopen("diso.out","w",stdout);
    I=1;
    cin>>IT;
    while(I<=IT){
       cin>>L>>X;
       F=L*X;
       cin>>s;
       cad=s;
       for(ll=1;ll<X;ll++){
          cad=cad+s;
       }
  
       exi=0;
       L1='1';
       p=0;ban=0;q=F;
       while(p < q && ban==0){
          
          L1=op(L1,cad[p]);
          if(L1=='i'){
          ban=1;
          
          }
          p++;
       }
       if( ban>0 ){
          ban=1;q=F-1; L2='1';        
          while( q > p && ban==1){
             L2=op(cad[q],L2);
        //     cout<<"\nL2: "<<L2<<endl;
             if(L2=='k'){
                ban=2;
             }
             q--;
          }
          
          
       }
       if(ban>=2){
              LL='1';   
          while(p<=q ){
              LL=op(LL,cad[p]);      
              //cout<<"\nLL: "<<LL<<endl;
              
              p++;
          } 
          if(LL=='j'){
              ban=3;
          }         
       
       }
       
       
       if(ban==3) {
         cout<<"Case #"<<I<<": YEs"<<endl;
       }
       else{
        cout<<"Case #"<<I<<": NO"<<endl;
       }
       
       
       I++;
    }

	return 0;
}

