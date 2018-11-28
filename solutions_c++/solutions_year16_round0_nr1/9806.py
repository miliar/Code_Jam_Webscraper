#include <iostream>
using namespace std;
 
int main() {
	int input_v, test_cases, i, j, variable, f, hash[10];
	float k;
	cin>>test_cases;
	for(i=0; i<test_cases; i++)
	{
		for(j=0; j<10; j++)
			hash[j]=0;
		cin>>input_v;
		for(k=0; k<1000000; k++)
		{
			variable=input_v*(k+1);
			f=1;
			while(variable!=0)
			{
				hash[variable%10]=1;
				variable/=10;
			}
			for(j=0; j<10; j++)
			{
				if(hash[j]==0)f=0;
			}
			if(f==1)break;
		}
		if(f==1)
			cout<<"Case #"<<i+1<<": "<<input_v*(k+1)<<endl;
		else
			cout<<"Case #"<<i+1<<": INSOMNIA\n";
    }
    return 0;
}
