#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <unistd.h>

using namespace std;

map<int,bool> arr;
int tot = 0;

bool addDigits(int number)
{
  int rem = number%10;
  while(number > 0) {
    if(arr[rem] != true) {
       arr[rem] = true;
       tot++;     
    }

  number = number/10;
  rem = number%10;
  }
  //cout<<" tot "<<tot<<"number "<<number<< "\n"; 
 //for(map<int, bool>::iterator elem= arr.begin();elem!=arr.end();elem++ )
 //{
 //          std::cout << elem->first << " " << elem->second <<"\n";
 //} 
  return (tot==10) ; 
}

void print(int count,int output)
{
if(output == -1) {
        cout<<"Case #"<<count<<": INSOMNIA\n";
} else {
cout<<"Case #"<<count<<": "<<output<<"\n";
}
}


void findOutput(int count,int input)
{
 if(input == 0) {
    print(count,-1);
 }
 else {
   int start =1;
   while(1) {
     //usleep(1000000);
     //cout << " start "<<start<<" input "<<input<<"\n";
     int res= start * input;
     bool done = addDigits(res);
     if (done) {
             print(count, res);
             break;
     }else {
        start++;         
     }
   }

 }
}



int main () {
          string line,tmp;
          ifstream myfile ("/Users/johnugeorge/Downloads/A-large.in");
          if (myfile.is_open())
          {
                  getline(myfile,line);
                  int noTestCases =  atoi(line.c_str());
                  {
                    for(int i=0;i<noTestCases;i++)
                    {
                    arr.clear();
                    tot = 0;
                     getline(myfile,tmp); 
                     int input = atoi(tmp.c_str());
                     findOutput(i+1,input); 
                    }
                  }
                  myfile.close();
          }

          else cout << "Unable to open file"; 

          return 0;
}
