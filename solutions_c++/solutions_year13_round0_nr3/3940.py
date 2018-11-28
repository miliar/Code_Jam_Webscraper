#include<iostream>
#include<cmath>
#include <cassert>
#include <cstring>
#include <cstdio>

using namespace std;

	/*for dp, gen[i][j] is the number
	 * of sqrt of fair and square
	 * with i digits and sum of square
	 * of digits of j
	 */
	long long int gen[70][11]={{0}};
	

void minusOne(char* a, char* dest, int digit)
{
	int pos=digit-1;
	char temp[120]={0};
	memcpy(temp,a,119);
	while (temp[pos]=='0') 
	{
		temp[pos]='9';
		pos--;
	}
	if (pos >= 0 && temp[pos] >0) temp[pos]--;
	if (pos == 0 && temp[pos]=='0')
	{
		memcpy(dest,temp+1,119);
	}
	else
	{
		memcpy(dest,temp,119);
	}
	if (dest[0]==0) dest[0]='0';
}

void appendTimes(char* a, char* dest, int digit, int b)
{
	if (b==0)
	{
		dest[0]='0';
		dest[1]=0;
	}
	char result[120]={0};
	int temp = b*b;
	int remainder=temp/10;
	result[digit+2]=temp%10+'0';
	for (int i=digit-1;i>=0;--i)
	{
		temp = (a[i]-'0')*2*b + remainder;
		remainder = temp/10;
		result[i+2] = temp%10 + '0';
		//cout << "--TEMP: " << temp << endl;
	}
	if (remainder >0) 
	{
		result[1]= remainder%10 + '0';
		remainder /= 10;
		if (remainder == 0)
			strcpy(dest,result+1);
		else strcpy(dest,result);
		return;
	}
	else
	{
		strcpy(dest,result+2);
		return;
	}
}


int compareNum(char* a, char* b, int digit)
{
	if (strlen(a) > strlen(b)) return 1;
	else if (strlen(a) < strlen(b)) return -1;
	for (int i=0;i<digit;++i)
	{
		if (a[i] == b[i]) continue;
		else if (a[i] > b[i]) return 1;
		else if (a[i] < b[i]) return -1;
	}
	return 0;
}

void minusBig(char* a, char* b)
{
	int alen = strlen(a), blen = strlen(b);
	int apos = alen-1, bpos = blen-1;
	int remainder = 0;
	for (int i=0;i<strlen(b);++i)
	{
		a[apos-i] = a[apos-i] - b[bpos-i] - remainder + '0' ;
		if (a[apos-i] < '0')
		{
			a[apos-i] += 10;
			remainder = 1;
		}
		else remainder = 0;
	}
	if (remainder == 1) a[apos-strlen(b)]-=1;
	char* nonZeroPos = a;
	while (*nonZeroPos == '0') nonZeroPos++;
	memmove(a,nonZeroPos,alen-(a-nonZeroPos)+1);
}

void sqrtBig(char* a,char* result, int digit)
{
	if (a[0] == '0')
	{
		result[0] = '0';
		result[1] = 0;
		return;
	}
	//cout << "DIGIT: " << digit << endl;
	int head=0;
	int tail=1-digit%2;
	char curRemainder[120]={0};
	char tstr[120];
	int pos=0;
	for (int i=0;i<=101;++i) result[i]=0;
	while (head < digit)
	{
		int multi=1;
		int temp=0;
		for (int i=tail;i>=head;--i)
		{
			temp+=(a[i]-'0')*multi;
			multi*=10;
		}
		if (temp/10>0 || strlen(curRemainder)==0) sprintf(curRemainder,"%s%d",curRemainder, temp);
		else sprintf(curRemainder,"%s0%d",curRemainder,temp);
		//cout << "#CURREMAINDER: " << curRemainder << endl;
		int numToMulti=0;
		for (int i=1;i<10;++i)
		{
			appendTimes(result,tstr,strlen(result),i);
			//cout << "--I: " << i << endl;
			//cout << "--TSTR: " << tstr << endl;
			int tLen = strlen(tstr), remainderLen = strlen(curRemainder);
			if (tLen < remainderLen) 
			{
				numToMulti=i;
				continue;
			}
			else if (tLen > remainderLen)
			{
				numToMulti=i-1;
				break;
			}
			else
			{
				int state = compareNum(tstr,curRemainder,tLen);
				if (state == -1)
				{
					numToMulti=i;
					continue;
				}
				if (state == 1) 
				{
					numToMulti=i-1;
					break;
				}
				if (state == 0)
				{
					numToMulti=i;
					break;
				}
			}
		}
		appendTimes(result,tstr,strlen(result),numToMulti);
		//cout << "TSTR: " << tstr << endl;
		//cout << "RESULT: " << result << endl;
		minusBig(curRemainder,tstr);
		//cout << "CURREMAINDER: " << curRemainder << endl;
		result[pos++]=numToMulti+'0';
		head = tail+1;
		tail += 2;
	}
	result[pos]=0;
	return;
	
}

