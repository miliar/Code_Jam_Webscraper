#include<iostream>
#include<math.h>
#include<string.h>
#include<vector>
#include<fstream>
using namespace std;
vector<int> v;
int main()
{

    
    ofstream fout;
    fout.open("B:\\codejam3big.txt");
    long int t;
int k=0;
    unsigned long long l,b,c,i=1,cnt=0,a[50];
a[0] = 1;
a[1] = 4;
a[2] = 9;
a[3] = 121;
a[4] = 484;

    std::cin>>t;
    while(t)
    {std::cin>>l;
     std::cin>>b;
       while(k<5)
    {
     
		
	   c=a[k];
	if(c>=l && c<=b)
        cnt++;
	k++;

    }
    k=0;
    --t;
   
    fout<<"Case #"<<i<<": "<<cnt<<"\n";
        ++i;
    cnt=0;
    }
    fout.close();
}
