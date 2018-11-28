#include<iostream>
#include<cstring>

using namespace std;

int main()
{
  
  ios_base::sync_with_stdio(false);
  
  int t;
  
  cin>>t;
  int cs=1;
  while(t--)
  {
    
    cout<<"Case #"<<cs<<": ";
    int Smax;
  string s;
  
    cin>>Smax>>s;
    int score=0,res=0;
    
    for(int i=0;i<Smax+1;i++)
    {
      if(score>=i)
      {
	score+=s[i]-'0';
      }
      else
      {
	res++;
	score ++;
	i--;
      }
    }
    
    cout<<res<<endl;
 cs++;   
  }
  
  return 0;
}