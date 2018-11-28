#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
using namespace std;


#define MAX 100009
typedef long long int ll;

string s;
ll X,L;
ll countj,countk;
ll counter;
const int matrix[4][4] = {
							{49,105,106,107},
							{105,-49,107,-106},
							{106,-107,-49,105},
							{107,106,-105,-49}
						};

const int resultTwo[4][4] = {
							{1,1,1,1},
							{-105,-1,105,1},
							{-106,-1,106,1},
							{-107,-1,107,1}
						};	 

const int resultOne[4][4] = {
							{1,1,1,1},
							{105,-1,-105,1},
							{106,-1,-106,1},
							{107,-1,-107,1}
						};	 

ll getIndex(char a)
{
	if(a=='1')
		return 0;
	if(a=='i')
		return 1;
	if(a=='j')
		return 2;
	if(a=='k')
		return 3;
}

char getCharVal(ll i)
{
	if(i==49)
		return '1';
	if(i==105)
		return 'i';
	if(i==106)
		return 'j';
	if(i==107)
		return 'k';
}

ll getIntVal(char cValue, ll factor)
{
	if(cValue == 'i' && factor == 1)
		return 105;

	if(cValue == 'i' && factor == -1)
		return -105;

	if(cValue == 'j' && factor == 1)
		return 106;

	if(cValue == 'j' && factor == -1)
		return -106;

	if(cValue == 'k' && factor == 1)
		return 107;

	if(cValue == 'k' && factor == -1)
		return -107;
	
	if(cValue == '1' && factor == 1)
		return 49;
	
	if(cValue == '1' && factor == -1)
		return -49;
}

ll getCvalue()
{
	ll i;
	ll e,f,intVal;
	ll factor = 1;
	char cValue;
	
	countk = 0;
	countj = 0;

	cValue = s[0];

	f = getIndex(s[0]);

	if(s[0]=='j')
		countj++;

	if(s[0]=='k')
		countk++;

	for(i=1;i<L;i++)
	{
		if(s[i]=='j')
			countj++;

		if(s[i]=='k')
			countk++;

		e = getIndex(s[i]);

		intVal = matrix[f][e];

		intVal = intVal * factor;

		if(intVal<0)
			factor = -1;
		else
			factor = 1;

		cValue = getCharVal(abs(intVal));

		f = getIndex(cValue);
	}

	return getIntVal(cValue,factor);
}

bool isIPresent()
{
	if(s[0]=='i')
		return true;

	ll P = X;
	ll i,start;
	ll intVal;
	ll factor = 1;
	ll e,f;

	start = 1;

	char currVal = s[0];
	
	while(P--)
	{

		f = getIndex(currVal);

		for(i=start ; i<L ;i++)
		{
			e = getIndex(s[i]);

			intVal = matrix[f][e];

			intVal = intVal * factor;

			if(intVal<0)
				factor = -1;
			else
				factor = 1;

			currVal = getCharVal(abs(intVal));

			if(currVal == 'i' && factor == 1){
				//printf("\nFound in func at index = %lld",i);
				counter+= (i+1);
				return true;
			}


			f = getIndex(currVal);
		}
		counter+=L;
		start = 0;
	}

	return false;
}

int main()
{
	ll caseno,tc;
	bool flag;	

	freopen("input","r",stdin);
	freopen("not","w",stdout);
	
	scanf("%lld",&tc);

	caseno = 1;

	while(caseno<=tc)
	{
		counter = 0;

		flag = false;

		ll value=0;
		ll temp;
		char cValue;
		ll factor;


		scanf("%lld%lld",&L,&X);
		
		cin>>s;

		temp = getCvalue();

		if(temp<0)
			factor = -1;
		else
			factor = 1;

		cValue = getCharVal(abs(temp));
//printf("\nC Value of string is %c and factor is %lld\n",cValue,factor);
		
		flag = isIPresent();

	//	printf("\nCount of J = %lld and count of k = %lld\n",countj,countk);

		if( flag && ( counter+1 < (L*X)) && (countj>0 || countk>0))
		{
			if(cValue != '1')
			{
				ll get = (X-1)%4;
				ll ind = getIndex(cValue);

				if(factor==1)
				{
					value = resultOne[ind][get];

					if(value == -1)
						printf("Case #%lld: YES\n",caseno);
					else
						printf("Case #%lld: NO\n",caseno);
				}
				else
				{
					value = resultTwo[ind][get];

					if(value == -1)
						printf("Case #%lld: YES\n",caseno);
					else
						printf("Case #%lld: NO\n",caseno);
				}
			}
			else if(factor == -1)
			{
				if(X%2==0)
				{
					printf("Case #%lld: NO\n",caseno);
				}
				else
				{
					printf("Case #%lld: YES\n",caseno);
				}
			}
			else
			{
				printf("Case #%lld: NO\n",caseno);
			}
		}
		else
		{
			printf("Case #%lld: NO\n",caseno);
		}

		caseno++;
	}
}