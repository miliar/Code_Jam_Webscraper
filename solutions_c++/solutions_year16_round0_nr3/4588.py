#include <iostream>
#include <string>
#include <math.h>
using namespace std;
long is_notprime(long);
long formBase(string,int);
string s;
void recur(int,string);
int nontriv[9],j,n;
long is_notprime(long x)
{
    if (x < 2)
    {
            return x;
    }

    for (long i = 2; i < sqrt(x+1); i++)
    {
        if (x%i == 0)
        {
            return i;
        }
    }
    return 0;
}

long formBase(int base){
  long mult=0,sum=0;
	for(int i=n-1;i>=0;i--){
    if(s[i]=='1')
		sum+=pow(base,mult);
    mult++;
	}
  return is_notprime(sum);
}

void recur(int m){
  if(j>0){
    if(m==0){
      long tmp,flag=0;
      for(int k=2;k<=10&&!flag;k++){
        tmp=formBase(k);
        if(tmp)
          nontriv[k-2]=tmp;
        else
          flag=1;
      }
      if(!flag){
          for(int p=0;p<n;p++)
           cout<<s[p];
          for(int l=0;l<9;l++)
            cout<<" "<<nontriv[l];
          cout<<"\n";
          j--;
      }
    }else{
      if(m==n || m==1){
        s[n-m]='1';
        recur(m-1);
      }
      else{
        s[n-m]='1';
        recur(m-1);
        s[n-m]='0';
        recur(m-1);
      }
    }
  }
}

int main() {
	// your code goes here
	long T,t;
	cin>>T;
	t=T;
	while(T>0){
		cin>>n>>j;
		cout<<"Case #"<<t-T+1<<":"<<"\n";
    	recur(n);
		T--;
	}
	return 0;
}
