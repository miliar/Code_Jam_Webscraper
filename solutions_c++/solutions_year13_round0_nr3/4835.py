#include <iostream>
#include <fstream>
#include<cmath>
#include<string>
#include <sstream>

using namespace std;

string itos(int i){
ostringstream s;
s << i;
return s.str();
}

int stoi(string s){
stringstream str;
int ans;
str << s;
str >>ans;
return ans;
}

string reverse(string str){
   int n;
   n=str.size();
   string ans;
   for(int i=0;i<n;i++){
      ans += str[n-1-i];
   }
  return ans;
}

int Check(int n){
	string str;
   str=itos(n);
   if(str== reverse(str)){return 1;}
   else{return 0;}
}

int main()
{
 FILE *fp;
 errno_t err;
 if((err=fopen_s(&fp,"C-small-attempt0.in","r"))!=0)
 {  printf("入力ファイルが開けません\n");
    return -1;
 }

 ofstream ofs("C-small-answer");

 int T;
 fscanf(fp,"%d",&T);

 int A, B;
 int I;
 int count=0;

 for(int t=0; t<T; t++){
   fscanf(fp,"%d %d", &A,&B);
     I= (int)sqrt(A*1.0) ;
	 count=0;

	for(int i=I; i*i <=B; i++){
		if(i*i <A) continue;
        if(Check(i)==1 && Check(i*i))count++;
	}

	ofs << "Case #" << t+1 << ": " << count<<endl; 
  
 } // T-loop fin

return count;
}