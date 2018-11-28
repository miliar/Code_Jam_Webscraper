#include<iostream>
#include<math.h>
//#include<conio.h>

using namespace std;

int main()
{
	long long T, A, B, req, j, k;
	long double a1, b1;
	cin>>T;
	static long ans[1000];
	long long a[]={1,2,3,11,22};//,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,1211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002	};
	for(int i=0;i<T;i++)
	{
		cin>>A>>B;
		a1=sqrt(A);
		b1=sqrt(B);
		j=0;
		while(j<5 && a[j]<a1)
		{
			j++;
		}
		k=j;
		while(k<5 && a[k]<=b1)
		{
			k++;
		}
		req=k-j;
		ans[i+1]=req;
	}
	for(int h=1;h<=T;h++)
	    cout<<"Case #"<<h<<": "<<ans[h]<<endl;
//	    getch();
}
