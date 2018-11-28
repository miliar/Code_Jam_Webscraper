#include<bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long int ll;
typedef unsigned long long int ull;
int main()
{ ofstream myfile("kj.txt");
	ll n,temp,temp2;
	ll t;
	int a=1;
	cin>>t;
	while(t--)
	{

     set<long long int>s;
     cin>>n;
 if(n==0)
            {
                myfile<<"Case #"<<a<<": "<<"INSOMNIA"<<endl;
                a++;
               continue;
            }
     for(int i=1;;i++){

      temp=n*i;
      temp2=temp;
      while(temp2!=0)
      {
      	s.insert(temp2%10);
        temp2/=10;
      }

     if(s.size()==10)
     	break;


}
  myfile<<"Case #"<<a<<": "<<temp<<endl;

a++;
	}



return 0;

}
