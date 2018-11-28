#include <iostream>
#include<string.h>
#include<vector>
using namespace std;
void print_vec(const std::vector<char>& vec)
{
    for (auto x: vec) {
         std::cout<< x;
    }
    std::cout << '\n';
}
 
int main() {
    int t,i,j,k,n;
  
    j=0;
cin>>t;
while(t--)
{j++;
  char s[1006];
    cin>>s;
    n=strlen(s);
    
    
     std::vector<char> c;
   
    c.push_back(s[0]);
    for(i=1;i<n;i++)
    {
       if((int)s[i]>=(int)c[0]) 
       {auto it = c.begin();
            c.insert(it,s[i]);
       }
       else
       {
           c.push_back(s[i]);
       }
    
      
    }
    
    
    cout<<"Case #"<<j<<": "; print_vec(c);
}
	return 0;
}

