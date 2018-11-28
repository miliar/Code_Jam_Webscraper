#include <iostream>
#include <string.h>
#include <set>
#include <stdio.h>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <iterator>
#include <queue>
#include <stack>

using namespace std;

int main()
{   
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long int n;
    cin>>n;
    for(long long int i=0;i<n;i++)
    {	
    	long long int count[30]={0};
    	string a;
    	cin>>a;
    	for(long long int j=0;j<a.length();j++)
    	{	
    		char c = tolower(a[j]);
    		count[c-'a']++;
    	}
    	long long int zeros = count[25];
    	if(zeros<0)
    		zeros = 0;
    	count[4]-=zeros;
    	count[17]-=zeros;
    	count[14]-=zeros;
    	long long int six = count[23];
    	if(six<0)
    		six = 0;
    	count[18]-=six;
    	count[8]-=six;
    	long long int seven = count[18];
    	if(seven<0)
    		seven = 0;
    	count[4]-=seven;
    	count[21]-=seven;
    	count[13]-=seven;
    	// cout<<seven<<endl;
    	long long int eight = count[6];
    	if(eight<0)
    		eight=0;
    	count[8]-=eight;
    	count[7]-=eight;
    	long long int four = count[20];
    	if(four<0)
    		four = 0;
    	count[14]-=four;
    	long long int five = count[5] - four;
    	if(five<0)
    		five = 0;
    	count[8]-=five;
    	count[4]-=five;
    	long long int two = count [22];
    	if(two<0)
    		two = 0;
    	count[19]-=two;
    	count[14]-=two;
    	long long int one = count[14];
    	if(one<0)
    		one = 0;
    	count[13]-=one;
    	count[4]-=one;
    	long long int three = count[7];
    	long long int nine  = count[8];
    	long long int ten = count[13];
    	cout<<"Case #"<<i+1<<": ";
    	for(long long int temp = 1;temp<=zeros;temp++)
    		cout<<0;
    	for(long long int temp = 1;temp<=one;temp++)
    		cout<<1;
    	for(long long int temp = 1;temp<=two;temp++)
    		cout<<2;
    	for(long long int temp = 1;temp<=three;temp++)
    		cout<<3;
    	for(long long int temp = 1;temp<=four;temp++)
    		cout<<4;
    	for(long long int temp = 1;temp<=five;temp++)
    		cout<<5;
    	for(long long int temp = 1;temp<=six;temp++)
    		cout<<6;
    	for(long long int temp = 1;temp<=seven;temp++)
    		cout<<"7";
    	for(long long int temp = 1;temp<=eight;temp++)
    		cout<<8;
    	for(long long int temp = 1;temp<=nine;temp++)
    		cout<<9;
    	cout<<endl;

    }
    return 0;
}

