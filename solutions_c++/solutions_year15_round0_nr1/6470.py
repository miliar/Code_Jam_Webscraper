#include<fstream>
#include<string>
using namespace std;
#define cin fin
#define cout fout
int main()
 {
  int k=0,smax,t,i,total_st,mincount; 
  ifstream fin("Hell.in");
  ofstream fout("out.out");
  string str;
  cin>>t;
  while(k<t)
   {
    cin>>smax>>str;
	total_st=str[0]-'0';
	mincount=0;
	for(i=1;i<=smax;i++)
	 {
	   if(total_st>=i)
	     total_st=total_st+(str[i]-'0');
	   else
		 { 
		  total_st=total_st+(str[i]-'0')+1;
		  mincount++;
		 }
	 }	   
    cout<<"case #"<<(k+1)<<": "<<mincount<<endl;
	str="";
	k++;
   }
  return 0;
 }

