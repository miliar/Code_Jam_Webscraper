#include <iostream>
#include<math.h>
#include<fstream>

using namespace std;
int main(){
ifstream myfile;
myfile.open("input.in");
int test;
myfile>>test;
int a[101];
for(int i=0;i<test;i++){
   cout<<i;
   int shyness;
   myfile>>shyness;
   int output=0;
   int count=0; 
   int input;
   
           //cout<<output;
		   myfile>>input;
	int div=10;
	if(shyness==0){
		output=0;
	}
	else{
	
	for(int l=0;l<shyness-1;l++){
		
		
		div=div*10;
	}
//	cout<<div;
	//if((input/div)==0){
	//	shyness=shyness-1;
	//	count=count+1;
	//	output=output+1;
	//	cout<<"yes";
	//}
	
   for(int j=0;j<=shyness;j++){
           
		   int real;
		  //int result= (input / (int)pow(10, floor(log10(input)) - j)) % 10;
           //cout<<result;
		   int result= input/(pow(10,(shyness-j)));
		   result=result%10;
		   //cout<<result;
		   if(result==0){
		   	
		   }
		   else{
		   
		   if(count>=j){
                count=count+result;
           }
           else{
           output=(j-count)+output;
           count=result+j;
           
           }
      
}
}
}
a[i]=output;
//cout<<a[0]; 
}
ofstream myfile2 ("output.txt");
 for(int k=0;k<test;k++){
    myfile2<<"case"<<" "<<"#"<<k+1<<":"<<" "<<a[k]<<"\n";


}
myfile2.close();
}



