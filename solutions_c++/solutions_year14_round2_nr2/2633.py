#include <iostream>
#include<algorithm>
#include <fstream>

using namespace std;

int main()
{
long long t,a,b,k,i,j,temp2,c=0,n=1;
ifstream ip;
ip.open("input.txt");
ofstream op;
op.open("output.txt");

ip>>t;

while(n<=t){
    ip>>a;ip>>b;ip>>k;
    c=0;
    for(i=0;i<a;i++)
    for(j=0;j<b;j++){
      temp2= i&j;
      if(temp2<k)
        c++;
    }




    op<<"Case #"<<n<<": "<<c<<endl;

 n++;
}

    return 0;
}
