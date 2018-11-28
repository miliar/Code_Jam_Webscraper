#include<iostream>
#include<string.h>
#include<stdio.h>

using namespace std;

void exchange(int,int);
void changeValue(int);
bool allValue(char *,int);

char a[100];

int main(){
	int len ,i,count;
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;++k)
    {
        //scanf("%[^\n]",a);
        cin >> a;
    	len=strlen(a);
		count=0;
	    while(!allValue(a,len))
	    {
	    	for(i=0;i<len;i++)
	        {
	            if(a[i]=='+') break;
	            else if(i==len-1)
	            {
	                for(int k=0;k<len;k++)
	                changeValue(k);
	                count++;
	            } 
	        }
	        for(i=0; i<len-1; i++)
	        {
	            if(a[i]!=a[i+1])
	            {
	                for(int j=0;j <= i;j++,i--)
	                {
	                    exchange(i,j);
	                    changeValue(i);
	                    if(i!=j)
	                    changeValue(j);
	                }
	                count++;
	            	break;  
	            }
	        }
	    }    
		cout << "Case #" << k << ": "<<  count << endl;
	}
    return 0;
}

void exchange(int p,int q)
{
    char temp;
    temp=a[p];
    a[p]=a[q];
    a[q]=temp;
}

void changeValue(int m)
{
    if(a[m]=='+')
    a[m]='-';
    else
    a[m]='+';
}

bool allValue(char *a,int len)
{
    for(int i=0; i < len; i++)
    {
        if(a[i]=='-')
        return 0;
    }
    return 1;
}