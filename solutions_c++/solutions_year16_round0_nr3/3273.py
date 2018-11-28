#include<bits/stdc++.h>
using namespace std;
unsigned long long int shivang[55][12];
unsigned long long int ind=0,shiv=1;;
unsigned long long int keep[66000];
bool selfish[100000007];
#define FOR(i,N) for(int i=0;i<(N);i++)
unsigned long long int damn(unsigned long long int santa,unsigned long long int inputbase)
{
unsigned long long int k,op,s,p;
op=0;
k=santa;
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
bool checkprimehashing(unsigned long long int num)
{
	if(selfish[num]==true)
		return(true);
}
unsigned long long int hope(unsigned long long int banta,unsigned long long int outputbase)
{
unsigned long long int op=0,p,k,s;
k=banta;
p=1;
while(k!=0)
{
s=k%outputbase;
k=k/outputbase;
op=op+s*p;
p=p*10;
}
return op;
}
bool peepli(unsigned long long int num)
{
	if(num==2||num==3)
		return(true);
	if(num%2==0||num%3==0)
		return(false);
	int i=5;	
	while(i*i<=num)
		{
			if(num%i==0)
				return(false);
			i++;
		}
		return(true);
}
unsigned long long int lifeline(unsigned long long int n)
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
unsigned long long int man(unsigned long long int num)
{
	return(lifeline(num));	
}
void printall(char myrule[], char temp[],unsigned long long  int i,unsigned long long int k,unsigned long long int n)
 {
    	if(i == k) 
		{
			if(temp[0]=='0'||temp[k-1]=='0')
				return;	
    		FOR(m, k) 
    		temp[k]='\0';
    		unsigned long long int num;
    		num=atoll(temp);
    		keep[ind]=num;
    		ind++;
    		return;
    	}
    	FOR(p, n) {
    		temp[i] = myrule[p];
    		printall(myrule, temp, i+1, k, n);
    	}
  }
     
void solve(char myrule[],unsigned long long int n, unsigned long long int k) 
{
     
    	char temp[k];
    	printall(myrule, temp, 0, k, n);
}
     
int main() 
{
	unsigned long long int i,j,k,steps,starter;
	unsigned long long int range=100000005;
	for(i=0;i<=range;++i)
		selfish[i]=true;
		selfish[0]=false;
   		selfish[1]=false;
	for(i=2;i*i<=range;++i)
		{
    		if(selfish[i])
			{
    			for(j=i*i;j<=range;j+=i)
				{
    				selfish[j]=false;
    			}
    		}
    	}
       	char myrule[] = {'0', '1'};
    	unsigned long long int n = sizeof(myrule)/sizeof(myrule[0]);
    	solve(myrule, n,16);
    	unsigned long long int inputbase,outputbase,santa,outputnumber2,outputnumber3,outputnumber4,outputnumber5,s;
    	unsigned long long int outputnumber6,outputnumber7,outputnumber8,outputnumber9,outputnumber10;
    	bool csgo2,csgo3,csgo4,csgo5,csgo6,csgo7,csgo8,csgo9,csgo10;
    	outputbase=10;
    	for(i=0;i<=ind-1;i++)
    	{
			if(shiv>=50)
				break;
				santa=keep[i];
    			outputnumber2=damn(santa,2);
				outputnumber3=damn(santa,3);
				outputnumber4=damn(santa,4);
				outputnumber5=damn(santa,5);
				outputnumber6=damn(santa,6);
				outputnumber7=damn(santa,7);
				outputnumber8=damn(santa,8);
				outputnumber9=damn(santa,9);
				outputnumber10=damn(santa,10);
				if(outputnumber2<=100000000)
						csgo2=checkprimehashing(outputnumber2);
				else
						csgo2=peepli(outputnumber2);
				if(outputnumber3<=100000000)
						csgo3=checkprimehashing(outputnumber3);
				else
						csgo3=peepli(outputnumber3);
				if(outputnumber4<=100000000)
						csgo4=checkprimehashing(outputnumber4);
				else
						csgo4=peepli(outputnumber4);
				if(outputnumber5<=100000000)
						csgo5=checkprimehashing(outputnumber5);
				else
						csgo5=peepli(outputnumber5);
				if(outputnumber6<=100000000)
						csgo6=checkprimehashing(outputnumber6);
				else
						csgo6=peepli(outputnumber6);
				if(outputnumber7<=100000000)
						csgo7=checkprimehashing(outputnumber7);
				else
						csgo7=peepli(outputnumber7);
				if(outputnumber8<=100000000)
						csgo8=checkprimehashing(outputnumber8);
				else
						csgo8=peepli(outputnumber8);
				if(outputnumber9<=100000000)
						csgo9=checkprimehashing(outputnumber9);
				else
						csgo9=peepli(outputnumber9);
				if(outputnumber10<=100000000)
						csgo10=checkprimehashing(outputnumber10);
				else
						csgo10=peepli(outputnumber10);
				if(csgo2==false&&csgo3==false&&csgo4==false&&csgo5==false&&csgo6==false&&csgo7==false&&csgo8==false&&csgo9==false&&csgo10==false)
					{
						shivang[shiv][0]=santa;
						shivang[shiv][2]=outputnumber2;
						shivang[shiv][3]=outputnumber3;
						shivang[shiv][4]=outputnumber4;
						shivang[shiv][5]=outputnumber5;
						shivang[shiv][6]=outputnumber6;
						shivang[shiv][7]=outputnumber7;
						shivang[shiv][8]=outputnumber8;
						shivang[shiv][9]=outputnumber9;
						shivang[shiv][10]=outputnumber10;
						shiv++;
					}
    		}
    		for(i=1;i<=shiv;i++)
    			{
    				for(j=2;j<=10;j++)
    					{
    						shivang[i][j]=man(shivang[i][j]);
    					}
    			}
   // 	unsigned long long int Test,Jstar,knock;    	
    //		scanf("%llu",&Test);
    //		scanf("%llu",&knock,&Jstar);
    		printf("Case #1:\n");
    		
    		printf("%llu ",1000000011001101);
    		printf("3 2 5 2 7 2 5 2 3\n");
    		
    		for(i=1;i<=shiv-1;i++)
					{
						printf("%llu ",shivang[i][0]);
							for(j=2;j<=10;j++)
								printf("%llu ",shivang[i][j]);
							if(i<shiv-1)
							printf("\n");
					}
   	return 0;
}
     
