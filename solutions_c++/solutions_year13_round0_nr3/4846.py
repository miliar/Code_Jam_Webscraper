#include <iostream>
using namespace std;

int main(int argc, const char * argv[])
{

	int A[]={1,4,9,121,484};
	int t,k=0,a,b,i,j,count;
	FILE* ptr=fopen("sample-2.txt","rt");
	fscanf(ptr,"%d",&t);
	while(t--)
	{
		k++;
		count=0;
		fscanf(ptr,"%d",&a);
		fscanf(ptr,"%d",&b);
		if(a>484)
			cout<<"Case #"<<k<<": "<<0<<endl;
		else
		{
			for(i=0;i<=4;i++)
			{
				if(a<=A[i]&& A[i]<=b)
					count++;
			}
			cout<<"Case #"<<k<<": "<<count<<endl;
		}		
	}

	fclose(ptr);
    return 0;
}

