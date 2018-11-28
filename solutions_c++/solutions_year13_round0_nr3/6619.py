#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>

using namespace std;



int func(int A, int B);
int IsPalindrome(int k);

int main()
{
	FILE *fp;
	FILE *out;
	int T;
	int A,B;
	int i,n;
	

	fp = fopen("C-small-attempt0.in","rb");

	if(fp==NULL)
	{
		cout << "nok" << endl;
		exit(0);
	}

	fscanf(fp, "%d",&T);

	
	out  = fopen("output.txt","w");

	for(i=1; i<=T; i++)
	{
		fscanf(fp, "%d",&A);
		fscanf(fp, "%d",&B);

		n = func(A,B);

		fprintf(out, "Case #%d: %d\n", i, n);

	}


	fclose(out);
	fclose(fp);


return(0);
}


int func(int A, int B)
{
	int d,k; 
	int sum=0;


	d = sqrt(A);		
	d = (d*d==A)? d:d+1;


	k = d*d;

	while(k<=B)
	{
		if(IsPalindrome(k))
		{
				if(IsPalindrome(d))
					{
						sum++;
						printf("%d\n", k);
					}
		}
		d++;
		k=d*d;
	}


	return(sum);
}


int IsPalindrome(int k)
{


	std::string s = std::to_string(k);

	if(s == string(s.rbegin(), s.rend()))return(1);

	return(0);
}

