#include<iostream.h> 
#include<fstream.h> 
using namespace std ; 
main(){
	int chs , cases , r,temp , chs2 , counter= 0  ; 
	 
	int  ar1[4] , ar2[4];
	ifstream in ; 
ofstream out ;
in.open("A-small-attempt0.in");
out.open("omer.out");
in >> cases ; 
for(int x = 1 ; x <= cases; x++)
{ temp = 0; 
 counter = 0 ;
in >> r ; 
 
for(int i = 0 ; i < 4 ; i ++ ) 
{for(int j = 0 ; j < 4 ; j ++)
{in >>chs ; 
if(i == r -1)
ar1[j] =  chs ;	
}
}

in >>chs2 ;  
for(int i = 0 ; i<4  ; i++)
{for(int  j = 0 ; j < 4  ; j++ )
   {in >> chs ; 
   if(i == chs2 -1) 
   ar2[j]=chs ; 
   }
}

////// fill 2 is done ; 
for(int i = 0 ; i < 4 ; i ++ )
for(int  j = 0 ; j < 4 ; j++ )
{
	if(ar1[i] == ar2[j])
   {temp = ar1[i];
   counter ++ ; }
 }
if(counter == 1 )
  {
  	out << "Case #"<<x<<": "<<temp<<endl; 
  }
 else if(counter == 0)
   {out<<"Case #"<<x<<": Volunteer cheated!"<<endl; 	
   }
  else out<< "Case #"<<x<<": Bad magician!"<<endl;
  
}
} 