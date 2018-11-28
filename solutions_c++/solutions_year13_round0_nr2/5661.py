#include <iostream>
#include <fstream>
#include<string>
using namespace std;
int main(){
    ifstream in("inn.txt");
    ofstream out("out.txt");
    int c,fl1=0,fl2=0;
    in>>c;
    int x,y;
	for(int p=0;p<c;p++)
    {
    in>>x>>y;
    int a[x][y];
    int b[x][y];
    bool aa[101];
    int m = 1;
    for(int i=0 ; i<101 ; ++i)
		aa[i] = false;
	
     for(int k=0;k<x;k++)
      { 
			for(int u=0;u<y;u++)
     		{
					in>>a[k][u];
					aa[b[k][u]] = true;
     				if(a[k][u] > m)
	     				m = a[k][u];
      	    }
      }
	  for(int j=0;j<x;j++)
			for(int k=0;k<y;k++)
	  			b[j][k] = m;
       int pos1,pos2;
       for(int g=0 ; g<101 ; ++g){
		  if(!aa[g])
		      continue;
	  for(int j=0;j<x;j++){
	      for(int k=0;k<y;k++)
			  if(a[j][k] == g){
			      fl1=0,fl2=0;
		    	  pos1=j;
		     	  pos2=k;
		      	for(int l1=0;l1<y;l1++)
		      		if(a[pos1][l1]!=g){
					fl1=1;
					break;
		     	 }
		        for(int l1=0;l1<x;l1++)
				if(a[l1][pos2]!=g){
			  		fl2=1;
			  	break;
			}
		    if(!fl1)
				for(int r=0;r<y;r++)
			 		 b[pos1][r] = g;
		     		 if(fl2==0)
						for(int r=0;r<x;r++)
			 				 b[r][pos2] = g;
		 				 }
	  		}
      	}
      int c=0;
      for(int j=0 ; j<x ; j++){
			for(int k=0 ; k<y ; k++){
	  			if(a[j][k] != b[j][k]){
	    			c = 1;
	    			break;
	  			}
			}
      }
      if(c)
		out << "Case #" << p << ": NO" << endl;
      else
		out << "Case #" << p << ": YES" << endl;
    }
    return 0;
}
