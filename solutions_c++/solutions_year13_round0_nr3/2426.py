#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <sstream>

using namespace std;

vector <long long> hasil;
int t;
long long a, b;

bool palindrom(long long x)
{

     string s;          // string which will contain the result
     ostringstream convert;   // stream used for the conversion
     convert << x;      // insert the textual representation of 'Number' in the characters in the stream
     s = convert.str();
     
     bool bener=true;
     for (int i=0; i<s.size()/2; i++)
     {
         if (s[i] != s[s.size()-1-i])
         {
             bener=false;
             break;
         }
     }
     
     return bener;
     
}

int cari(long long a, long long b)
{
    int p=0;
    for (int i=0; i<hasil.size(); i++)
    {
        if ((hasil[i] >=a) && (hasil[i]<=b)) p+=1;
        if (hasil[i] > b) break;
    }
    
    return p;
}


int main ()
{
    int k=1;
    

    
    for (long long i=1; i<=20002; i++)
    {
        long long z=i*i;
        if (palindrom(z) && (palindrom(i))) {
//           cout <<k << " " << i << " " << z << endl;
            hasil.push_back(z);
            k+=1;

        }
    }    
    
hasil.push_back(404090404LL);
hasil.push_back(10000200001LL);
hasil.push_back(10221412201LL);
hasil.push_back(12102420121LL);
hasil.push_back(12345654321LL);
hasil.push_back(40000800004LL);
hasil.push_back(1000002000001LL);
hasil.push_back(1002003002001LL);
hasil.push_back(1004006004001LL);
hasil.push_back(1020304030201LL);
hasil.push_back(1022325232201LL);
hasil.push_back(1024348434201LL);
hasil.push_back(1210024200121LL);
hasil.push_back(1212225222121LL);
hasil.push_back(1214428244121LL);
hasil.push_back(1232346432321LL);
hasil.push_back(1234567654321LL);
hasil.push_back(4000008000004LL);
hasil.push_back(4004009004004LL);

//cout << hasil.size() << endl;
scanf("%d",&t);
for (int z=1; z<=t; z++)
{
    cin >> a >> b;
    printf("Case #%d: %d\n",z,cari(a,b));
}


//    system("pause");
    return 0;
}
