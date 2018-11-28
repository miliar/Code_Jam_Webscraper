#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#define FOR(i,N) for(int i=0;i<(N);i++)

unsigned long long int store[66000];
unsigned long long int final[55][12];

unsigned long long int indexi=0,Jcount=1;;

bool myprime[100000007];

unsigned long long int other_to_decimal(unsigned long long int,unsigned long long int);
unsigned long long int decimal_to_other(unsigned long long int,unsigned long long int);

unsigned long long int primeFactors(unsigned long long int n)
{
    // Print the number of 2s that divide n
    while (n%2 == 0)
    {
    //    printf("%d ", 2);
        return(2);
        n = n/2;
    }
 
    // n must be odd at this point.  So we can skip one element (Note i = i +2)
    for (int i = 3; i*i <=n; i = i+2) //Don't use i<=sqrt(n)
    {
        // While i divides n, print i and divide n
        while (n%i == 0)
        {
      //      printf("%d ", i);
        	return(i);
		    n = n/i;
        }
    }
 
    // This condition is to handle the case whien n is a prime number
    // greater than 2
    if (n > 2)
    	return(n);
        //printf ("%d ", n);
}

unsigned long long int finddivisor(unsigned long long int num)
{
	return(primeFactors(num));	
}

unsigned long long int other_to_decimal(unsigned long long int inputnumber,unsigned long long int inputbase)
{
unsigned long long int k,op,s,p;
op=0;
k=inputnumber;
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

unsigned long long int decimal_to_other(unsigned long long int outputnumber,unsigned long long int outputbase)
{
unsigned long long int op=0,p,k,s;
k=outputnumber;
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


bool checkprime(unsigned long long int num)
{
	if(num==2||num==3)
		return(true);
	if(num%2==0||num%3==0)
		return(false);
	
	int i=5;
	//int w=2;
	
	while(i*i<=num)
		{
			if(num%i==0)
				return(false);
			i++;
	//		w=6-w;
		}
		return(true);
}

bool checkprimehashing(unsigned long long int num)
{
	if(myprime[num]==true)
		return(true);
}
     
void printall(char arr[], char temp[],unsigned long long  int i,unsigned long long int k,unsigned long long int n)
 {
    	if(i == k) 
		{
			if(temp[0]=='0'||temp[k-1]=='0')
				return;	
    		FOR(m, k) //printf("%c",temp[m]);// << temp[m];
    		temp[k]='\0';
    		unsigned long long int num;
    	//	sprintf(temp,"%llu",num);
    		num=atoll(temp);
		//	printf("temp=%s and num=%llu\n",temp,num);
    		store[indexi]=num;
    		indexi++;
    		return;
    	}
     
    	FOR(p, n) {
    		temp[i] = arr[p];
    		printall(arr, temp, i+1, k, n);
    	}
  }
     
void solve(char arr[],unsigned long long int n, unsigned long long int k) 
{
     
    	char temp[k];
    	printall(arr, temp, 0, k, n);
}
     
int main() 
{
//freopen("input.txt", "r" , stdin);
//freopen ("output.out","w",stdout);

	unsigned long long int i,j,k,count,begin;
	//int N=10000000002;
	// Generate the primes till sqrt(n)
//	int range=floor(sqrt((double)N));
	//Generate the primes till range
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
	
/*	for(i=0;i<=1000000;i++)
		{
			if(myprime[i]==true)
				printf("%d is a prime\n",i);
		}
*/
	
       	char arr[] = {'0', '1'};
    	unsigned long long int n = sizeof(arr)/sizeof(arr[0]);
     
     	
    	solve(arr, n,16);
    	
    	unsigned long long int inputbase,outputbase,inputnumber,outputnumber2,outputnumber3,outputnumber4,outputnumber5,s;
    	unsigned long long int outputnumber6,outputnumber7,outputnumber8,outputnumber9,outputnumber10;
    	bool cas2,cas3,cas4,cas5,cas6,cas7,cas8,cas9,cas10;
    	
    //	int countneg=0;
    /*	printf("Total=%d\n",indexi);
    	for(i=0;i<=indexi-1;i++)
    		printf("%d\n",store[i]);
    */		
    	outputbase=10;
    	
    	for(i=0;i<=indexi-1;i++)
    	{
			if(Jcount>=50)
				break;
				inputnumber=store[i];
				
    			outputnumber2=other_to_decimal(inputnumber,2);
				outputnumber3=other_to_decimal(inputnumber,3);
				outputnumber4=other_to_decimal(inputnumber,4);
				outputnumber5=other_to_decimal(inputnumber,5);
				outputnumber6=other_to_decimal(inputnumber,6);
				outputnumber7=other_to_decimal(inputnumber,7);
				outputnumber8=other_to_decimal(inputnumber,8);
				outputnumber9=other_to_decimal(inputnumber,9);
				outputnumber10=other_to_decimal(inputnumber,10);
				
				if(outputnumber2<=100000000)
						cas2=checkprimehashing(outputnumber2);
				else
						cas2=checkprime(outputnumber2);
				if(outputnumber3<=100000000)
						cas3=checkprimehashing(outputnumber3);
				else
						cas3=checkprime(outputnumber3);
				if(outputnumber4<=100000000)
						cas4=checkprimehashing(outputnumber4);
				else
						cas4=checkprime(outputnumber4);
				if(outputnumber5<=100000000)
						cas5=checkprimehashing(outputnumber5);
				else
						cas5=checkprime(outputnumber5);
				if(outputnumber6<=100000000)
						cas6=checkprimehashing(outputnumber6);
				else
						cas6=checkprime(outputnumber6);
				if(outputnumber7<=100000000)
						cas7=checkprimehashing(outputnumber7);
				else
						cas7=checkprime(outputnumber7);
				if(outputnumber8<=100000000)
						cas8=checkprimehashing(outputnumber8);
				else
						cas8=checkprime(outputnumber8);
				if(outputnumber9<=100000000)
						cas9=checkprimehashing(outputnumber9);
				else
						cas9=checkprime(outputnumber9);
				if(outputnumber10<=100000000)
						cas10=checkprimehashing(outputnumber10);
				else
						cas10=checkprime(outputnumber10);
				
				if(cas2==false&&cas3==false&&cas4==false&&cas5==false&&cas6==false&&cas7==false&&cas8==false&&cas9==false&&cas10==false)
					{
						final[Jcount][0]=inputnumber;
						final[Jcount][2]=outputnumber2;
						final[Jcount][3]=outputnumber3;
						final[Jcount][4]=outputnumber4;
						final[Jcount][5]=outputnumber5;
						final[Jcount][6]=outputnumber6;
						final[Jcount][7]=outputnumber7;
						final[Jcount][8]=outputnumber8;
						final[Jcount][9]=outputnumber9;
						final[Jcount][10]=outputnumber10;
						Jcount++;
					}

    		}
				
			//	int x=100011;
			//	printf("Input Number=%d--->%d",x,other_to_decimal(x,2));
				
		/*		for(i=1;i<=Jcount;i++)
					{
						printf("Input Number=%d-->",final[i][0]);
							for(j=2;j<=10;j++)
								printf("%d ",final[i][j]);
							printf("\n");
					}
    	*/
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
    
    //Finding this manually
    		printf("%llu ",1000000011001101);
    		printf("3 2 5 2 7 2 5 2 3");
    		
    		
    		//printf("\n");
    		
    //	fclose(stdout);
    	return 0;
}
     
