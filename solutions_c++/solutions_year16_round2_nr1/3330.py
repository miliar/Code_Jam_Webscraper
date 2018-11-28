#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <fstream>
#include <map>
#include <algorithm>
#include <cstring>
using namespace std;
bool myfunction (char i,char j) { return (i>j); }

int main() {
  ofstream output;
  output.open("output.txt");
  int t;
  cin >> t;
  for(int ii=1;ii<=t;ii++) {
    string num;
    cin >> num;
    sort(num.begin(),num.end(),myfunction);cout<<num;
    int vnum=0,tnum=0,snum=0,rnum=0,onum=0,nnum=0,numbers[10];
    for(int i=0;i<10;i++){
      numbers[i]=0;
    }

    for(int i=0; i<num.length(); i++) {
      if(num[i]=='Z'){
	numbers[0]++;
      }
      else if(num[i]=='X'){
	numbers[6]++;
      }
      else if(num[i]=='W'){
	numbers[2]++;
      }
      else if(num[i]=='V'){
	vnum++;
      }
      else if(num[i]=='U'){
	numbers[4]++;
      }
      else if(num[i]=='T'){
	tnum++;
      }
      else if(num[i]=='S'){
	snum++;
      }
      else if(num[i]=='R'){
	rnum++;
      }
      else if(num[i]=='O'){
	onum++;
      }
      else if(num[i]=='N'){
	nnum++;
      }
    }

    tnum = tnum - numbers[2];
    snum = snum - numbers[6];
    snum = snum/2;
    numbers[7] = snum;
    rnum = rnum - numbers[0] - numbers[4];
    numbers[3] = rnum;
    tnum = tnum - numbers[3];
    numbers[8] = tnum;
    onum = onum - numbers[0] - numbers[2] - numbers[4];
    numbers[1] = onum;
    nnum = nnum - numbers[7] - numbers[1];
    numbers[9] = nnum;

    output << "Case #" << ii << ": ";
    for(int k=0;k<10;k++) {
      if(numbers[k]>0) {
		for(int l=0;l<numbers[k];l++) {
	  		output<<k;
		}
      }
    }
    output<<endl;
  } 
  return 0;
}
