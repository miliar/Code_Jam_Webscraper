#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;


int main() {
    int T,Smax,stand,i,count,l=1;
    string word;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    while(l<=T)
    {
        count=0,stand=0;
        cin>>Smax;
        cin>>word;
        (word[0]== '0')?(count=1,stand=1):stand=(word[0]-'0');

        for(i=1;i<=Smax;i++)
        {
          if(stand<i)
             count+=i-stand,stand=i+(word[i]-'0');
          else if (stand==i)
                 stand=i+(word[i]-'0');
                else
                  stand+=(word[i]-'0');
        }
        cout<<"Case #"<<l<<":"<<" "<<count<<endl;
        l++;
    }

    return 0;
}
