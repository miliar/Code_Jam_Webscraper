#include<bits/stdc++.h>
using namespace std;
typedef long long lld;
int main()
{
	lld t,a,ar[10],tmp,i,j,k,count,no;
	FILE *input,*output;
	input=fopen("testcase1.txt","r");
	if(input==NULL)
	{
		printf("ERROR!!");
		exit(0);	
	}
	output=fopen("output1.txt","w");	
	if(output==NULL)
	{
		printf("Error!!");
		exit(0);
	}
	fscanf(input,"%lld",&t);
	for(k=1;k<=t;k++)
	{
		fscanf(input,"%lld",&a);
		if(a==0)
			fprintf(output,"Case #%lld: INSOMNIA\n",k);
		else
		{
			count=0;
			memset(ar,0,sizeof(ar));
			for(i=1;;i++)
			{
				no=a*i;
//				cout<<"no"<<no<<endl;
				while(no)
				{
					tmp=no%10;
					ar[tmp]++;
//					cout<<ar[tmp]<<" "<<tmp<<endl;
					no=no/10;
					if(a==0)
						ar[0]=1;
				}
//				cout<<"s"<<a<<"no"<<no<<endl;
//				cout<<"w";
				count=0;
				for(j=0;j<10;j++)
				{
					if(ar[j]>0)
					{
						count++;
//						cout<<ar[j]<<" ";
					}
				}
				
				
				if(count==10)
					break;
			}
			fprintf(output,"Case #%lld: %lld\n",k,(a*i));
		}
	}
	return 0;
}
