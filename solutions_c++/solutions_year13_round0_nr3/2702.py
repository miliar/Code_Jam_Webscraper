#include<stdio.h>
#include<stdlib.h>
//#include<math.h>
#include<vector>
#include<string>
double readDoubleFromBuffer(char *a, int i, int f, int *end=0)
{
	if(end)*end=-1;
	int n=1;
	double value=0;
	for(__int32 k=i;k<f;k++)
	{
		switch(a[k])
		{
		case '-':
			n*=-1;
			continue;
		case '1':case '2':case '3':case '4':case '5':case '6':case '7':case '8':case '9':case '0':case '.':
			{
				__int32 k2=k+1;
				for(;k2<f;k2++)if((a[k2]<'0'||a[k2]>'9')&&a[k2]!='.')break;
				if(end)*end=k2;
				for(__int32 k3=k;k3<k2;k3++)
				{
					if(a[k3]>='0'&&a[k3]<='9')
					{
						double p=1;
						for(__int32 k4=k;k4<k2;k4++)
						{
							if(a[k4]=='.')
							{
								for(__int32 k5=k4+1;k5<k2;k5++)
								{
									if(a[k5]=='.')continue;
									p/=10;
								}
								break;
							}
						}
						for(__int32 k4=k2-1;k4>=k;k4--)
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
	_iobuf *inFile=fopen("D:\\C++\\CJ\\Fair and square\\C-small-attempt2.in", "r");
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
	std::vector<std::string> A, B;
	std::vector<double> dA, dB;
	{
		char *temp=strtok(a, " \r\n");
		for(int k=0;k<T;k++)
		{
			temp=strtok(0, " \r\n");
			int k2=0;
			A.push_back(std::string(temp));
			dA.push_back(readDoubleFromBuffer(temp, k2, alen, &k2));
			temp=strtok(0, " \r\n");
			k2=0;
			B.push_back(std::string(temp));
			dB.push_back(readDoubleFromBuffer(temp, k2, alen, &k2));
		}
	}
	_iobuf *outFile=fopen("D:\\C++\\CJ\\Fair and square\\2.out", "w");
	char b[128];
	for(int k=0;k<T;k++)
	{
		int fairNsquare=0;
		double i=sqrt(dA[k]), f=sqrt(dB[k]);
		for(double k2=ceil(i);k2*k2<=dB[k];k2++)
		{
			bool palindrome=true;
			int l=sprintf(b, "%ld", long long(k2*k2));
			for(int k3=0;k3<l/2;k3++)if(b[k3]!=b[l-1-k3]){palindrome=false;break;}
			l=sprintf(b, "%ld", long long(k2));
			for(int k3=0;k3<l/2;k3++)if(b[k3]!=b[l-1-k3]){palindrome=false;break;}
			if(palindrome)fairNsquare++;
		}
		fprintf(outFile, "Case #%d: %d\n", k+1, fairNsquare);
	}
	fclose(inFile), fclose(outFile);
}