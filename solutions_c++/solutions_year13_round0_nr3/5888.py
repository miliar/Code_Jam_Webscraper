#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>


int isPalindrome(unsigned long );

int main(int argc,char *argv[])
{
	char *line=NULL;
	size_t lineLen=0;
	int totalRounds=0;
	FILE *fp=NULL;
	unsigned long startNumber,endNumber;
	double squareRoot;
	fp=fopen(argv[1],"r");
	if(fp!=NULL)
	{
		getline(&line,&lineLen,fp);
		totalRounds=atoi(line);
		for(int i=0;i<totalRounds;i++)
		{			
			fscanf(fp,"%ld %ld",&startNumber,&endNumber);
			int totalSquarePalindromes=0;
			for(unsigned long j=startNumber;j<=endNumber;j++)
			{
				if(isPalindrome(j))
				{
					squareRoot=sqrt(j);
					if(ceil(squareRoot)==squareRoot and isPalindrome(squareRoot)==1)
						totalSquarePalindromes++;
				}

			}
			printf("Case #%d: %d\n",i+1,totalSquarePalindromes);
		}

		fclose(fp);
	}
	return 0;
}


int isPalindrome(unsigned long number)
{
	char palindromeNumber[100];
	bzero(palindromeNumber,sizeof(palindromeNumber));
	sprintf(palindromeNumber,"%ld",number);

	for(int i = 0, len=strlen(palindromeNumber),j=len-1; i < len / 2; i++, j--) {
		if(palindromeNumber[i] != palindromeNumber[j]) {
			return 0;
			break;
		}
	}


	return 1;
}

