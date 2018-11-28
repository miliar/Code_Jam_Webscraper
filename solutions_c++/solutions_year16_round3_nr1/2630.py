#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#define ll long long

using namespace std;

bool compare(const pair<ll,char>&i, const pair<ll,char>&j)
{
    return i.first > j.first;
}

int main()
{ll t,plus,minus,length,count,n,a; 
 char ch;
 
  vector< pair<ll,char> > v;
  ifstream fin;
  ofstream fout;
  fin.open("code_1.txt");
  fout.open("code");
  fin>>t;
  for(ll popo=1;popo<=t;popo++)
   {
    {ch='A';
	 fin>>n;
	  for(ll i=1;i<=n;i++)
	   {fin>>a;
	    v.push_back(make_pair(a,ch));
	    ch++;
	   }
	    
    sort(v.begin(),v.end(),compare);
    fout<<"Case #"<<popo<<": ";
    vector< pair<ll,char> > :: iterator it;
   it=v.begin();
   while(it->first>(it+1)->first)
    {
    	fout<<it->second<<" ";
    	it->first=(it->first)-1;
	}
	
	for(it=v.begin()+2;it!=v.end();it++)
	 {
	 	while(it->first>0)
	 	 {fout<<it->second<<" ";
	 	   it->first=(it->first)-1; 
		 }
	 }
	 
	 it=v.begin();
	 
	 while(it->first>0)
	  {
	  	fout<<it->second<<(it+1)->second<<" ";
	  	it->first=(it->first)-1;
	  	(it+1)->first=(it+1)->first-1;
	  }
	  
	  while(!v.empty())
	   v.pop_back();
	   
	   fout<<"\n";
    }
   }
 return 0;
}

