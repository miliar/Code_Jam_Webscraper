#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>

#define ll long long

using namespace std;

int main()
{ll t,plus,minus,length,count; 
 string ch;
 ofstream fout;
 ifstream fin;
 fin.open("code_1.txt");
 fout.open("code1");
 if(!fin.is_open())
  {cout<<"lol";return 0;}
  
  fin>>t;
  getline(fin,ch);
  
   for(ll popo=1;popo<=t;popo++)
    { plus=0;minus=0;
	  getline(fin,ch);
	  count=0;
	  
	  ch[ch.size()]=ch[ch.size()-1];
	  
	  for(ll i=0;i<ch.size();i++)
        {if(ch[i]=='+')
          plus++;
            else
              minus++;
          
          if(ch[i]==ch[i+1])
           continue;
          
           
		    if(minus==0)
		      {minus=plus;plus=0;}
		        else
		         {plus=minus;minus=0;}
		    
		    count++;
		      
		  }
		  
		  
		    if(plus==ch.size())
		     fout<<"Case #"<<popo<<": "<<count<<"\n";
		     
		     if(minus==ch.size())
		      fout<<"Case #"<<popo<<": "<<count+1<<"\n";
		      
	}
 		   fin.close();
           fout.close();
		   return 0;		    	
}
