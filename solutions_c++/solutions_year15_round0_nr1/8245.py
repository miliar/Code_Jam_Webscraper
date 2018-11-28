#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<iostream> 
#include<fstream>

using namespace std;
int check(int *a,int size){
int invite=0,stand,invite_now;
stand=a[0];
for(int i=1;i<size+1;i++){
if(i<=stand)	stand+=a[i];
else {invite_now = i - stand;
      invite += invite_now;
		stand += invite_now + a[i];}
    
}
return invite;
}
  
 
int main() {
		freopen("E:\\codejam\\A-large.in","r",stdin);
		freopen("E:\\codejam\\out1.txt","w",stdout);
	  int tt,smax,ans;
	  char *input1;
	  int *input2;
		cin>>tt;
 
  for (int qq=1;qq<=tt;qq++) {
	
		cin >> smax;
     input1 = new char[smax];
	 input2 = new int[smax];
     for(int i = 0; i < smax+1; i++){
         cin >> input1[i];
		input2[i]=input1[i]-'0';
	 }
		 cout<<"Case #"<<qq<<": "<<check(input2,smax)<<"\n";
		
	 }
	
}

