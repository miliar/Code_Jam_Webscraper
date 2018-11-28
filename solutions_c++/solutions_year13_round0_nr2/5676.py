#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){
    int T,d1,d2,flag1=0,flag2=0;
    cin>>T;
    
    for(int tc=1;tc<=T;tc++){
      cin >> d1 >> d2;
      int D[d1][d2];
      int D2[d1][d2];
      bool alls[101];
      for(int i=0 ; i<101 ; ++i)
	alls[i] = false;
      
      int max = 1;
      for(int j=0;j<d1;j++)
	for(int k=0;k<d2;k++){
	  cin >> D[j][k];
	  alls[D[j][k]] = true;
	  if(D[j][k] > max)
	      max = D[j][k];
	}
	
      for(int j=0;j<d1;j++)
	for(int k=0;k<d2;k++)
	  D2[j][k] = max;
      
      int p1,p2;
      
      for(int aa=0 ; aa<101 ; ++aa){
	  if(!alls[aa])
	      continue;
	  
	  for(int j=0;j<d1;j++){
	      for(int k=0;k<d2;k++)
		  if(D[j][k] == aa){
		      flag1=0,flag2=0;
		      
		      p1=j;
		      p2=k;
		      for(int l1=0;l1<d2;l1++)
		      if(D[p1][l1]!=aa){
			flag1=1;
			break;
		      }
		      for(int l1=0;l1<d1;l1++)
			if(D[l1][p2]!=aa){
			  flag2=1;
			  break;
			}
		      
		      if(!flag1)
			for(int r=0;r<d2;r++)
			  D2[p1][r] = aa;
		      if(flag2==0)
			for(int r=0;r<d1;r++)
			  D2[r][p2] = aa;
		  }
	  }
      }
      
      int c=0;
      for(int j=0 ; j<d1 ; j++){
	for(int k=0 ; k<d2 ; k++){
	  if(D[j][k] != D2[j][k]){
	    c = 1;
	    break;
	  }
	}
      }

      if(c)
	cout << "Case #" << tc << ": NO" << endl;
      else
	cout << "Case #" << tc << ": YES" << endl;
    }
}