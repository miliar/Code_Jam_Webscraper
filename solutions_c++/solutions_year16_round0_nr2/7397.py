#include <iostream>
#include<stdint.h>
#include<stdio.h>
#include<string.h>
using namespace std;

int main() {
    long int t,te=0;
    cin>>t;
    do
    {
        cout<<"Case #"<<te+1<<": ";
        char A[110];
        scanf("%s",A);
        char ch=A[0];
        int val=0,i;
        int l=strlen(A);
        if (A[l-1]=='-') val++;
        for (i=1;i<l;i++)
        {
            if (ch!=A[i])
            {
                val++;ch=A[i];
            }
        }
        cout<<val<<endl;
        te++;
    }
    while(te<t);
	return 0;
}
