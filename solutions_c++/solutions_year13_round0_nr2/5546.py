#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
    ifstream in("B-small-attempt2.in");
    ofstream out("probb.txt");
	int t,d,dd,flag1=0,flag2=0;
    in>>t;
    for(int i=1;i<=t;i++){
      in >> d >> dd;
      int Data[d][dd];
      int D2[d][dd];
      bool all[101];
      for(int i=0 ; i<101 ; ++i)
		all[i] = false;
      int max = 1;
      for(int j=0;j<d;j++)
		for(int k=0;k<dd;k++){
	  		in >> Data[j][k];
	  		all[Data[j][k]] = true;
	  		if(Data[j][k] > max)
	     		 max = Data[j][k];
		}
      for(int j=0;j<d;j++)
			for(int k=0;k<dd;k++)
	  			D2[j][k] = max;
       int pos1,pos2;
       for(int aa=0 ; aa<101 ; ++aa){
		  if(!all[aa])
		      continue;
	  for(int j=0;j<d;j++){
	      for(int k=0;k<dd;k++)
			  if(Data[j][k] == aa){
			      flag1=0,flag2=0;
		    	  pos1=j;
		     	  pos2=k;
		      	for(int l1=0;l1<dd;l1++)
		      		if(Data[pos1][l1]!=aa){
					flag1=1;
					break;
		     	 }
		        for(int l1=0;l1<d;l1++)
				if(Data[l1][pos2]!=aa){
			  		flag2=1;
			  	break;
			}
		    if(!flag1)
				for(int r=0;r<dd;r++)
			 		 D2[pos1][r] = aa;
		     		 if(flag2==0)
						for(int r=0;r<d;r++)
			 				 D2[r][pos2] = aa;
		 				 }
	  		}
      	}
      int c=0;
      for(int j=0 ; j<d ; j++){
			for(int k=0 ; k<dd ; k++){
	  			if(Data[j][k] != D2[j][k]){
	    			c = 1;
	    			break;
	  			}
			}
      }
      if(c)
		out << "Case #" << i << ": NO" << endl;
      else
		out << "Case #" << i << ": YES" << endl;
    }
    return 0;
}
