#include <iostream>
#include <cmath>
#include <cstring> 
#include <string>
#include <iomanip>
#include <algorithm>
#include <cstdlib>
#include <ctime>
using namespace std; 

int calculate_y(string name, int n){
   char vow[]= "aeiou";
  // cout<<name<<endl;
   int aij[name.length()];
   for(int i=0;i<name.length();i++) aij[i]=0;
   //int i= strcspn(name.c_str(),vow);
   for(int i=name.length()-1;i>=0;i--){
       if((int(name.length())-i)<n) aij[i]=0;
       else{
            string subname= name.substr(i);
            int j = strcspn(subname.c_str(),vow);
   //         cout << "j "<<j << endl;
            if(j==subname.length()) aij[i]=max(0,j-n+1);
            else if(j+1==subname.length() && j+1<=n) aij[i]=max(0,j-n+1);
            else if(j+1<=n) aij[i]=aij[i+j+1];
            else { aij[i]=(subname.length()-n+1); }
       }
      // cout << "i "<<i<<" aij "<<aij[i]<<endl;
   }
   int result=0;
   for(int i=0;i<name.length();i++) result+=aij[i];
   return result;

}

int main(){
    int cases; 
    cin  >> cases; 

    for(int casnum=1;casnum<=cases;casnum++){
        string name;
        int n;
        cin >> name >> n;
        
        cout<<"Case #"<<casnum<<": "<<calculate_y(name,n);
        cout<<endl;
    }

return 0;
}
