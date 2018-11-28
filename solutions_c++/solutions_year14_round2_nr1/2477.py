#include<iomanip>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<ctype.h>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<fstream>

#define min(a,b) a<b?a:b;

using namespace std;

//ifstream inx("ad.txt");
ofstream onx("o.txt");

string minimal(string a)
{string ans="";
	int i=0;
 while(i<a.size())
 {
	 while(i<a.size()-1 && a[i]==a[i+1])
	 {
		 i++;
	 }
	 ans+=a[i];
     i++;

 }
 return ans;

}
int count(string a,string b)
{   int ans=0;
	
      
  
     int i=0;int j=0;
	 while(1)
	 {int count1=1;int count2=1;

		 
	 while(i<a.length()-1 && a[i]==a[i+1]){count1++; i++;}
	 while(j<b.length()-1 && b[j]==b[j+1]){count2++;j++;}

	// cout<<count1<<count2<<endl;
		 ans+=abs(count2-count1);
		 i++;j++;
		 if(i>=a.length() )break;

	 }
	 return ans;
}
int main()
{
	
	int ntc
		;
	cin>>ntc;
	
	int n;
	string words[100];
	int cas=1;
	while(ntc--)
	{
		cin>>n;

		for(int i=0;i<n;i++)
			cin>>words[i];
          
		int ans=0;
		
		if(n==2)
		  {
			  if(minimal(words[0])!=minimal(words[1]))
			  {ans=-1;
			  }
			  else
				  if(words[0]==words[1])ans=0;
				    else
					  ans= count(words[0],words[1]);
			        
		  }
	/*	onx<<"Case #"<<cas++<<": ";
		//fprintf(onx,"%.7f\n",seconds);
	   //onx << setprecision(7) << std::fixed;
		onx<<  ans << '\n';
	*/
		onx<<"Case #"<<cas++<<": ";
		//fprintf(onx,"%.7f\n",seconds);
	   //onx << setprecision(7) << std::fixed;
		if(ans!=-1)
		onx<<  ans << '\n';
		else
			onx<<"Fegla Won\n";
		  }

}