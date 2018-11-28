#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string>
int readIntFromBuffer(char *a, int i, int f, int *end=0)
{
	if(end)*end=-1;
	int n=1;
	int value=0;
	for(int k=i;k<f;k++)
	{
		switch(a[k])
		{
		case '-':
			n*=-1;
			continue;
		case '1':case '2':case '3':case '4':case '5':case '6':case '7':case '8':case '9':case '0':
			{
				int k2=k+1;
				for(;k2<f;k2++)if(a[k2]<'0'||a[k2]>'9')break;
				if(end)*end=k2;
				for(int k3=k;k3<k2;k3++)
				{
					if(a[k3]>='0'&&a[k3]<='9')
					{
						int p=1;
						for(int k4=k2-1;k4>=k;k4--)
						{
							if(a[k4]=='.')continue;
							value+=(a[k4]-'0')*p, p*=10;
						}
						break;
					}
				}
			}
			break;
		default:
			continue;
		}
		break;
	}
	return n*value;
}
void main()
{
	_iobuf *inFile=fopen("D:\\C++\\CJ\\Lawnmower\\B-large.in", "r");
	int alen=0;
	char *a=(char*)malloc(sizeof(char));
	a[0]='\0';
	{
		char temp[1024];
		for(;fgets(temp, 1024, inFile);)
		{
			alen+=strlen(temp), a=(char*)realloc(a, (alen+1)*sizeof(char));
			strcat(a, temp);
		}
	}
	int T=0;
	{
		int k=0;
		T=readIntFromBuffer(a, k, alen, &k);
	}
	std::vector<std::vector<int> > cs;
	std::vector<int> L, M;
	{
		char *temp=strtok(a, "\r\n");
		for(int k=0;k<T;k++)
		{
			temp=strtok(0, "\r\n");
			int k2=0;
			L.push_back(readIntFromBuffer(temp, k2, alen, &k2));
			M.push_back(readIntFromBuffer(temp, k2, alen, &k2));
			cs.push_back(std::vector<int>());
			for(int k3=0;k3<L[k];k3++)
			{
				if(temp=strtok(0, "\r\n"))
				{
					std::string str=temp;
					k2=0;
					for(int k4=0;k4<M[k];k4++)
						cs[k].push_back(readIntFromBuffer((char*)str.c_str(), k2, alen, &k2));
				}
			}
		}
	}
	_iobuf *outFile=fopen("D:\\C++\\CJ\\Lawnmower\\2.out", "w");
	for(int k=0;k<T;k++)
	{
		bool possible=true;
		if(cs[k].size()==L[k]*M[k])
		{
			for(int k2=0;k2<L[k];k2++)
			{
				for(int k3=0;k3<M[k];k3++)
				{
					bool temp=true;
					for(int k4=0;k4<L[k];k4++)if(cs[k][k4*M[k]+k3]>cs[k][k2*M[k]+k3]){temp=false;break;}
					for(int k4=0;k4<M[k];k4++)if(cs[k][k2*M[k]+k4]>cs[k][k2*M[k]+k3]){if(!temp)possible=false;if(!possible)break;}
					if(!possible)break;
				}
				if(!possible)break;
			}
		}
		switch(possible)
		{
		case true:
			fprintf(outFile, "Case #%d: YES\n", k+1);
			break;
		case false:
			fprintf(outFile, "Case #%d: NO\n", k+1);
			break;
		}
	}
	fclose(inFile), fclose(outFile);
}