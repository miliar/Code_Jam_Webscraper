#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;


string str;



int modi(int k,int i)
{
	
	int t[11],r[11],f[11],s[11];
	t[2]=0,t[3]=1,t[4]=0,t[5]=1,t[6]=0,t[7]=1,t[8]=0,t[9]=1,t[10]=0;
	r[2]=2,r[3]=0,r[4]=1,r[5]=2,r[6]=0,r[7]=1,r[8]=2,r[9]=0,r[10]=1;
	f[2]=3,f[3]=2,f[4]=4,f[5]=0,f[6]=1,f[7]=3,f[8]=2,f[9]=4,f[10]=0;
	s[2]=2,s[3]=3,s[4]=4,s[5]=5,s[6]=6,s[7]=0,s[8]=1,s[9]=2,s[10]=3;
	if(i==2)
	return t[k];
	if(i==3)
	return r[k];
	if(i==5)
	return f[k];
	if(i==7)
	return s[k];
//	cout<<"entered";
	return 100;

}

long long int factor(long long int a,int k)
{
	long long int i;
	int temp;
	for(i=2;i<=a&&i<10;i++)
	{
		
		
		if(i!=2&&i!=3&&i!=5&&i!=7)
		{
			cout<<":()||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||";
			continue;
		}
		
		
		temp=modi(k,i);
	
		if(temp==100)
		return a;
		if((a%i+temp)%i==0)
		return i;
		
	}
	return a;
}

long long int por(int a,int b)
{
	long long int val=1;
	for(int i=0;i<b;i++)
	val*=a;

	return val;
}


long long int bascal(int base)
{
	long long int val=0;
		for(int k=0;k<16;k++)
		{
			if(str[k]-48)
			val+=por(base,15-k);
		}
	return val;
}


int main()
{
	
	fstream fin,fout;
	fin.open("input.txt",ios::in);
	fout.open("output1.txt",ios::out);
	
	int i[14],t,n,j,k;
	fin>>t>>n>>j;
//	j=0;
	
	fout<<"Case #1:"<<endl;
	
	for(i[1]=48;i[1]<=49;i[1]++)	
		for(i[2]=48;i[2]<=49;i[2]++)	
			for(i[3]=48;i[3]<=49;i[3]++)	
				for(i[4]=48;i[4]<=49;i[4]++)	
					for(i[5]=48;i[5]<=49;i[5]++)	
						for(i[6]=48;i[6]<=49;i[6]++)	
							for(i[7]=48;i[7]<=49;i[7]++)	
								for(i[8]=48;i[8]<=49;i[8]++)	
									for(i[9]=48;i[9]<=49;i[9]++)	
										for(i[10]=48;i[10]<=49;i[10]++)	
											for(i[11]=48;i[11]<=49;i[11]++)	
												for(i[12]=48;i[12]<=49;i[12]++)	
													for(i[13]=48;i[13]<=49;i[13]++)	
														for(i[14]=48;i[14]<=49;i[14]++)	
	
	{
		str="1";
		for(k=1;k<=14;k++)
		str+=i[k];
		str+="1";
//	cout<<str<<endl;
		int flag=0;
		
		long long int base[9];
		for(k=2;k<=10;k++)
		{
			base[k]=bascal(k);
//	cout<<base[k]<<"   ";
		}
		
		for(k=2;k<=10;k++)
		{
			long long int temp;
			temp=factor(base[k],k);
			if(base[k]==temp)
			flag=1;
			else
			base[k]=temp;
		}
//	cout<<"fact done"<<endl;	
		if(flag==1)
		continue;
		else
		{
			fout<<"1000000000000000"<<str<<" ";
			for(k=2;k<=10;k++)
			fout<<base[k]<<" ";
			fout<<endl;
			
			j++;
		}
		
		if(j==500)
		{
			cout<<"done";
			return 0;
		}
		
//	cout<<"      "<<j<<endl;
	}
	








	
	
	cout<<"done";
	return 0;
}
