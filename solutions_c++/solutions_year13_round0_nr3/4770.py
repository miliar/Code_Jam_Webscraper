#include<iostream>
#include<fstream>
#include <cstring>
#include <cmath>
#include <cstdlib>
using namespace std;
char a[100];
bool ishuiwen(int i)
{
	itoa(i,a,10);
	char *p,*q;
	p=a;
	q=p+strlen(a)-1;
	while(q>=p)
	{
		if(*p==*q)
		{
			p++;
			q--;
			continue;
		}
		else return false;
	}
	return true;
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int T;
	cin >> T;
    
	for (int k=1;k<=T;k++)
	{
		int A,B;
		cin>>A>>B;
        int sum=0;
		int start=sqrt(double(A));
		if(start*start<A) start++;
		int end=sqrt(double(B))+1;
		for(int i=start;i<end;i++)
        {
            if (ishuiwen(i)&&ishuiwen(i*i)) {
                sum++;
            }
        }
        cout<<"Case #"<<k<<": "<<sum<<endl;
    
    }
	return 0;
}