long long int bruteLastDigit(int digit, char* max)
{
	if (max[0]=='0') return 0;
	if (max[0]>='3' && digit==1) return 3;
	long long int result=0;
	int pos=(digit-1)/2;
	char num[51]={0};
	num[0] = num[digit-1] = '1';
	int sumSqr = 2;
	if (compareNum(num,max,digit)<1) result=1;
	int addSqr[4]={0};
	addSqr[0]=1;
	addSqr[1]=3;
	addSqr[2]=5;
	addSqr[3]=7;
	while (num[0] <= '2' && compareNum(num,max,digit) < 1)
	{
		assert(pos == (digit-1)/2);
		int multi=2;
		if (pos == (digit-1)/2 && digit%2==1) multi=1;
		while (sumSqr + multi*addSqr[num[pos]-'0'] >=10 && pos>0)
		{
			pos = pos-1;
			multi=2;
		}
		if (sumSqr + multi*addSqr[num[pos]-'0'] >= 10 && pos==0) break;
		for (int i=pos+1;i<=digit-3-pos;++i)
			num[i]='0';
		assert(sumSqr + multi*addSqr[num[pos]-'0'] < 10);
		num[pos]++;
		if (!(pos == (digit-1)/2 && digit%2==1))
			num[digit-1-pos]++;
		//cout << "NUM: " << num << ", MAX: " << max << endl;
		if (num[pos]>'2' || compareNum(num,max,digit) == 1) break;
		sumSqr += multi*addSqr[num[pos]-'0'];
		result++;
		if (pos < (digit-1)/2) pos = (digit-1)/2;
			
	}	
	//cout << "RESULT: " << result << endl;
	return result;

}

long long int countFNSfromZeroTo(char* max, int digit)
{
	long long int result=0;
	result += gen[digit-1][10];
	//cout << "GEN: " << result << endl;
	result += bruteLastDigit(digit,max);
	return result;
}

int main()
{
	//GENERATE gen[i][j] with DP
	gen[0][0]=1; //gen[0][0] is only to initialize
	for (int i=0;i<60;i+=2)
	{
		for (int j=0;j<10;++j)
		{
			if (gen[i][j] >0)
			{
				for (int k=0;k<sqrt(11-j)/2;++k)
				{
					int sumSqr=j+2*k*k;
					if (sumSqr <10 && sumSqr > 0)
					{
						gen[i+2][sumSqr]+=gen[i][j];
					}
				}
				for (int k=0;k<sqrt(11-j);++k)
				{
					int sumSqr=j+k*k;
					if (sumSqr <10 && sumSqr>0)
					{
						gen[i+1][sumSqr]+=gen[i][j];
					}
				}
			}
		}
		/*NOTE: we set gen[i][10] to be the number
		 * of i digits fair and square number
		 */ 
		for (int j=0;j<10;++j)
		{
			gen[i+1][10]+=gen[i+1][j];
			gen[i+2][10]+=gen[i+2][j];
		}
	}
	gen[0][10]=0;

	//STARTING THE TEST CASE
	int T;
	cin >> T;

	for (int t=1;t<=T;++t)
	{
		long long int result;
		char _A[120]={0}, _B[120]={0};
		cin >> _A >> _B;
		//cout << _A << "::" << _B << endl;
		int digitA=strlen(_A), digitB=strlen(_B);
	   char	AMinusOne[120];
		minusOne(_A, AMinusOne,digitA);
		char A[120],B[120];
		//cout << "CALCULATE SQRT OF: " << AMinusOne << endl;
		sqrtBig(AMinusOne,A,strlen(AMinusOne));
		//cout << "CALCULATE SQRT OF: " << _B << endl;
		sqrtBig(_B,B,digitB);

		//cout << "DEBUG\n";
		//cout << A << endl;
		//cout << B << endl;
		//cout << "END DEBUG\n";


		long long int resZeroToA, resZeroToB;
		digitA = strlen(A);
		digitB = strlen(B);
		resZeroToA = countFNSfromZeroTo(A,digitA);
		resZeroToB = countFNSfromZeroTo(B,digitB);
		//cout << "0 to " << A<< ": " <<resZeroToA << endl;
		//cout << "0 to " << B << ": " <<resZeroToB << endl;
		result = resZeroToB - resZeroToA;
		cout << "Case #" << t << ": " << result << endl;
	}


	return 0;



}
