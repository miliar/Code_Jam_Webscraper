#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

int main(){
     ifstream filein;
     filein.open("A-large.in");
     ofstream fileout;
     fileout.open("A-large.out");
     
     int times;
     int num,temp,digit;
     filein>>times;
     //cout<<times;
     for (int ntimes = 0 ; ntimes < times; ntimes++){
     	 filein>>num;
     
     	 //cout<<"Num is:"<<num<<"   ";
     	 int count[10];
     	 int flag = 0;
     	 memset(count,0,sizeof(int)*10);
     	 int i;
		 for (i = 1 ; i < 1001; ++i){
		     temp = num * i;
		     while( temp > 0){
		     	  digit = temp %10;
		     	  if (count[digit]==0){
		     	  	 count[digit]++;
		     	  	 flag ++;
		     	  }
		          if (flag == 10)
		             break;	
		          temp = (temp-digit)/10;
		     }
     	     if (flag == 10)
     	        break;
     	
         }
         if (flag < 10){
         //	cout<<"INSOMNIA"<<endl;
         	fileout<<"Case #"<<ntimes+1<<": "<<"INSOMNIA"<<endl;
         }
         else{
       //  cout<<i*num<<endl;;
         fileout<<"Case #"<<ntimes+1<<": "<<i*num<<endl;
         }
}
   return 0;
}
