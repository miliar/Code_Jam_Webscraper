#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
#include<vector>
#include<utility>
#include<map>
#include<list>
#include<queue>
#include<stack>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<fstream>

using namespace std;



int main()
{


ifstream file;
ofstream out;
file.open("A-small-attempt2.in");
out.open("small_output.txt");
int T;
file>>T;
 for(int t=1 ; t<=T ; t++){
    int ans1 , ans2;
   file>>ans1;
    set<int>result;
   int v1[4][4];
   int v2[4][4];
   for(int i=0 ; i<4 ; i++)
      for(int j=0 ; j<4 ; j++)
	   file>>v1[i][j];
   file>>ans2;
   for(int i=0 ; i<4 ; i++)
      for(int j=0 ; j<4 ; j++)
	   file>>v2[i][j];
   
   for(int i=0 ; i<4 ; i++)
      for(int j=0 ; j<4 ; j++){
         if(v1[ans1-1][i] == v2[ans2-1][j]) 
	         result.insert(v1[ans1-1][i]);
	  }
   out<<"Case #"<<t<<": ";
   if(result.size()==1){
    set<int>::iterator iter=result.begin();
        out<<*iter<<endl;
   }
   else if(result.size()>1)
	 out<<"Bad magician!"<<endl;
   else out<<"Volunteer cheated!"<<endl; 		   
 }


    return 0;
}
