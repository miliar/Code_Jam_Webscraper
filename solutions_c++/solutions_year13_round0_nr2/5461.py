#include <iostream>
using namespace std;

int main(int argc, const char * argv[])
{
	int t,i,j,n,m,k,p=0;
	int A[11][11];
	int h_flag,v_flag,flag;
	FILE* ptr=fopen("sample-3.txt","rt");
	fscanf(ptr,"%d",&t);
	while(t--)
	{
		flag=0;
		p++;
		fscanf(ptr,"%d",&n);
		fscanf(ptr,"%d",&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
				fscanf(ptr,"%d",&A[i][j]);
		}
		// for(i=0;i<n;i++)
		// {
		// 	for(j=0;j<m;j++)
		// 		cout<<A[i][j]<<" ";
		// 	cout<<endl;
		// }
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				h_flag=0;
				v_flag=0;
				if(A[i][j]==1)
				{
					for(k=0;k<m;k++)
					{
						if(A[i][k]!=1)
						{
							h_flag=1;
							break;
						}
					}
						for(k=0;k<n;k++)
						{
							if(A[k][j]!=1)
							{
								v_flag=1;
								break;
							}
						}
					if(h_flag && v_flag)
						flag=1;
				}
				if(flag==1)
					break;
			}
			if(flag==1)
				break;
		}
		if(flag==1)
			cout<<"Case #"<<p<<": NO"<<endl;
		else 
			cout<<"Case #"<<p<<": YES"<<endl;			
	}
    fclose(ptr);
    return 0;
}

