#include<bits/stdc++.h>
#include<vector>
#include<iostream>
#include<stack>
#include<queue>
#include<algorithm>
#include<string.h>
#include<stdlib.h>
#include<set>
#include<map>
#include<math.h>

int gcd(int a, int b)
{
	if(a%b==0)
	return a;
	else
	return gcd(b,a%b);
}
int read_int(){
	char r;
	bool start=false,neg=false;
	long long int ret=0;
	while(true){
		r=getchar();
		if((r-'0'<0 || r-'0'>9) && r!='-' && !start){
			continue;
		}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){
			break;
		}
		if(start)ret*=10;
		start=true;
		if(r=='-')neg=true;
		else ret+=r-'0';
	}
	if(!neg)
		return ret;
	else
		return -ret;
}
using namespace std ;

int main()
{
    freopen("question.txt","r",stdin);
    freopen("answer.txt","w",stdout);

int t;
int p;
int q;
int o;
int k;

//	cin>>t;
  t=read_int();
	for(q=0;q<t;q++)

        {
		p=read_int();
		int arr[p];

		for(k=0;k<p;k++)


        arr[k]=read_int();

		int john=arr[0];
		k=1;
		while(k<p){
			if(arr[k]>john)john=arr[k];
			k++;
		}
		int petrucci=john,guitar;
		for(o=1;o<john+1;o++){
			guitar=o;
			for(k=0;k<p;k++)
                {
				if(arr[k]>o)

				{
					if(arr[k]%o==0)

						guitar+=((arr[k]/o)-1);
					else
						guitar+=arr[k]/o;
				}

			}

			petrucci=min(petrucci,guitar);
		}
		int musicman=petrucci;

		cout<<"Case #"<<q+1<<": "<<musicman<<endl;
	}

	return 0;
}
