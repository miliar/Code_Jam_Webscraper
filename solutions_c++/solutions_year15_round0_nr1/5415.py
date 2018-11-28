#include<iostream>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<sstream>
using namespace std;
int main()
{
 
freopen("A-small-attempt1","r",stdin);
//freopen("out.txt","w",stdout);

 
 int T,fio,cnn=0,result=0;
 string x;
 cin>>T;
 for(int i=0; i<T; i++)
 {
	cin>>fio>>x;
	for(int t=0; t<x.length(); t++)
	{
		int res=0;
		if(t>cnn)
		{
		    result+=t-cnn;
			res=t-cnn;
		}
         cnn+=(int)x[t]-'0'+res;
	}
	 cout<<"Case #"<<i+1<<": "<<result<<endl;
	  result=0,cnn=0;
 }
}