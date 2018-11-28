#include <cstdio>
#include <string>
#include<iostream>
using namespace std;

int main() {
	int I,IT;
    int i,l,k,inc,fr,NA;
    int cad[9000];
    int ban;
    string s;
    freopen("A-large.in","r",stdin);
    freopen("ovalarge.out","w",stdout);
    I=1;
    cin>>IT;
    while(I<=IT){
       cin>>k;
       
       cin>>s;
       for(l=0;l<=k;l++){
          //scanf("%lld", &A[i]);
          cad[l]=(int)s[l]-48;
        //  cout<<"_N"<<l<<":"<<cad[l];
       }
       //cout<<"ban";
       //cin>>ban;
       
       i=0; //NA=0;
       //fr=cad[0] ;
       while(cad[i]==0){
          i++;
       }
       NA=i;
       fr=NA+cad[i];
       i++;
       while(i<=k){
          if(cad[i]>0){
             fr=fr+cad[i];
          }
          else{
             do{
                i++;
             }while(cad[i]==0);
             if(fr>=i){
                
             }
             else{
                inc=i-fr;
                fr=fr+inc;
                NA=NA+inc;
             }
             fr=fr+cad[i];
          }
          i++;
       }
       
   
       cout<<"Case #"<<I<<": "<<NA<<endl;
      
       I++;
    }

	return 0;
}

