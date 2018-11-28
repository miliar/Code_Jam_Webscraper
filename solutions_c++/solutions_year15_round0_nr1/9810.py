#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  int t,max,i,sum,count,j;
  char s[1002],y;
    cin>>t;
    
    for(int j=1;j<=t;++j)
        {
        count=0;
        cin>>max;
        y=getchar();
        gets(s);
        
        sum= (int (s[0]))-48;
        
        for(i=1;i<=max;++i)
            {
            if(i>=(sum+count))
            {
                if((int(s[i])-48)>0)
                    count+=i-(sum+count);
            }
            sum=sum+ int(s[i])-48;
        }
        cout<<"Case #"<<j<<": "<<count<<endl;
    }
    
  return 0;
}
