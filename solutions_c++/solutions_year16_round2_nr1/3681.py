#include <bits/stdc++.h>
 
using namespace std;
 
int A[26],C[10];
int main()
{
	string l;
	int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
		for(int i=0; i<10;++i)C[i]=0;
		for(int i=0; i<26;++i)A[i]=0;
		cin>>l;
		for(int i=0; i<l.size();++i)
		{
			A[l[i]-'A']++;
			if(l[i]=='W')C[2]++;
			if(l[i]=='Z')C[0]++;
			if(l[i]=='G')C[8]++;
			if(l[i]=='U')C[4]++;
			if(l[i]=='X')C[6]++;
		}
		C[3]=A['T'-'A']-C[2]-C[8];
		C[7]=A['S'-'A']-C[6];
		C[5]=A['V'-'A']-C[7];
		C[9]=A['I'-'A']-C[8]-C[6]-C[5];
		C[1]=A['O'-'A']-C[2]-C[0]-C[4];
		cout<<"Case #" <<t<<": ";
		for(int i=0;i<10;++i)
			while(C[i]--)
				cout<<i;
		cout<<endl;
	}
	return 0;
}