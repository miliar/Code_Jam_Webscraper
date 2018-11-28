#include<bits/stdc++.h>
using namespace std;
char str[100000]={NULL};
int arr[1000]={NULL};
char result[1000]={NULL};
map<char,int>m;
map<int,int>num;
map<int,int>::iterator itr1;
int counter=0;
void putnum();
void remstr(char arr1[]);
int main(){
	//freopen("input.in","r",stdin);
	//freopen("output.txt","w",stdout);
	int test,t;
	scanf("%d",&test);
	t = test;
	while(test--){
	m.clear();
	num.clear();
	counter = 0;
	scanf("%s",str);
	for(int i=0;i<strlen(str);i++)
	{
		switch(str[i]){
	case 'Z':
		num[0]++;
		remstr("ZERO");
		break;
	case 'W':
		num[2]++;
		remstr("TWO");
		break;
	case 'U':
		num[4]++;
		remstr("FOUR");
		break;
	case 'X':
		num[6]++;
		remstr("SIX");
		break;
	case 'G':
		num[8]++;
		remstr("EIGHT");
		break;
		}
	}
putnum();
for(int i=0;i<strlen(str);i++)
	{
		switch(str[i]){
	case 'O':
		num[1]++;
		remstr("ONE");
		break;
	case 'F':
		num[5]++;
		remstr("FIVE");
		break;
	case 'S':
		num[7]++;
		remstr("SEVEN");
		break;
	case 'H':
		num[3]++;
		remstr("THREE");
		break;
		}
	}
putnum();
for(int i=0;i<strlen(str);i++)
	{
		switch(str[i]){
	case 'I':
		num[9]++;
		remstr("NINE");
		break;
		}
	}
putnum();
sort(arr,arr+counter);
int i;
for( i=0;i<counter;i++)
result[i] = arr[i] + '0';
result[i]= '\0';
printf("Case #%d: %s\n",t-test,result);
}
}
void putnum()
{
	for(itr1= num.begin();itr1!=num.end();itr1++)
	{
		for(int i=0;i<itr1->second;i++)
			arr[counter++]=itr1->first;
	}
num.clear();
}
void remstr(char arr1[])
{
for(int j= 0;j<strlen(arr1);j++)
for(int i=0;i<strlen(str);i++)
{
	if(str[i] == arr1[j])
		{
		str[i] = '1';
		break;
		}
}
}
