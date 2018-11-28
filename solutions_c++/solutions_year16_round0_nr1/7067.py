#include<iostream>
#include<conio.h>
#include<fstream>

using namespace std;
int rai(int,int);
int size(int);

int main()
{
    fstream fin,fout;
    fin.open("Large.in",ios::in);
    fout.open("OutLarge.txt",ios::out);
	int T,N[100],DIGIT,Already[10]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},Step[100];
	fin>>T;
	for(int i=0;i<T;i++)
		fin>>N[i];
	for(int z=0;z<T;z++)
	{
        if(N[z]==0)
        {
                   z++;
                   }    
        
        for(int l=0;l<10;l++)
                Already[l]=-1;
		int sze=size(N[z]);
		int Na,j=0,prev=0;
		next:
		j++;
		Na=N[z]*j;
		sze=size(Na);
		for(int i=0,prev=0;i<sze;i++)
		{
			prev*=10;
			DIGIT=Na/rai(10,sze-i-1)-prev;
			prev+=DIGIT;
			Already[DIGIT]=DIGIT;
		}
		for(int i=0;i<10;i++)
		{
			if(Already[i]!=i)
				goto next;
		}
		Step[z]=Na;
	}
	for(int i=0;i<T;i++)
	{
        if(N[i]==0)
        {
                   fout<<"Case #"<<i+1<<": INSOMNIA"<<endl;    
                   i++;
        }
        fout<<"Case #"<<i+1<<": "<<Step[i]<<endl;
	}
	return 0;
}

int size(int x)
{
	for(int i=1;i;i++)
	{
		if(x/rai(10,i)==0)
		{
			return i;
		}
	}
}

int rai(int A,int B)
{
    int T=1;
    for(int i=0;i<B;i++)
            T*=A;
    return T;
    }
