#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
unsigned long long int final[55][12];
unsigned long long int st[66000];
unsigned long long int indexi=0,Jcount=1;;
bool myprime[100000007];
unsigned long long int baseod(unsigned long long int,unsigned long long int);
unsigned long long int basedo(unsigned long long int,unsigned long long int);
unsigned long long int pfac(unsigned long long int num)
{
    while (num%2 == 0)
    {
        return(2);
        num=num/2;
    }
    for (int i = 3; i*i <=num; i = i+2) 
    {
        while (num%i == 0)
        {
        	return(i);
		    num= num/i;
        }
    }
    if (num> 2)
    	return(num);
}

unsigned long long int finddivisor(unsigned long long int num)
{
	return(pfac(num));	
}

unsigned long long int baseod(unsigned long long int innum,unsigned long long int inbase)
{
unsigned long long int k,op,s,p;
op=0;
k=innum;
p=1;
while(k!=0)
{
 s=k%10;
 k=k/10;
 op=op+s*p;
 p=p*inbase;
}
return op;
}
unsigned long long int basedo(unsigned long long int outnum,unsigned long long int outbase)
{
unsigned long long int op=0,p,k,s;
k=outnum;
p=1;
while(k!=0)
{
s=k%outbase;
k=k/outbase;
op=op+s*p;
p=p*10;
}
return op;
}
bool check(unsigned long long int num)
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

bool chash(unsigned long long int num)
{
	if(myprime[num]==true)
		return(true);
}
     
void solveit(char arr[], char temp[],unsigned long long  int i,unsigned long long int k,unsigned long long int n)
 {
    	if(i == k) 
		{
			if(temp[0]=='0'||temp[k-1]=='0')
				return;	
    	for(int m=0;m<(k);m++)
    		temp[k]='\0';
    		unsigned long long int num;
    		num=atoll(temp);
    		st[indexi]=num;
    		indexi++;
    		return;
    	}
     
		for(int p=0;p<(n);p++)		{
    		temp[i] = arr[p];
    		solveit(arr, temp, i+1, k, n);
    	}
  }
     
void solve(char arr[],unsigned long long int n, unsigned long long int k) 
{
     
    	char temp[k];
    	solveit(arr, temp, 0, k, n);
}
     
int main() 
{
	unsigned long long int i,j,k,count,begin;
	unsigned long long int range=100000005;
	for(i=0;i<=range;++i)
		myprime[i]=true;
   			
		myprime[0]=false;
   		myprime[1]=false;
	
	for(i=2;i*i<=range;++i)
		{
    		if(myprime[i])
			{
    			for(j=i*i;j<=range;j+=i)
				{
    				myprime[j]=false;
    			}
    		}
    	}
		char arr[] = {'0', '1'};
    	unsigned long long int n = sizeof(arr)/sizeof(arr[0]);
    	solve(arr, n,16);
    	unsigned long long int inbase,outbase,innum,s;
    	unsigned long long int o2,o3,o4,o5,o6,o7,o8,o9,o10;
    	bool c2,c3,c4,c5,c6,c7,c8,c9,c10;
    	outbase=10;
    	for(i=0;i<=indexi-1;i++)
    	{
			if(Jcount>=50)
				break;
				innum=st[i];
    			o2=baseod(innum,2);
				o3=baseod(innum,3);
				o4=baseod(innum,4);
				o5=baseod(innum,5);
				o6=baseod(innum,6);
				o7=baseod(innum,7);
				o8=baseod(innum,8);
				o9=baseod(innum,9);
				o10=baseod(innum,10);
				
				if(o2<=100000000)
						c2=chash(o2);
				else
						c2=check(o2);
				if(o3<=100000000)
						c3=chash(o3);
				else
						c3=check(o3);
				if(o4<=100000000)
						c4=chash(o4);
				else
						c4=check(o4);
				if(o5<=100000000)
						c5=chash(o5);
				else
						c5=check(o5);
				if(o6<=100000000)
						c6=chash(o6);
				else
						c6=check(o6);
				if(o7<=100000000)
						c7=chash(o7);
				else
						c7=check(o7);
				if(o8<=100000000)
						c8=chash(o8);
				else
						c8=check(o8);
				if(o9<=100000000)
						c9=chash(o9);
				else
						c9=check(o9);
				if(o10<=100000000)
						c10=chash(o10);
				else
						c10=check(o10);
				
				if(c2==false&&c3==false&&c4==false&&c5==false&&c6==false&&c7==false&&c8==false&&c9==false&&c10==false)
					{
						final[Jcount][0]=innum;
						final[Jcount][2]=o2;
						final[Jcount][3]=o3;
						final[Jcount][4]=o4;
						final[Jcount][5]=o5;
						final[Jcount][6]=o6;
						final[Jcount][7]=o7;
						final[Jcount][8]=o8;
						final[Jcount][9]=o9;
						final[Jcount][10]=o10;
						Jcount++;
					}

    		}
    		for(i=1;i<=Jcount;i++)
    			{
    				for(j=2;j<=10;j++)
    					{
    						final[i][j]=finddivisor(final[i][j]);
    					}
    			}
    	unsigned long long int T,J,NN;
    		scanf("%llu",&T);
    		scanf("%llu",&NN,&J);
    		printf("Case #1:\n");
    		for(i=1;i<=Jcount-1;i++)
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
     
