#include <vector>
#include <string.h>
#include <stdint.h>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <bitset>
#include <math.h>



using namespace std;


bool setAllDigitsAndCheck(uint64_t no,bool* ar){
  while(no!=0){
    ar[no%10]=true;
    no=no/10;      
  }
 
  //check for all elements of bool array

  for(uint8_t i=0;i<10;i++){
    if(ar[i]==true)
      continue;
    else
      return false;//if we find some digit not set we return false
  }
  return true;    //this is the no we wanted
}


uint64_t computeSheepSleep(uint32_t inputNo, bool* ar){    
  uint64_t no=inputNo; 

  //Hopefully insomnia test case
  //no mathematical proof so potentally dangerous for lerge data set
  if(no==0)
    return no;

  //@todo infinite loop not good logic
  while(1){
    if(setAllDigitsAndCheck(no,ar)==true)    
      return no;
    else
      no=no+inputNo;   
  }
}


int main(int argc,char**argv){
  
  
  if(argc<2){
    cout<<"Bad Command!! Input File missing! check args"<<std::endl;
    return -1;
  }
  
  std::string inputFile(argv[1]);
  
  ifstream *infile=new ifstream();
  infile->open(inputFile.c_str());

  ofstream myfile;
  myfile.open("output.txt");

  uint16_t test_cases;
  *infile>>test_cases;

  cout<<"No of test cases:"<<test_cases<<endl;

  uint16_t tc = test_cases;
  uint16_t x=1;
  
  bool ar[10];
  
  while(test_cases>0)
    {
  
  
  uint32_t N=0;
  *infile>>N;
    

  cout<<"Number "<<N<<endl;
  
  //clear the array
  for(uint16_t i=0;i<10;i++)
    ar[i]=false;
      
  uint64_t res=computeSheepSleep(N,ar);
  if(res>0)
    myfile<<"Case #"<<x<<": "<<res<<std::endl;
  else
    myfile<<"Case #"<<x<<": "<<"INSOMNIA"<<std::endl;

  x++;
  test_cases--;
}


  
  infile->close();
  myfile.close();


 



#if 0
  cout<<"******* Test case 1 *********"<<endl;

  bool ar[10];

  //clear the array
  for(uint8_t i=0;i<10;i++)
    ar[i]=false;


  //testing: base test  case
  uint32_t x=1234567890;
  cout<<computeSheepSleep(x,ar)<<endl<<endl; 
  
  cout<<endl<<"******* Test case 2 *********"<<endl;

  x=1359;
  //check boolean setting

    //clear the array
  for(uint8_t i=0;i<10;i++)
    ar[i]=false;

  cout<<"Are all elements set: "<<setAllDigitsAndCheck(x,ar)<<endl;
  
  for(uint16_t i=0;i<10;i++)
    cout<<i<<" "<<ar[i]<<endl;

  cout<<endl<<"******* Test case 3 *********"<<endl;

 for(uint8_t i=0;i<10;i++)
    ar[i]=false;
  //testing: inputs
 x=11;
 cout<<computeSheepSleep(x,ar)<<endl<<endl; 
  
  

#endif


  return 0;
}
