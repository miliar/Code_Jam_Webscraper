#include <iostream>
#include <string>
#include <cstring>
#include <fstream>

using namespace std;

#define cin input
#define cout myfile

char str[1000];

int main(){
    ofstream myfile;
    ifstream input;
    input.open("input.in");
    myfile.open("output.txt");
    
    int T,t,i,len,ans;
    cin>>T;
    for(t=1;t<=T;t++){
               cin>>str;
               len = strlen(str);
               for(ans=0,i=0;i<len && str[i]=='-' ; i++);
               
               if(i!=0)
                         ans = 1;
               
               if(i!=len)          
               {
                  for(i++;i<len;i++)
                   if(str[i-1]=='-' && str[i]=='+' )
                      ans+=2;
                  if(str[len-1]=='-')
                                     ans+=2;               
               }
               cout<<"Case #"<<t<<": "<<ans<<"\n";
    }
    input.close();
    myfile.close();                      
    return 0;
}

