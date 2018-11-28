#include <iostream>
#include <cstring>
using namespace std;

int main() {
    int T,count=0;
    string s;
    cin>>T;
for(int i=1;i<=T;i++)
{  
    cin>>s;
    int moves=0;
    
    for(int k=0;k<s.length()-1;k++) 
    {
        if(s[k]!=s[k+1]) 
        {
           moves++;
        }
    }
        if(s[s.length()-1]=='-')
        {
            moves++;
        }
        cout<<"Case #"<<i<<": "<<moves<<endl;
}
	return 0;
}
