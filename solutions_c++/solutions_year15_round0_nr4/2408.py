#include<iostream>
using namespace std;

int main(){
  int T;
  int t=0;
  cin >> T;

  while(t < T){
    int X,R,C;
    bool richard=0; bool gabriel=0;
    cin >> X >> R >> C;

    if(X == 1) gabriel=1;

    if(X == 2) 
      if((R*C % 2) == 0) gabriel=1;
      else richard=1;
      
    
    if(X == 3)
      if((R*C % 3) == 0)
	if(R == 1 || C == 1) richard=1;
	else gabriel=1;
      else richard=1;
    
    if(X == 4)
      if((R*C % 4) == 0){
	if(R == 1 || C == 1) richard=1;
	//else gabriel=1;

	if(R == 2 || C == 2) richard=1;
	//else gabriel=1;	

	if(R == 3)
	  if(C == 4) gabriel=1;	
	  else richard=1;	
	if(C == 3)
	  if(R == 4) gabriel=1;	
	  else richard=1;	

	if(R == 4)
	  if(C == 4) gabriel=1;	
	  else richard=1;
	if(C == 4)
	  if(R == 4) gabriel=1;	
	  else richard=1;		
      }else{
	richard=1;
      }

    if(gabriel==1) cout << "Case #" << t+1 << ": " << "GABRIEL" << endl;
    else if(richard==1) cout << "Case #" << t+1 << ": " << "RICHARD" << endl;

    t++;
  }
}
