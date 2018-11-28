#include<iostream>

#include<cstdio>

using namespace std;

int main()
{
		FILE *in=freopen("B-large.in","r",stdin);

  		FILE *out =freopen("outputLarge.txt","w",stdout);
  		
  		int test,ptest,i;
  	cin>>test;
  	cin.ignore(256,'\n');
  	ptest=test;
  	while(test > 0)
  	{
  		int result;
		string given;
  		getline(cin,given);
  		if(given[0]=='-')
  			result=1;
  		else
		  result=0;
		  
		for(i=1;i<given.size();i++)
		{
			if(given[i]=='-' && given[i-1]=='+')
				result=result + 2;
		}
		cout<<"Case #"<<(ptest-test)+1<<":"<<" "<<result<<endl;
		 	
  		test--;
	  }
  		fclose(in);
fclose(out);
	return 0;
}
