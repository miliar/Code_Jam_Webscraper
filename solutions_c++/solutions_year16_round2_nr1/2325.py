#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;
int main()
{
	int n,f=1,t;
	FILE* fp = fopen("uo.txt","w");
	cin>>t;
	while(t--)
	{
		char a[100001]; int b[31] = {0},c[12]={0};
		cin>>a;
		for(int i=0;a[i]!='\0';i++)
		{
			b[a[i]-65]++;
		}
        c[0]= b[25];b[25]-=c[0];b[14]-=c[0];b[4]-=c[0];b[17]-=c[0];
        c[2] = b[22];b[4]-=c[2];b[14]-=c[2];b[13]-=c[2];
        c[4]=b[20]; b[5]-=c[4];b[14]-=c[4];b[17]-=c[4];
        c[6]=b[23]; b[18]-=c[6];b[8]-=c[6];
        c[8]=b[6]; b[4]-=c[8]; b[8]-=c[8]; b[7]-=c[8]; b[19]-=c[8];
        c[3]=b[17]; b[19]-=c[3];b[7]-=c[3];b[4]-=2*c[3];
        c[1]=b[14]; b[13]-=c[1];b[4]-=c[1];
        c[5]=b[5]; b[8]-=c[5];b[21]-=c[5];b[4]-=c[5];
        c[7]=b[21]; b[18]-=c[7];b[4]-=2*c[7];b[13]-=c[7];
        c[9]=b[8];
        fprintf(fp, "Case #%d: ", f); 
        for(int i=0;i<10;i++)
        {
        	for(int j=0;j<c[i];j++)
        	{
        		cout<<i;
        		fprintf(fp, "%d",i );
        	}
        }
        cout<<endl;
        f++;
        fprintf(fp, "\n" );
	}
	return 0;
}






















