#include <iostream>
#include<stdio.h>

using namespace std;
//char input[20],data[1000][20];
int count=0;

void main()
{
	int case_no= 0,number=0;
	int index=0;
	int number_A,number_B;
	char number_str[10000],number_rev[10000];
	freopen ("d:/C-small-attempt0.in","r",stdin);
    freopen ("d:/C-small-attempt0.out","w",stdout);
	cin>>case_no;

	for( int x=1; x<=case_no ;x++)
	{
			printf("Case #%d: ",x);
			cin>>number_A;
			cin>>number_B;
			count=0;
			for(number= number_A;number<=number_B; number++)
			{
				itoa(number,number_str,10);
				strcpy(number_rev,number_str);
				strrev(number_rev);

				if(strcmp(number_rev,number_str)==0)
				{
				//cout<<"palindrome";
				double n= sqrt((double)number);
				int x=n;
				n=n-x;
					if(n == 0.0)
					{
					//cout << " and square";
					itoa(x,number_str,10);
					strcpy(number_rev,number_str);
					strrev(number_rev);
						if((strcmp(number_rev,number_str)==0))
						{
						//cout<<" fair and square";
							//cout<<"\nnumbers "<<number<<"\n";
							count++;
						}
						/*else
						{
						cout<<" square root not palindrome";
						}*/
					}
					//else
					//cout<<n<<" less for square";

			}
		}//number_A to number_B loop
		printf("%d\n",count);
	}//case ended
}