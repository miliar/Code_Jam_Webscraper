#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#define FOR(i,N) for(int i=0;i<(N);i++)

unsigned long long int st[66000];
unsigned long long int final[55][12];
unsigned long long int indexi=0,J=1;;
bool prime[100000007];
unsigned long long int od(unsigned long long int,unsigned long long int);
unsigned long long int d_o(unsigned long long int,unsigned long long int);

unsigned long long int d_o(unsigned long long int on,unsigned long long int oba)
{
unsigned long long int op=0,p,k,s;
k=on;
p=1;
while(k!=0)
{
s=k%oba;
k=k/oba;
op=op+s*p;
p=p*10;
}
return op;
}

unsigned long long int od(unsigned long long int in,unsigned long long int ib)
{
unsigned long long int k,op,s,p;
op=0;
k=in;
p=1;
while(k!=0)
{
 s=k%10;
 k=k/10;
 op=op+s*p;
 p=p*ib;
}
return op;
}
unsigned long long int factor(unsigned long long int num)
{
    while (num%2 == 0)
    {
        return(2);
        num = num/2;
    }
    for (int i = 3; i*i <=num; i = i+2)
    {
        while (num%i == 0)
        {
        	return(i);
		    num = num/i;
        }
    }
    if (num > 2)
    	return(num);
}

unsigned long long int divi(unsigned long long int num)
{
	return(factor(num));	
}



bool chk(unsigned long long int num)
{
	if(num==2||num==3)
		return(true);
	if(num%2==0||num%3==0)
		return(false);
	int i=5;
	while(i*i<=num)
		{if(num%i==0)
				return(false);
			i++;
		}
		return(true);
}
bool Chash(unsigned long long int num)
{
	if(prime[num]==true)
		return(true);
}
void prt(char arr[], char temp[],unsigned long long  int i,unsigned long long int k,unsigned long long int n)
 {
    	if(i == k) 
		{
			if(temp[0]=='0'||temp[k-1]=='0')
				return;	
    		FOR(m, k)
    		temp[k]='\0';
    		unsigned long long int num;
    		num=atoll(temp);
    		st[indexi]=num;
    		indexi++;
    		return;
    	}
    	FOR(p, n) {
    		temp[i] = arr[p];
    		prt(arr, temp, i+1, k, n);
    	}
  }
  

void cal(char arr[],unsigned long long int n, unsigned long long int k) 
{		char temp[k];
    	prt(arr, temp, 0, k, n);
}  


int main() 
{
	unsigned long long int i,j,k,count,begin;
	unsigned long long int range=100000005;
	for(i=0;i<=range;++i)
		prime[i]=true;
   			
		prime[0]=false;
   		prime[1]=false;
	
	for(i=2;i*i<=range;++i)
		{if(prime[i])
			{for(j=i*i;j<=range;j+=i)
				{
    				prime[j]=false;
    			}
    		}
    	}
       	char arr[] = {'0', '1'};
    	unsigned long long int n = sizeof(arr)/sizeof(arr[0]);
    	cal(arr, n,16);
    	unsigned long long int ib,ob,in,on2,on3,on4,on5,s;
    	unsigned long long int on6,on7,on8,on9,on10;
    	bool cas2,cas3,cas4,cas5,cas6,cas7,cas8,cas9,cas10;		
    	ob=10;
    	for(i=0;i<=indexi-1;i++)
    	{
			if(J>=50)
				break;
				in=st[i];
    			on2=od(in,2);
				on3=od(in,3);
				on4=od(in,4);
				on5=od(in,5);
				on6=od(in,6);
				on7=od(in,7);
				on8=od(in,8);
				on9=od(in,9);
				on10=od(in,10);
				if(on2<=100000000)
						cas2=Chash(on2);
				else
						cas2=chk(on2);
				if(on3<=100000000)
						cas3=Chash(on3);
				else
						cas3=chk(on3);
				if(on4<=100000000)
						cas4=Chash(on4);
				else
						cas4=chk(on4);
				if(on5<=100000000)
						cas5=Chash(on5);
				else
						cas5=chk(on5);
				if(on6<=100000000)
						cas6=Chash(on6);
				else
						cas6=chk(on6);
				if(on7<=100000000)
						cas7=Chash(on7);
				else
						cas7=chk(on7);
				if(on8<=100000000)
						cas8=Chash(on8);
				else
						cas8=chk(on8);
				if(on9<=100000000)
						cas9=Chash(on9);
				else
						cas9=chk(on9);
				if(on10<=100000000)
						cas10=Chash(on10);
				else
						cas10=chk(on10);
				
				if(cas2==false&&cas3==false&&cas4==false&&cas5==false&&cas6==false&&cas7==false&&cas8==false&&cas9==false&&cas10==false)
					{
						final[J][0]=in;
						final[J][2]=on2;
						final[J][3]=on3;
						final[J][4]=on4;
						final[J][5]=on5;
						final[J][6]=on6;
						final[J][7]=on7;
						final[J][8]=on8;
						final[J][9]=on9;
						final[J][10]=on10;
						J++;
					}

    		}
    		for(i=1;i<=J;i++)
    			{
    				for(j=2;j<=10;j++)
    					{
    						final[i][j]=divi(final[i][j]);
    					}
    			}
    	unsigned long long int T,JC,NN;
    		scanf("%llu",&T);
    		scanf("%llu",&NN,&JC);
    		printf("Case #1:\n");
    		for(i=1;i<=J-1;i++)
					{
						printf("%llu ",final[i][0]);
							for(j=2;j<=10;j++)
								printf("%llu ",final[i][j]);
							printf("\n");
					}
    		printf("%llu ",1000000011001101);
    		printf("3 2 5 2 7 2 5 2 3");
    	return 0;
}
     
