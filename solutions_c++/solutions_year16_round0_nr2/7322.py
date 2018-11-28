#include<bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long int ll;
typedef unsigned long long int ull;
int main()
{ ofstream myfile("kj.txt");
	ll n,temp,temp2;
	ll t;
	ll cnt=0,cnt1=0;
	int a=1;
	cin>>t;
	while(t--)
	{  cnt1=0;
	cnt=0;
	     string s;
     cin>>s;
       for(int i=0;i<s.length();i++)
       {
           if(s[i]=='-')
          cnt++;
       }
       if(cnt==0){
            myfile<<"Case #"<<a<<": "<<"0"<<endl;
               a++;
               continue;
            }
        for(int i=s.length()-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                cnt1++;
                for(int j=0;j<=i;j++)
                {
                    if(s[j]=='-')
                    s[j]='+';
                    else
                        s[j]='-';

                }



            }

        }

  myfile<<"Case #"<<a<<": "<<cnt1<<endl;
a++;
	}



return 0;

}
