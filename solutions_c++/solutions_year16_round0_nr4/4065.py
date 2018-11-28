#include<stdlib.h>
#include<stdio.h>
#include<fstream>


using namespace std;



int main(){
ifstream in; ofstream out;
in.open("D-small-attempt0.in"); out.open("Fractiles.out");
out.clear();

int t,k,c,s,z,stop;

in>>t;

for(int j=1;j<=t;j++){ 
   in>>k>>c>>s; 
   z=k/2;  
   
   if(k%2==0) stop=z;
   else   stop=z+1;
   if(c==1) stop=k;
   
   if(s<stop) {
   	  out<<"Case #"<<j<<": IMPOSSIBLE"<<endl;
   }
   
   else if (c==1){
   	   out<<"Case #"<<j<<": ";
	   for(int i=1;i<=stop;i++)
	      out<<i<<" ";
	   out<<endl;   
   }
   
   else{
   	  out<<"Case #"<<j<<": ";   	  
   	  for(int i=0;i<=stop-1;i++)
   	      out<<i*k+z+(i+1)<<" ";
   	  out<<endl; 
   }
   
}



	
return 0;	
}
