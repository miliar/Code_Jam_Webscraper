#include<fstream>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>


using namespace std;

bool check(int i, int count[], string bb[])
{ string s=bb[i];
  int temp[26];;
  for(i=0;i<26;i++) temp[i]=count[i];
  
  for(i=0;i<s.size();i++)
   {
     if(temp[s[i]-'A']<=0) return false;
     temp[s[i]-'A']--;
   }
   return true;
}

void decrease(int i, int count[], string bb[])
{ string s=bb[i];
  for(i=0;i<s.size();i++)
   count[s[i]-'A']--;
}

void increase(int i, int count[], string bb[])
{ string s=bb[i];
  for(i=0;i<s.size();i++)
   count[s[i]-'A']++;
}

void gen(string &res, int count[], int len, int start, string bb[], bool &have)
{  //cout<<res<<" "<<start<<" "<<len<<endl;
   if(have) return;
   int i=start;
   for(;i<10;)
    { if(check(i,count,bb))
 	    { decrease(i,count,bb); len-=bb[i].size();
 	      res.push_back('0'+i);
 	    }
 	   else i++;
    }
    int a;
   // cout<<len<<" "<<res<<endl;
    if(len!=0) 
	{ 
	  a=res.back()-'0'; res.pop_back(); // cout<<"*"<<a<<endl;
      increase(a,count,bb); len+=bb[a].size();  gen(res,count,len,a+1,bb,have);
    }
    else { have=true; return;}
	
}


string solve(string s, string bb[])
 {  int count[26]={0};
    string res;
    int i;
    int n=s.size();
    for(i=0;i<n;i++)
     { count[s[i]-'A']++;
     }
 	/* char x;
 	 for(i=0;i<26;i++)
 	  { x=i+'A';
 	   cout<<x<<": "<<count[i]<<endl;
     }*/
    bool have=false;
    gen(res,count,n,0,bb,have);
 	cout<<s<<" "<<res<<endl;
 	 return res;
 }
int main()
{  
  int i,n;
  string s;
  string bb[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
  ofstream output;
  //cout<<solve("SFNSVIREEUXO",bb)<<endl;
  output.open("output3.txt");
  
  ifstream input;
  input.open("A-small-attempt2.in");
  input>>n;
  
  for(i=1;i<=n;i++)
   {  input>>s;
      output<<"Case #"<<i<<": "<<solve(s,bb)<<endl; 
   }
 input.close();
 output.close();
   return 0;
}
