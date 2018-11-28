#include <iostream>
#include<fstream>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
	
	freopen("asm.in", "r", stdin);
	freopen("output1.txt", "w", stdout);
	
	int test;
	
	cin >> test;
	for(int z=0;z<test;z++)
		{
		string s;
		cin >> s;
		int a[667],size=0,d[26]={0};d[4]=0;
		for(int i=0;i<s.length();i++)
		{
			char ch=s[i];
			d[(int)(ch)-65]++;
			switch(ch)
			{
				case 'Z':
					a[size]=0;size++;d[4]--;d[14]--;d[17]--;
					break;
				case 'W':
					a[size]=2;size++;d[19]--;d[14]--;
					break;
				case 'U':
					a[size]=4;size++;d[5]--;d[14]--;d[17]--;
					break;
				case 'X':
					a[size]=6;size++;d[8]--;d[18]--;
					break;
				case 'G':
					a[size]=8;size++;d[4]--;d[8]--;d[19]--;d[7]--;
					break;
							
					
			}
		
}
while(d[4]!=0){
		if(d[14]>0 && d[4]>0&& d[13]>0)
			{a[size++]=1;d[14]--;d[4]--;d[13]--;}
		if(d[19]>0 && d[4]>1&& d[17]>0 && d[7]>0)
			{a[size++]=3;d[19]--;d[17]--;d[7]--;
		d[4]-=2;}
		if(d[5]>0 && d[4]>0 && d[8]>0 && d[21]>0)
			{a[size++]=5;d[4]--;d[5]--;d[8]--;d[21]--;}
		if(d[13]>0 && d[4]>1 && d[18]>0 && d[21]>0)
			{a[size++]=7;d[4]-=2;d[13]--;d[18]--;d[21]--;}
		if(d[13]>1 && d[4]>0 && d[8]>0)
			{a[size++]=9;d[13]-=2;d[4]--;d[8]--;}
		
}
	sort(a,a+size);
cout<<"Case #"<<(z+1)<<": ";
		for(int x=0;x<size;x++)
		{
		cout<<a[x];
	}
	cout<<endl;
}
}
