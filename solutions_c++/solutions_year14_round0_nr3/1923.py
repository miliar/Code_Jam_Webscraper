#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <ctime>
#pragma comment(linker,"/STACK:102400000,102400000")
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>

#define SQR(x) ((x)*(x))
#define rep(i, n) for (int i=0; i<(n); ++i)
#define repd(i,n)  for(int i=1;i<=(n);++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define reps(i, a, b) for (int i=(a); i>=(b); --i)
#define PB push_back
#define MP(A, B) make_pair(A, B)
#define pow2(n) (1<<(n))
#define pi acos(-1)
#define eps 0.00000001
#define lg(n) log10((n)*1.0)
#define MaxN  500010
#define mod 1000000007
#define mod2 1000000009
#define mod3 1000007
#define inf 1000100000
#define inf2 0x7fffffffffffffff
#define ll __int64
#define typed int
using namespace std;
void data(){
   freopen("data.in","r",stdin);
   freopen("data2.out","w",stdout);
}
void pt(){
	printf("Impossible\n"); 
}

char hhhhhhhh[51][51];
void ptmap(int r,int c){
//	 cout<<r<<"  "<<c<<endl;
	 for(int i=0;i<r;i++)
	 { 
	    for(int j=0;j<c;j++)
	       printf("%c",hhhhhhhh[i][j]);
        printf("\n");
	 }
}
void ptmap1(int r,int c){
	 //cout<<r<<"  "<<c<<endl;
	 for(int i=0;i<c;i++)
	 { 
	    for(int j=0;j<r;j++)
	       printf("%c",hhhhhhhh[j][i]);
        printf("\n");
	 }
}
int main(){
	//data();
	int T,t=1;
	cin>>T;
	int R,C,M;
	while(T--){
		cin>>R>>C>>M;
		for(int i=0;i<R;i++)
		for(int j=0;j<C;j++) hhhhhhhh[i][j]='*';
		printf("Case #%d:\n",t++);
		int fg=2;			
	//	if(t==225||t==224) cout<<R<<" "<<C<<endl; 
		if(R < C){ int tp=R;R=C;C=tp; fg=1;}
		if(M==0){
	        for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
			if(i==0&&j==0)hhhhhhhh[i][j]='c';
			else hhhhhhhh[i][j]='.';
		}
		else if(C*R-M==1){
	        for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
			if(i==0&&j==0)hhhhhhhh[i][j]='c';
			else hhhhhhhh[i][j]='*';
		 }
		else if(C==1){
		    	if(R-M<2) fg=0;
				else {
					for(int i=0;i<M;i++)hhhhhhhh[i][0]='*';
					for(int i=0;i<R-M-1;i++)hhhhhhhh[i+M][0]='.';
					hhhhhhhh[R-1][0]='c';
				}	 
		}
		else if(C==2){
	 	     if(R*C-M<4||(R*C-M)%2==1) fg = 0;
	 	     else {
  			      int kk =( R*C - M )/2;
			 	  for(int i=0;i<R;i++)
  			   	  for(int j=0;j<C;j++)
			   	  {
	   		   	   if(j==0&&i==0)hhhhhhhh[i][j]='c';
				   else if(i<kk)hhhhhhhh[i][j]='.';
				   else hhhhhhhh[i][j]='*';     
 		   		   }
             }
	    }
		else if(C==3){
		     if(R*C-M<4) fg=0;
		     else{
                int cnt=R*C-M;
				if(R==3){if(cnt&1) fg=0;
				    else {
				 		for(int i=0;i<R;i++)
  				   		for(int j=0;j<C;j++)
				   	  	{
	   			   	  		if(j==0&&i==0)hhhhhhhh[i][j]='c';
				   			else if(i<2&&j<2)hhhhhhhh[i][j]='.';
				   			else if(cnt>4) {hhhhhhhh[i][j]='.';cnt--;}
				   			else hhhhhhhh[i][j]='*';     
 		   		   		}
             	    }
				}
				else if(R==4){
			        if(cnt==5||cnt==7) fg=0;
			        else if(cnt!=10){
 	  					for(int i=0;i<R;i++)
  			   	  		for(int j=0;j<C;j++)
			   	  		{
	   		   	   			if(j==0&&i==0)hhhhhhhh[i][j]='c';
				   			else if(i<2&&j<2)hhhhhhhh[i][j]='.';
				   		   	else if(cnt>4) {hhhhhhhh[i][j]='.';cnt--;}
				   		  	else hhhhhhhh[i][j]='*';     
 		   		   		}
					}
					else{
						//cout<<"hehe"<<cnt<<endl; 
				        for(int i=0;i<C;i++)
  			   	  		for(int j=0;j<R;j++)
			   	  		{
	   		   	   			if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  	else if(i<2&&j<2)hhhhhhhh[j][i]='.';
				   		  	else if(cnt>4) {hhhhhhhh[j][i]='.';cnt--;}
				   		  	else hhhhhhhh[j][i]='*';     
				   		  	//cout<<i<<" "<<j<<endl;
 		   		   		}
 		   		   	//	ptmap1(R,C);	
					}
				}
				else{
					// cout<<"asd"<<endl;
			        if(cnt==5||cnt==7) fg=0;
			        else if(cnt!=10&&cnt!=13){
 	  					for(int i=0;i<R;i++)
  			   	  		for(int j=0;j<C;j++)
			   	  		{
	   		   	   			if(j==0&&i==0)hhhhhhhh[i][j]='c';
				   		  	else if(i<2&&j<2)hhhhhhhh[i][j]='.';
				   		  	else if(cnt>4) {hhhhhhhh[i][j]='.';cnt--;}
				   		  	else hhhhhhhh[i][j]='*';     
 		   		   		}
					}
					else{
				        for(int i=0;i<C;i++)
  			   	  		for(int j=0;j<R;j++)
			   	  		{
	   		   	   			if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  	else if(i<2&&j<2)hhhhhhhh[j][i]='.';
				   		  	else if(cnt>4) {hhhhhhhh[j][i]='.';cnt--;}
				   		  	else hhhhhhhh[j][i]='*';     
 		   		   		}
					}
				}
			}
		}
		else if(C==4){
	    	int cnt = R*C-M;
			if(cnt<4||cnt==5||cnt==7)  fg=0;
			else if(cnt==9){
			         for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  else if(i<3&&j<3)hhhhhhhh[j][i]='.';
				   		  else hhhhhhhh[j][i]='*';     
 		   		   		 }
		    }
		    else if(cnt==6){
			         for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  else if(i<2&&j<3)hhhhhhhh[j][i]='.';
				   		  else hhhhhhhh[j][i]='*';     
 		   		   		 }		    	 
			}
			else if(R==4){
		    	 
				 if(cnt==13){
	 	         	  for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[i][j]='c';
				   		  
						  else if((i>=2&&j>2)||(i>2&&j>=2))hhhhhhhh[i][j]='*';
				   		  else hhhhhhhh[i][j]='.';     
 		   		   		 }
			    }
			    else{
			        for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  else if(i<2&&j<2)hhhhhhhh[j][i]='.';
				   		  else if(cnt>4) {hhhhhhhh[j][i]='.';cnt--;}
				   		  else hhhhhhhh[j][i]='*';     
 		   		   		 }
				}
			}else{
	        	 if(cnt==13||cnt==15||cnt==17){
			        for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  else if(i<2&&j<2)hhhhhhhh[j][i]='.';
				   		  else if(cnt>4) {hhhhhhhh[j][i]='.';cnt--;}
				   		  else hhhhhhhh[j][i]='*';     
 		   		   		 }
				 }
				 else{
				 	  //cout<<"hehe"<<R<<"  "<<C<<endl;
 	  					 for(int i=0;i<R;i++)
  			   	  		 for(int j=0;j<C;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[i][j]='c';
				   		  else if(i<2&&j<2)hhhhhhhh[i][j]='.';
				   		  else if(cnt>4) {hhhhhhhh[i][j]='.';cnt--;}
				   		  else hhhhhhhh[i][j]='*';     
 		   		   		 }
	 	         } 
			}
		}	
		else{
	    	int cnt=25-M;
			if(cnt<4||cnt==5||cnt==7)  fg=0;
			else if(cnt==9){
			         for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  else if(i<3&&j<3)hhhhhhhh[j][i]='.';
				   		  else hhhhhhhh[j][i]='*';     
 		   		   		 }
		    }
		    else if(cnt<=10){
			         for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  else if(i<2&&j<cnt/2)hhhhhhhh[j][i]='.';
				   		  else hhhhhhhh[j][i]='*';     
 		   		   		 }		    	 
			}
			else if(cnt==11){
			         for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  else if(i<2&&j<4)hhhhhhhh[j][i]='.';
				   		  else if(i==2&&j<3)hhhhhhhh[j][i]='.';
		 				  else hhhhhhhh[j][i]='*';     
 		   		   		 }				    	 
			}
			else if(cnt==16){
			         for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[j][i]='c';
				   		  else if(i<4&&j<4)hhhhhhhh[j][i]='.';
		 				  else hhhhhhhh[j][i]='*';     
 		   		   		 }			 		 
			 }
			 else if(cnt==21){
			         for(int i=0;i<C;i++)
  			   	  		 for(int j=0;j<R;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[i][j]='c';
				   		  else if((i<3)||(i==3&&j<4)||(i==4&&j<2))hhhhhhhh[i][j]='.';
	   					  else hhhhhhhh[i][j]='*';     
 		   		   		 }	 
			}	 
			else{
 	  					 for(int i=0;i<R;i++)
  			   	  		 for(int j=0;j<C;j++)
			   	  		 {
	   		   	   		  if(j==0&&i==0)hhhhhhhh[i][j]='c';
				   		  else if(i<2&&j<2)hhhhhhhh[i][j]='.';
				   		  else if(cnt>4) {hhhhhhhh[i][j]='.';cnt--;}
				   		  else hhhhhhhh[i][j]='*';     
 		   		   		 }		 		 	 
		    }

			    	 
		}
		if(fg==0) pt();
		else if(fg==1) ptmap1(R,C);	
		else ptmap(R,C);   	   
		
	}
	return 0;
}
