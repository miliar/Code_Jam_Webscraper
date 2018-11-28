#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <set>
#include <string>
#include <sstream>

using namespace std;

int main(){



ifstream inf;
ofstream fout;



inf.open("a.in");
fout.open("out.txt");
if(!inf.good()){
   cout<<"bad input"<<endl;
   return 0;
   }

int T;
inf>>T;




for(int tt=0;tt<T;tt++){
   int A,N;
   vector<int> motes;

   inf>>A>>N;
   for(int i=0;i<N;++i){
      int temp;
      inf>>temp;
      motes.push_back(temp);
   }
   
   sort(motes.begin(),motes.end());

   bool done = false;
   int added = 0;
   int index = 0;
   // vector # to be able to absorb i
   vector<int> numberAdded;
   for(int i=0;i<N;++i){
      int num=0;
      if(A==1)
         num = 10000;
      else if(A>motes[i])
         num = 0;
      else{
         while(A<=motes[i]){
            num++;
            A+=A-1;
         }

      }

      numberAdded.push_back(num);
      A+=motes[i];
   }

   int total=0;
   int removeIndex = N;
   int numberRemoved = 0;
   for(int i=N-1;i>=0;--i){
      total+=numberAdded[i];
      if(total > removeIndex - i){
         removeIndex = i;
         total = 0;
      }
   }


   fout<<"Case #"<<tt+1<<": "<<total+N-removeIndex<<endl;
}

fout.close();
return 0;
}







