#include <iostream>
#include<stdint.h>
#include<fstream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    ifstream fin;
    fin.open("A-large.in");
	int t,te=0;
	fin>>t;
	do
	{
	    char A[1010];
	    fin>>A;
	    char B[1010],ch=A[0];
	    int l=strlen(A),i,j;
	    for (i=1;i<l;i++)
	    {
	        if (A[i]>ch) ch=A[i];
	    }
	    B[0]='\0';
	    for (i=0;i<l;i++)
	    {
	        if (A[i]==ch || (i!=0 && B[0]!=ch && A[i]>=B[0]))
	        {
	            for (j=i;j>=1;j--)
	            B[j]=B[j-1];
	            B[0]=A[i];
	        }
	        else
	        {
	            B[i]=A[i];
	        }
	    }
	    B[i]='\0';
	    cout<<"Case #"<<te+1<<": ";
	    cout<<B<<endl;
	    te++;
	}
	while(te<t);
	fin.close();
	return 0;
}
