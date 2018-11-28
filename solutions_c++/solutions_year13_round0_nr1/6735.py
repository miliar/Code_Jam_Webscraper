//
//#include<cstdio>
//#include<iostream>
//#include<string.h>
//using namespace std;
//int main()
//{
//	freopen("in1.txt","r",stdin);
//	int it,t,n,m,i,j,k,num;
//	char art[101],mid[21],a[10][21],b[10][21];
//	cin>>t;
//	for(it=1;it<=t;it++)
//	{
//		cin>>n>>m;
//		for(i=0;i<m;i++)
//			cin>>a[i]>>b[i];
//		getchar();
//		gets(art);
//		cout<<"Case #"<<it<<": ";
//		num=0;
//		for(i=0;i<(strlen(art)+1);i++)
//		{
//			if(i==strlen(art)||art[i]==' ')
//			{
//				mid[num]='\0';
//				num=0;
//				for(j=0;j<n-1;j++)
//				{
//					for(k=0;k<m;k++)
//						if(strcmp(mid,a[k])==0)
//						{
//							num++;
//							strcpy(mid,b[k]);
//							break;
//						}
//					if(k==m) 
//					{
//						cout<<mid;
//						break;
//					}
//				}
//				if(j==n-1) cout<<mid;
//				if(art[i]==' ') cout<<' ';
//				num=0;
//				i++;
//			}
//			mid[num++]=art[i];
//		}
//		cout<<endl;
//	}
//    return 0;
//}
#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
char a[5][5],b;
int T,complete,flag,low;
ofstream outfile;
int main()
{
	freopen("A-large.in","r",stdin);
	outfile.open("output.txt");
	cin>>T;
	int num=0;
	while(T--)
	{
		complete=0;
		flag=0;
		int i,j;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
			{
				cin>>a[i][j];
				if(a[i][j]=='.')
					complete=1;
		    }
			low=0;
			while(a[low][low]=='T')
				low++;
			for(i=low+1,j=low+1;i<4,j<4;i++,j++)
			{
				if(a[low][low]=='.')
					break;
				if(a[low][low]==a[i][j])
					continue;
				if(a[i][j]=='T')
					continue;
				break;
			}
			if(i==4)
			{
				flag=1;
				outfile<<"Case #"<<++num<<": "<<a[low][low]<<" won"<<endl;
				continue;
			}
			low=0;
			while(a[3-low][low]=='T')
				low++;
			for(i=low+1;i<4;i++)
			{
				if(a[3-i][i]=='.')
					break;
				if(a[3-low][low]==a[3-i][i])
					continue;
				if(a[3-i][i]=='T')
					continue;
				break;
			}
			if(i==4)
			{
				flag=1;
				outfile<<"Case #"<<++num<<": "<<a[3-low][low]<<" won"<<endl;
				continue;
			}
			for(i=0;i<4;i++)
			{
				low=0;
				while(a[i][low]=='T')
					low++;
				for(j=low+1;j<4;j++)
				{
					if(a[i][low]=='.')
						break;
					if(a[i][low]==a[i][j])
						continue;
					if(a[i][j]=='T')
						continue;
					break;
				}
				if(j==4)
				{
					flag=1;
					outfile<<"Case #"<<++num<<": "<<a[i][low]<<" won"<<endl;
					break;
				}
			}
			if(flag)
				continue;
			for(j=0;j<4;j++)
			{
				low=0;
				while(a[low][j]=='T')
					low++;
				for(i=1;i<4;i++)
				{
					if(a[low][j]=='.')
						break;
					if(a[low][j]==a[i][j])
						continue;
					if(a[i][j]=='T')
						continue;
					break;
				}
				if(i==4)
				{
					flag=1;
					outfile<<"Case #"<<++num<<": "<<a[low][j]<<" won"<<endl;
					break;
				}
			}
			if(!flag&&!complete)
			{
				outfile<<"Case #"<<++num<<": Draw"<<endl;
			}
			if(complete&&!flag)
			{
				outfile<<"Case #"<<++num<<": Game has not completed"<<endl;
			    continue;
			}
	}
}