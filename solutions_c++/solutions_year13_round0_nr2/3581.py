#include<iostream>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>
#include<iomanip>
#include<string>
#include<vector>
using namespace std;
int main()
{
	int inc=1;
	ifstream file("i1.in");
	ofstream file2("o1.txt",ios::trunc);
	string s1;
	getline(file,s1);
	while(!file.eof())
	{
		getline(file,s1,' ');
		int n=atoi(s1.c_str());
		getline(file,s1);
		int m=atoi(s1.c_str());
	
		int h[102][102];
		for(int y=1;y<=n;y++)
		{
		  	
	      for(int z=1;z<m;z++)  
	      {
	      	getline(file,s1,' ');
	      	h[y][z]=atoi(s1.c_str());
	      }
	      getline(file,s1);
	      h[y][m]=atoi(s1.c_str());
	    }
	    
	    int q=1;
	    for(int y=1;y<=n;y++)
		{
		  	
	      for(int z=1;z<=m;z++)  
	      {
	      	int r=0,p=0;
	      for(int x=1;x<=m;x++)
		  {
		  	if(h[y][z]<h[y][x])
		  	{
		  		r=-1;
		  		break;
		  	}
		  	
		  }
		  
		  for(int w=1;w<=n;w++)
		  {
		  	if(h[y][z]<h[w][z])
		  	{
		  		p=-1;
		  		break;
		  	}
		  
		  }
		  if(r==-1&&p==-1)
		  {
		  	q=0;
		  	break;
		  }
		  else
		  {
		  r=0;p=0;
	      }
	    }
	    if(q==0)
	    break;
  	
		  }  	
	    
	    
		file2<<"Case #"<<inc++<<": ";
		if(q==1)
		file2<<"YES";
		else
		file2<<"NO";
		file2<<endl;
	}
}
