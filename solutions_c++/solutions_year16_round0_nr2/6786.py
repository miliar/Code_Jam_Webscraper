#include <iostream>
using namespace std;

string funRev(string t,int st,int fin)
{
    char temp;
    int sttemp =st,fintemp = fin;
   while(st<fin)
   {
       temp = t[st];
       t[st]=t[fin];
       t[fin] = temp;
       st++;
       fin--;
   }
   
    for(int i=sttemp;i<=fintemp;i++)
    {
        if(t[i]=='-')
        t[i]='+';
        else
        t[i]='-';
    }
    return t;
}

int main() {
	int T=0;
  int st=0,fin=0,count=0,j=0;
	string s= "";
	int flag=0;
	cin>>T;
	for(int i= 1;i<=T;i++)
	{
	    cin>>s;
	  //  cout<<funRev(s,0,s.length()-1);
	  
	   st=0;fin=0;count=0;j=0;
	  while(1)
	  {
	      j=0;
	      flag =0;
	      while(s[j]=='+' && j<s.length())
	      {
	          flag= 1;
	          s[j]='-';
	          j++;
	         
	      }
	      if(j == s.length())
	      {
	           cout<<"Case #"<<i<<": "<<count<<endl;
	        break;
	      }
	      if(flag == 1)
	      {
	          count++;
	      }
	      fin = j;
	      while(s[fin]=='-' && fin<s.length())
	      {
	          fin++;
	      }

	       fin = fin -1;   

	      
	      s= funRev(s,st,fin);

	      count ++;
	  }
	  
	  
	
	}
	return 0;
}
