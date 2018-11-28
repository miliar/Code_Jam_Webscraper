//Charging.cpp

#include <iostream>
#include <cstdlib>
#include <bitset>
#include <cstring>
#define clear() cout<< "\033[H\033[J"
using namespace std;


class Util{
	private:
		int  Smx    ;
		 
		char *strSmax;   
		 
		 
	public:
		void   scanArray();
		void  getResult(int);
		bool findOutfromIn(int *);
		 
 };



 

void Util::   scanArray( ){
			
			std::cin>>Smx ;	
			strSmax=(char*)malloc(sizeof(char*)*(Smx+1));
			std::cin>>strSmax ;
			 
 			
	
	}


void Util::getResult(int t){
	
	int numoffrnd=0;
	int S=0;
	for(int i=0;i<Smx+1;i++){

		if((strSmax[i]-48)>0)
		S+=numoffrnd+	(strSmax[i]-48);
		if(S<i+1){
			numoffrnd+=1;
			//S+=numoffrnd;


		}

	}

	
	 
		std::cout<<"Case #"<<t<<": "<<numoffrnd<<endl;

}


bool Util:: findOutfromIn(int * in){
	

 
	
}

	int main(){

		int T;
		 std::cin>> T;
		  Util util[T];
		 clear();
		 for(int i=0;i<T;i++){
		 
			 util[i].scanArray();
		 
		  
		 }
		 
		 for(int i=0;i<T;i++){
			util[i].getResult(i+1);
			}
		  
	   return 0;

}
