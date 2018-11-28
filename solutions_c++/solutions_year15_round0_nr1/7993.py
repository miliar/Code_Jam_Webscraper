#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,i,j=0,l,sum,k,m;
    ifstream f2;
    ofstream f1;
    f1.open("out.txt");
    f2.open("inp.in");
    f2>>t;
    m=1;
    string a;
    while(t--)
    {
    f2>>l>>a;
    j=0;
    sum=0;
    k= a.size();
    for(i=0;i<k;++i)
    {
    	if(a[i]!=0)
    	{
    		if(sum<i)
    		{
    			j+=(i-sum);
    			sum+=(i-sum);
			}
			sum+=(a[i]-'0');
		}
	}
    f1<<"Case #"<<m<<": "<<j<<endl;
    m++;
    }
    f1.close();
    f2.close();
    return 0;
    }
          
        
