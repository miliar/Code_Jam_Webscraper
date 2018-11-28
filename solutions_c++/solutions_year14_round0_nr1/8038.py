#include<algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include<cstring>
#include <sstream>
using namespace std;

int main ()
{
        string s;
	ifstream infile;
	ofstream outfile;
	infile.open ("input.in");
	outfile.open("output.txt");
	int tc;
	 getline(infile,s);
	 tc=stoi(s);
	 //cout<<"tc="<<tc<<endl;
       for(int i=0;i<tc;i++)
       {
    	   getline(infile,s);
    	   int n1=stoi(s);
    	   string s1,s2;
    	   int a[4],b[4];
    	   for(int j=1;j<=4;j++)
    		   {
    		     getline(infile,s);
    		     if(j==n1)
    		    	 s1=s;
    		   }
    	   getline(infile,s);
    	   int n2=stoi(s);
    	   for(int j=1;j<=4;j++)
    	       		   {
    	       		     getline(infile,s);
    	       		     if(j==n2)
    	       		    	 s2=s;
    	       		   }

    	  // cout<<"s1="<<s1<<endl;
    	 // cout<<"s2="<<s2<<endl;

    	   stringstream ss(s1);
    	   ss >> a[0] >> a[1]>> a[2]>>a[3];

    	   stringstream sss(s2);
    	   sss >> b[0] >> b[1]>> b[2]>>b[3];
    	   int count=0,pos=0;
    	   for(int j=0;j<4;j++)
    	   {
    		   for(int k=0;k<4;k++)
    		   if(a[j]==b[k])
    			   {
    			   count++;
    			   pos=j;
    			   }

    	   }
    	   cout<<count<<endl;
    	   if(count==1)
    		   outfile<<"Case #"<<i+1<<": "<<a[pos]<<endl;
    	   else if(count>1)
    		    outfile<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
    	   else
    		   outfile<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;

       }
	infile.close();
	outfile.close();
	return 0;
}




