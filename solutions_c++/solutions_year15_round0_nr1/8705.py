#include<iostream>
#include<fstream>
using namespace std;
 char c[1001];

int main() {
    ifstream in ("a.txt");
    ofstream out ("b.txt");
    int t,n;
    in>>t;

    n=t;
    while(t--)
     {
         int s;
         in>>s;
         in.ignore();
         in>>c[0];
         cout<<c[0]<<endl;
        int sum=0,p=0;
        if(s>0)
        {
        for(int i=1;i<=s;i++)
           {in>>c[i];
           sum+=(c[i-1]-'0');

           if(i-sum>0)
             {p+=i-sum;
              sum+=(i-sum);}

           }
        }
        out<<"Case #"<<n-t<<": "<<p<<"\n";
     }
	return 0;
}
