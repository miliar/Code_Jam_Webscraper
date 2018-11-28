#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
using namespace std;
int main ()
{
int T,A,B,n;
    ofstream cout ("1.out");
    ifstream cin ("1.in");

int C[5]={1,4,9,121,484};

cin>>T;

for (int i=0;i<T;i++)
{
 n=0;
cin>>A>>B;
for(int j=0;j<5;j++)
{
    if(C[j]<=B&&C[j]>=A)n++;
}
cout<<"Case #"<<i+1<<": "<<n<<endl;

}


cin.close();
cout.close();


   return 0;
}



