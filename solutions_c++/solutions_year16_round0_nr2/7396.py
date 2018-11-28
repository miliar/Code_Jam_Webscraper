#include <string>
#include <iostream>

using namespace std;

int main(char* argv[],int argc)
{  int t;string s[100];;  
    cin>>t;
    for(int i=0;i<t;i++)
    {
	cin>>s[i];
	}
	    
    for(int i=0;i<t;i++)
    {	    
      int count1 = 0,count2=0;
      size_t mPos =s[i].find("-+", 0); 
      size_t nPos = s[i].find("+-", 0); 
      while(nPos != string::npos)
      {
        count1++;
        nPos = s[i].find("+-", nPos+1);
      }   
      while(mPos != string::npos)
      {
        count2++;
        mPos = s[i].find("-+", mPos+1);
      }   
      if(s[i][s[i].size()-1]=='-')
       cout<<"Case #"<<i+1<<": "<<count1+count2+1<<"\n";
      else
	   cout<<"Case #"<<i+1<<": "<<count1+count2<<"\n";
    
    }
}
