#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{  int t,a;
//cin>>t;
//a=t;
ifstream fin;
ofstream fon;
fin.open("B-large.in",ios::in);
fon.open("output",ios::out);
fin>>t;
a=t;

while(t>0)
 {string s;
  //cin>>s;
  fin>>s;
  //int n=0;
  int count=0;
  int n=s.length();
  for(int i=0;i<n-1;i++)
  {
  	if(s[i]!=s[i+1])
  	{ count++;
  	   for(int j=i;j>=0;j--)
  	  s[j]=s[j+1];
  	  
  	   
	  }
	  
	  
  }
  int i=0;
  while(i<n)
 {
    if(s[i]=='-')
	  s[i]='+';
	  else if(s[i]=='+')
	  break;
	  i++;
}
	  if(i>=n)
	  count+=1;
  
  //cout<<"case #"<<a-t+1<<": "<<count;
  fon<<"case #"<<a-t+1<<": "<<count<<"\n";
t--;

}

fon.close();
fin.close();
	return 0;
}
