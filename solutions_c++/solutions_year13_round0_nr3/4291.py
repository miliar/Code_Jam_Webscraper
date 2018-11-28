#include <iostream>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <sstream>
#include <vector>
using namespace std;
bool isvalid(long long n)
{
        char str[16];
        sprintf(str,"%lld",n);
        int c = strlen(str);
        for(int  i = 0;i<c / 2;i++)
        {
                if(str[i] != str[c - i - 1])
                        return false;
        }
        return true;
}
 
int main()
{
vector<long long> v;
 freopen("src.txt","r",stdin); 
 freopen("out.txt","w",stdout);
 for(long long i=1;i<10000001;++i)
        if(isvalid(i) && isvalid(i*i))
                v.push_back(i*i);
 
 
 long long a,b;
 int n ;cin >> n;
for(int i = 1;i<=n;i++)
 {       cin >> a >>b;
         int counter = 0;
         for(int i = 0;i<v.size();i++)
         {
                 if(v[i] >= a && v[i] <= b)
                         counter++;
         }
         cout << "Case #" <<i<<": "<<counter << endl;
 }
return 0;
}