#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<fstream.h>
int comp(int D[102],int S[102],int al,int bl)
{
	int r=1,i;
	if(al<=bl)
	{
		if(al==bl)
		{
			i=0;
			while(i<al)
			{
				if(D[i]==S[i])
					i++;
				else if(D[i]<S[i])
					break;
				else
				{
					r=0;
					break;
				}
			}
		}
	}
	else
		r=0;
	return r;
}
int palindrome_check(int Z[102],int zl)
{
	int r=1,i=0;
	while(i<(zl/2))
	{
		if(Z[i]!=Z[zl-1-i])
		{
			r=0;
			break;
		}
		i++;
	}
	return r;
}
int square_and_palindrome_check(int D[],int dl)
{
	int SR[51],l=1,i,j,k,w,ret,q;
	SR[0]=1;
	k=1;
	while(k<=dl)
	{
		int S[102]={0};
		k=(2*l);
		q=0;
		w=0;
		for(i=l-1;i>=0;i--)
		{
			for(j=l-1;j>=0;j--)
				S[k-w+j-l]+=(SR[j]*SR[i]);
			w++;
		}
		for(i=k-1;i>=1;i--)
		{
			j=S[i]/10;
			S[i]=S[i]%10;
			S[i-1]+=j;
		}
		ret=1;
		if(S[0]==0)
		{
			k--;
			for(i=0;i<k;i++)
				S[i]=S[i+1];
		}
		if(palindrome_check(SR,l)==1 && (dl==k || dl==(k-1)))
		{
			for(i=0;i<k;i++)
			{
				if(D[i]!=S[i])
				{
					ret=0;
					break;
				}
			}
			if(ret==1 && k==dl)
			{
				q=1;
				break;
			}
		}
		SR[l-1]++;
		for(i=l-1;i>0;i--)
		{
			j=SR[i]/10;
			SR[i]=SR[i]%10;
			SR[i-1]+=j;
		}
		if(SR[0]>9)
		{
			for(i=l;i>0;i--)
				SR[i]=SR[i-1];
			SR[0]=SR[1]/10;
			SR[1]=SR[1]%10;
			l++;
		}
	}
	return q;
}
void main()
{
	clrscr();
	char A[102],B[102];
	int D[102],S[102];
	int T,i,al,bl,j,k;
	long int *count;
	ifstream f1;
	f1.open("Code_Jam\\IS3.in");
	ofstream f2;
	f2.open("Code_Jam\\OS3.out");
	f1>>T;
	f1.getline(A,102,'\n');
	count=new long int[T];
	for(i=0;i<T;i++)
	{
		count[i]=0;
		f1.getline(A,102,' ');
		f1.getline(B,102,'\n');
		al=strlen(A);
		bl=strlen(B);
		for(j=0;j<al;j++)
			D[j]=(int(A[j]))-48;
		for(j=0;j<bl;j++)
			S[j]=(int(B[j]))-48;
		while(comp(D,S,al,bl)==1)
		{
			if(palindrome_check(D,al)==1)
			{
				if(square_and_palindrome_check(D,al)==1)
					count[i]++;
			}
			D[al-1]++;
			for(k=al-1;k>0;k--)
			{
				j=D[k]/10;
				D[k]=D[k]%10;
				D[k-1]+=j;
			}
			if(D[0]>9)
			{
				for(k=al;k>0;k--)
					D[k]=D[k-1];
				D[0]=D[1]/10;
				D[1]=D[1]%10;
				al++;
			}
		}
	}
	for(i=0;i<T;i++)
	{
		f2<<"Case #"<<(i+1)<<": "<<count[i]<<"\n";
		cout<<"Case #"<<(i+1)<<": "<<count[i]<<"\n";
	}
	delete []count;
	f1.close();
	f2.close();
	getch();
}