#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string>
#include<math.h>
double readDoubleFromBuffer(char *a, int i, int f, int *end=0)
{
	if(end)*end=-1;
	int n=1;
	double value=0;
	if(a)
	{
		for(int k=i;k<f;k++)
		{
			switch(a[k])
			{
			case '-':
				n*=-1;
				continue;
			case '1':case '2':case '3':case '4':case '5':case '6':case '7':case '8':case '9':case '0':case '.':
				{
					int k2=k+1, endValid=0;
					for(;k2<f;k2++)
						if((a[k2]<'0'||a[k2]>'9')&&a[k2]!='.')
						{
							endValid=1;
							break;
						}
					if(!endValid)
						k2=f;
					if(end)*end=k2==f?-1:k2;
					for(int k3=k;k3<k2;k3++)
					{
						if(a[k3]>='0'&&a[k3]<='9')
						{
							double p=1;
							for(int k4=k;k4<k2;k4++)
							{
								if(a[k4]=='.')
								{
									for(int k5=k4+1;k5<k2;k5++)
									{
										if(a[k5]=='.')continue;
										p/=10;
									}
									break;
								}
							}
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
	}
	return n*value;
}
void main()
{
	_iobuf *inFile=fopen("D:\\C++\\CJ\\Bullseye\\A-small-attempt1.in", "r");
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
	int k;
	int T=readDoubleFromBuffer(a, 0, alen, &k);
	std::vector<double> r, t;
	{
		char *temp=strtok(a, "\r\n");
		for(int k=0;k<T;k++)
		{
			std::string str;
			for(int k2=0;k2<4;k2++)
			{
				if(temp=strtok(0, "\r\n"))
				{
					int k3=0;
					r.push_back(readDoubleFromBuffer(temp, k3, strlen(temp), &k3));
					if(k3!=-1)
						t.push_back(readDoubleFromBuffer(temp, k3, strlen(temp), &k3));
				}
			}
		}
	}
	_iobuf *outFile=fopen("D:\\C++\\CJ\\Bullseye\\2.out", "w");
	for(int k=0;k<T;k++)
	{
		double b=2*r[k]-1;
		double y=(-b+sqrt(b*b+8*t[k]))/4;
		double y2=floor(y);
	//	double y2=floor(y==floor(y)?y-1:y);
	//	double y2=floor(y==1?y:y==floor(y)?y-1:y);
		fprintf(outFile, "Case #%d: %d\n", k+1, int(y2));
	//	fprintf(outFile, "Case #%d: %d\n", k+1, int(floor((-(2*r[k]-1)+sqrt((2*r[k]-1)*(2*r[k]-1)+8*t[k]))/4)));
	}
	fclose(inFile), fclose(outFile);
}