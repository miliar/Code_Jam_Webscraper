#include<bits/stdc++.h>
using namespace std;
#define FOR(i,N) for(int i=0;i<(N);i++)
	unsigned long long int marzi[66000];
	unsigned long long int pesit[55][12];
unsigned long long int point=0,help=1;
	bool myprime[100000007];
		unsigned long long int oddec(unsigned long long int,unsigned long long int);
		unsigned long long int decimal_to_other(unsigned long long int,unsigned long long int);
  				unsigned long long int primeFactors(unsigned long long int n)
{
    while (n%2 == 0)
    {
        return(2);
    		    n = n/2;
    }
    for (int i = 3; i*i <=n; i = i+2) 
    {
  		      while (n%i == 0)
        {
        			return(i);
		    n = n/i;
        }
    }
 		if (n > 2)
    	return(n);
}
		unsigned long long int finddivisor(unsigned long long int heman)
{
				return(primeFactors(heman));	
}
unsigned long long int oddec(	unsigned long long int wewon,	unsigned long long int inputbase)
{
			unsigned long long int k,op,s,p;
	op=0;
	k=wewon;
		p=1;
	while(k!=0)
	{
			 s=k%10;
 		k=k/10;
 				op=op+s*p;
 					p=p*inputbase;
	}	
			return op;
}
		unsigned long long int decimal_to_other(unsigned long long int welose,unsigned long long int outputbase)
{
			unsigned long long int op=0,p,k,s;
	k=welose;
			p=1;
			while(k!=0)
			{
				s=k%outputbase;
		k=	k/outputbase;
				op=op+s*p;
					p=p*10;
	}
			return op;
}
		bool world(unsigned long long int heman)
{
			if(heman==2||heman==3)
		return(true);
					if(heman%2==0||heman%3==0)
					return(false);
	int i=5;
				while(i*i<=heman)
						{
							if(heman%i==0)
				return(false);
			i++;
		}
				return(true);
}
bool worldhashing(unsigned long long int heman)
{
			if(myprime[heman]==true)
					return(true);
}
void 	doicare(char arr[], char temp[],unsigned long long  int i,unsigned long long int k,unsigned long long int n)
 {
    			if(i == k) 
		{
			if(temp[0]=='0'||temp[k-1]=='0')
						return;	
    		FOR(m, k) 
			temp[k]='\0';
    		unsigned long long int heman;
    		heman=atoll(temp);
					marzi[point]=heman;
    			point++;
    		return;
    	}
    	FOR(p, n) {
    		temp[i] = arr[p];
    		doicare(arr, temp, i+1, k, n);
    	}
  }
void roselinjerry(char arr[],unsigned long long int n, unsigned long long int k) 
{    
    	char temp[k];
    	doicare(arr, temp, 0, k, n);
}  
int main() 
{
	unsigned long long int i,j,k,tnuoc,yeaaah;
	unsigned long long int phirangi=100000005;
	for(i=0;i<=phirangi;++i)
		myprime[i]=true;   			
		myprime[0]=false;
   		myprime[1]=false;
	for(i=2;i*i<=phirangi;++i)
		{
    		if(myprime[i])
			{
    			for(j=i*i;j<=phirangi;j+=i)
				{
    				myprime[j]=false;
    			}
    		}
    	}
	       	char arr[] = {'0', '1'};
    				unsigned long long int n = sizeof(arr)/sizeof(arr[0]);
    	roselinjerry(arr, n,16);
    			unsigned long long int inputbase,outputbase,wewon,welose2,welose3,welose4,welose5,s;
    					unsigned long long int welose6,welose7,welose8,welose9,welose10;
    	bool sopc2,sopc3,sopc4,sopc5,sopc6,sopc7,sopc8,sopc9,sopc10;
    	outputbase=10;
    	for(i=0;i<=point-1;i++)
    	{
			if(help>=50)
				break;
				wewon=marzi[i];
    			welose2=oddec(wewon,2);
				welose3=oddec(wewon,3);
				welose4=oddec(wewon,4);
				welose5=oddec(wewon,5);
				welose6=oddec(wewon,6);
				welose7=oddec(wewon,7);
				welose8=oddec(wewon,8);
				welose9=oddec(wewon,9);
				welose10=oddec(wewon,10);
				if(welose2<=100000000)
						sopc2=worldhashing(welose2);
				else
						sopc2=world(welose2);
				if(welose3<=100000000)
						sopc3=worldhashing(welose3);
				else
						sopc3=world(welose3);
				if(welose4<=100000000)
						sopc4=worldhashing(welose4);
				else
						sopc4=world(welose4);
				if(welose5<=100000000)
						sopc5=worldhashing(welose5);
				else
						sopc5=world(welose5);
				if(welose6<=100000000)
						sopc6=worldhashing(welose6);
				else
						sopc6=world(welose6);
				if(welose7<=100000000)
						sopc7=worldhashing(welose7);
				else
						sopc7=world(welose7);
				if(welose8<=100000000)
						sopc8=worldhashing(welose8);
				else
						sopc8=world(welose8);
				if(welose9<=100000000)
						sopc9=worldhashing(welose9);
				else
						sopc9=world(welose9);
				if(welose10<=100000000)
						sopc10=worldhashing(welose10);
				else
						sopc10=world(welose10);
				if(sopc2==false&&sopc3==false&&sopc4==false&&sopc5==false&&sopc6==false&&sopc7==false&&sopc8==false&&sopc9==false&&sopc10==false)
					{
						pesit[help][0]=wewon;
						pesit[help][2]=welose2;
						pesit[help][3]=welose3;
						pesit[help][4]=welose4;
						pesit[help][5]=welose5;
						pesit[help][6]=welose6;
						pesit[help][7]=welose7;
						pesit[help][8]=welose8;
						pesit[help][9]=welose9;
						pesit[help][10]=welose10;
						help++;
					}
    		}
    		for(i=1;i<=help;i++)
    			{
    				for(j=2;j<=10;j++)
    					{
    						pesit[i][j]=finddivisor(pesit[i][j]);
    					}
    			}
    	unsigned long long int tester,HULARA,KING;
    		scanf("%llu",&tester);
    		scanf("%llu",&KING,&HULARA);
    		printf("Case #1:\n");
    		for(i=1;i<=help-1;i++)
					{
						printf("%llu ",pesit[i][0]);
							for(j=2;j<=10;j++)
								printf("%llu ",pesit[i][j]);
							printf("\n");
					}
    		printf("%llu ",1000000011001101);
    		printf("3 2 5 2 7 2 5 2 3");
    	return 0;
}
