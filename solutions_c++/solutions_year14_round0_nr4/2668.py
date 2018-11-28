#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<vector>
#include<utility>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<fstream>

using namespace std;



int main()
{


ifstream file;
ofstream out;
file.open("D-large.in");
out.open("large_output.txt");
int T;
file>>T;
 for(int t=1 ; t<=T ; t++){
   
   int n;
   file>>n;
   vector<double>naomi(n,0);
   vector<double>ken(n,0);
    vector<double>v1(n,0);
   vector<double>v2(n,0);
   for(int i=0 ; i<n ; i++)
  	   file>>naomi[i];
   for(int i=0 ; i<n ; i++)
  	   file>>ken[i];
 
  sort(naomi.begin() , naomi.end());  
  sort(ken.begin() , ken.end());
    
	for(int i=0 ; i<n ; i++)
  	   { v1[i]=naomi[i]; v2[i]=ken[i];}
  /*
  cout<<"test : "<<t<<endl;
  for(int i=0 ; i<n ; i++) 
      cout<<naomi[i]<<" ";
      cout<<endl;
  for(int i=0 ; i<n ; i++) 
      cout<<ken[i]<<" ";
      cout<<endl;
  */
  
  int DecitfulWar(0) , HonestWar(0) ;
    if(n==1 && naomi[0]>ken[0]) 
         { DecitfulWar=1; HonestWar=1;}
    if(n==1 && naomi[0]<ken[0]) 
         { DecitfulWar=0; HonestWar=0;}
  
  // Honest War Computation ////////////////////////
    if(n>1){
     int next(0);
      for(int i=n-1 ; i>=0 ; i--){
        bool F(0);
	    int index(0);  
        for(int j=n-1 ; j>=0 ; j--) 
	   	   if( v2[j]>v1[i]  && v2[j]!=-1 )
              {index=j; F=1;}
          
        if(F) v2[index]=-1;
		else {HonestWar++; v2[next]=-1; next++;  }
     }
    }
  
    // DecitfulWar War Computation ////////////////////////
	if(n>1){ 
	  int next=0;
      for(int i=n-1 ; i>=0 ; i--) {
        bool F=false;
        int index(0);
		for(int j=0 ; j<n ; j++) 
		   if( naomi[i] > ken[j] && ken[j]!=-1 )
               {F=1; index=j;}
              
		if(F) { ken[index]=-1;DecitfulWar++;}
	    else {ken[next]=-1; next++;}
 	  }
     } 
   //if(HonestWar==n) DecitfulWar=n;
   // cout<<DecitfulWar<<" "<<HonestWar<<endl;
    //cout<<"-------------------------------------------------------------"<<endl;
    out<<"Case #"<<t<<": "<<DecitfulWar<<" "<<HonestWar<<endl;
   }

 
    return 0;
}
