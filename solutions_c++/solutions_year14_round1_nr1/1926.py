#include <iostream>
#include<math.h>
#include<algorithm>
#include<cstdio>
using namespace std;

int l;

int convert_bin2dec(char * bin_arr) {
    int val = 0;
    for ( int i = 0; i <l; ++i ) {
        val = (val << 1) | ((int)(bin_arr[i]-48));
    }
    return val;
}

int main() {
	int j,x,count,i,k,a1[155],a2[155],w,flag,n,array[45],t;
	char a[155][45],b[155][45],g,temp[155][45] ;
	cin>>t;
	for(w=0;w<t;w++)
	{
		flag=1;
		cin>>n>>l;
		scanf("%c",&g);
		i=0;
		for(k=0;k<n;k++)
		{
			for(j=0;j<l;j++)
			{
				scanf("%c",&a[k][j]);
			}

			a1[k]=convert_bin2dec(a[k]);
			scanf("%c",&g);
		}
		sort(a1,a1+n);
		for(i=n;i<(2*n);i++)
		{
			for(j=0;j<l;j++)
			{
				scanf("%c",&b[i][j]);
			}
			a2[i-n]=convert_bin2dec(b[i]);
			scanf("%c",&g);
		}
		sort(a2,a2+n);
		for(int u=0;u<pow(2,l)-1;u++)
		{
			for (i = 0; i < l; ++i)
			{
			x = u & (1 << i) ? 1 : 0;
			array[i]=x;
			}
			for(i=0;i<n;i++)
			for(j=0;j<l;j++)
			temp[i][j]=a[i][j];
			for(i=0;i<l;i++)
			{
			if(array[i]==1)
			{
				for(j=0;j<n;j++)
				{
					if(temp[j][i]=='0')
					temp[j][i]='1';
					else
					temp[j][i]='0';
					a1[j]=convert_bin2dec(temp[j]);
				}
			}
			}
			/*for(i=0;i<l;i++)
			cout<<array[i];
			cout<<endl;*/
			sort(a1,a1+n);
		/*	for(i=0;i<n;i++)
			cout<<a1[i];
			cout<<endl;
		*/	sort(a2,a2+n);
		/*	for(i=0;i<n;i++)
			cout<<a2[i];
			cout<<endl;
		*/	flag=1;
			for(i=0;i<n;i++)
			{
				//cout<<a1[i];
				//cout<<a2[i];
				if(a1[i]!=a2[i])
				flag=0;
			}
			//cout<<flag<<endl;
			if(flag)
			{
				 count=0;
				for(i=0;i<l;i++)
				{
					if(array[i]==1)
					count++;
				}
				//cout<<count;
				break;
			}
		
		}
		if(flag)
		cout<<"Case #"<<w+1<<": "<<count<<endl;
		//cout<<count<<endl;
		else
		cout<<"Case #"<<w+1<<": "<<"NOT POSSIBLE"<<endl;;
	}	
return 0;
}