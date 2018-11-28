#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
string found;
string digs[] =  {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int digsize = sizeof(digs)/sizeof(digs[0]);
string origin;
int findDigits(map<char,int> &m, string d);
void addStr(map<char,int> &m, string s);
int removeStr(map<char,int> &m, string s);
bool isMapEmpty(map<char,int> &m, string s){
    for(int j=0;j<s.length();j++)
    	{
    	   if(m[s[j]] != 0) return false;
    	}
    	return true;
}
int main() {
	int t;
	
	map<char,int> m;
	cin>>t;
//	char one[] =
	
	for(int i=1;i<=t;i++){
	    found = "";
	    m.clear();
    	cin>> origin;
    	for(int j=0;j<origin.length();j++)
    	{
    	    m[origin[j]] = m[origin[j]] + 1;
    	    
    	}
    	//cout<<"filled";
    	findDigits(m,"");
    	std::sort(found.begin(), found.end());
    	cout<<"Case #"<<i<<": "<<found<<endl;
    	
	}
	return 0;
}
int findDigits(map<char,int> &m, string d)
{
  /* if(d == "012"){
       for(auto elem : m)
        {
           std::cout << elem.first << " " << elem.second  << "\n";
        }
   } */
   if(isMapEmpty(m,origin))
   {
       found = d;
      // cout<< "found! "<< found<<endl;
       return 1; 
   }
  // cout<<"d "<<d<<endl;
    for(int i=0;i<digsize;i++){
        
        if(removeStr(m,digs[i]) == 1)
        {
            if(findDigits(m,d+std::to_string(i)) == 1)
                return 1;
            addStr(m,digs[i]);
        }
        
    }
    return 0;
}
int removeStr(map<char,int> &m, string s){
    bool good = true;
    for(int j=0;j<s.length();j++){
            if(m.find(s[j]) == m.end() || m[s[j]] == 0 )
            {
                good = false;
              //  cout<<"falsed!"<<endl;
            }
             m[s[j]] =  m[s[j]] - 1;
            if(m[s[j]] == 0)
                m.erase(m[s[j]]);
       // cout<<s[j]<<" "<<m[s[j]]<<endl;
        }
    if(good)
    {
        
        return 1;
    }
    addStr(m,s);
    return 0;
}
void addStr(map<char,int> &m, string s){
    for(int j=0;j<s.length();j++){
             m[s[j]] =  m[s[j]] + 1;
             if(m[s[j]] == 0)
                m.erase(m[s[j]]);
        }
}
