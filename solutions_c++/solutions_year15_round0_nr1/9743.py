#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	int t,tc;
	cin>>t;
	for(tc=1;tc<=t;tc++)
	{
		int maxshy,i,need=0,sp=0,temp,totneed=0;
		char a[1000];
		cin>>maxshy;
		cin>>a;
		for(i=0;i<=maxshy;i++)
		{
			temp=a[i]-'0';
			if(sp>=i||temp==0)
				sp+=temp;
			else
			{
                  need=i-sp;
              	  totneed+=need;
              	  sp+=temp+need;
			}
		}
		cout<<"Case #"<<tc<<": "<<totneed<<"\n";
		
	}
	return 0;
}