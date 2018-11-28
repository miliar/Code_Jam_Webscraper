#include<iostream>
using namespace std;
int main()
{int T,S;
cin>>T;
for(int i=1;i<=T;i++)
{cin>>S;
int aud[S+1],num;
cin>>num;
for(int j=S;j>=0;j--)
	{aud[j]=num%10;
	num=num/10;
	}
int fr=0,fl=0;
for(int k=1;k<=S;k++)
	{fl=fr;
	for(int l=0;l<k;l++)
		{fl+=aud[l];
		}
		if(fl<k){fr=fr+(k-fl);}
	}
cout<<"Case #"<<i<<": "<<fr<<endl;

}
return 0;}
