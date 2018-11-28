#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<math.h>
#include<fstream>

using namespace std;

int pal(long long int 	i)
{long long int num=i;
long long int n = num,dig;
 long long int rev = 0;
 while (num > 0)
 {
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
 }
 if(n == rev )return 1;
 else return 0;
}

int main()
{   //ios_base::sync_with_stdio(false);
	int a,b;int n ;fstream f("o.txt",ios::out);int i,q=0;
	fstream fin("new.txt",ios::in);fin>>n;
	while(n>0){int cnt=0;
	fin>>a>>b;
	for(i=a;i<=b;i++)
	{   int re=0;
		int res = pal(i);
		int p=sqrt(i);
		double z=sqrt(i);
		if(p-z==0)re=pal(p);
		 if((res==1)&&((p-z)==0)&&(re==1)){cnt++;cout<<i<<" ";}
	
	}
	//cout<<cnt<<"\n";
	
	f<<"Case #";f<<++q;f<<": ";f<<cnt<<"\n";
	n--;cout<<q<<"\n";
	}
	system("pause");
	return 0;
}



